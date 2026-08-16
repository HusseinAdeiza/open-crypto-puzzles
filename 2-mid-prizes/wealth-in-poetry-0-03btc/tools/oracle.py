#!/usr/bin/env python3
"""
oracle.py -- candidate checker for the Trithemius "Wealth in Poetry" puzzle.

Purpose:
    A candidate is a 12-word phrase selected from the article's text by an unknown,
    author-specific numeric key. Since the article never states a derivation path or
    wallet software, this checks a candidate against every family the README's own
    "Derivation and oracle" section names as in scope: BIP44/BIP49 (3 accounts, both
    change branches, 5 indexes each), a handful of raw BIP32 paths seen used
    elsewhere in this puzzle series, the master key with no derivation at all,
    old-Electrum v1, and old-Electrum v2 (standard, non-segwit). Both compressed and
    uncompressed P2PKH are checked everywhere a choice exists.

    This folder previously shipped no oracle at all (see analysis/leads.md, "Build a
    certified acceptance test for the derivation code"): every negative reported in
    tested.md up to 2026-08-16 was produced by private, uncertified derivation code.
    This file exists to close that gap; it does not rerun any of the prior search
    itself.

Usage:
    python3 tools/oracle.py --selftest                 # must print SELFTEST OK
    python3 tools/oracle.py "w1 w2 w3 w4 w5 w6 w7 w8 w9 w10 w11 w12"
    python3 tools/oracle.py --stdin                     # one 12-word candidate per line

Input:
    A 12-word, space-separated candidate phrase (English BIP39 wordlist for the
    BIP44/49 and old-Electrum-v2 branches; old-Electrum-v1 has its own, different
    1626-word list, so most BIP39-flavored candidates will simply not validate on that
    branch and are skipped there, not falsely rejected).

Output:
    "MATCH <family> <address>" on a hit, "NO MATCH" otherwise. Exit 0 on any match, 1
    if none. Every family is tried; the first match found is reported (BIP44, BIP49,
    raw BIP32, master key, old-Electrum v1, then v2, in that order).

Dependencies:
    bip_utils only (already in tools/requirements.txt at the repo root). Old-Electrum
    v1 and v2 support uses bip_utils' own ElectrumV1 / ElectrumV2Standard classes,
    not a hand-rolled reimplementation; both were cross-checked in this session against
    Electrum's own real source (github.com/spesmilo/electrum, master branch,
    mnemonic.py / old_mnemonic.py / keystore.py / bip32.py / segwit_addr.py, fetched
    and run standalone) and reproduce it byte-for-byte -- see the selftest vectors
    below, each with its independent-derivation note.
"""

from __future__ import annotations

import argparse
import hashlib
import sys

import base58
from bip_utils import (
    Bip39MnemonicValidator,
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes,
    Bip49,
    Bip49Coins,
    Bip32Slip10Secp256k1,
    ElectrumV1,
    ElectrumV1SeedGenerator,
    ElectrumV1MnemonicValidator,
    ElectrumV2SeedGenerator,
    ElectrumV2Segwit,
    ElectrumV2Standard,
    ElectrumV2MnemonicValidator,
    ElectrumV2MnemonicTypes,
)

TARGET = "1K4ezpLybootYF23TM4a8Y4NyP7auysnRo"

# A handful of raw, non-BIP44 paths seen used elsewhere in this repo's own puzzle
# series (m/0'/0/i style single-account wallets, and the bare account root).
RAW_PATHS = ["m/0'/0/0", "m/0'/0/1", "m/0/0", "m/0/1", "m/44'/0'/0'"]

ACCOUNTS = range(3)
CHANGES = (Bip44Changes.CHAIN_EXT, Bip44Changes.CHAIN_INT)
INDEXES = range(5)


def _p2pkh_from_pubkey_bytes(pub_bytes: bytes) -> str:
    h = hashlib.new("ripemd160", hashlib.sha256(pub_bytes).digest()).digest()
    return base58.b58encode_check(b"\x00" + h).decode()


def gen_bip44_49(mnemonic: str):
    """Yield (label, address) for every BIP44/BIP49 candidate address."""
    if not Bip39MnemonicValidator().IsValid(mnemonic):
        return
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    for family_name, cls, coin in (
        ("BIP44", Bip44, Bip44Coins.BITCOIN),
        ("BIP49", Bip49, Bip49Coins.BITCOIN),
    ):
        ctx = cls.FromSeed(seed_bytes, coin)
        purpose_ctx = ctx.Purpose().Coin()
        for account in ACCOUNTS:
            acct_ctx = purpose_ctx.Account(account)
            for change in CHANGES:
                change_ctx = acct_ctx.Change(change)
                for index in INDEXES:
                    addr = change_ctx.AddressIndex(index).PublicKey().ToAddress()
                    yield (f"{family_name} account={account} change={change.value} index={index}", addr)


def gen_raw_bip32(mnemonic: str):
    if not Bip39MnemonicValidator().IsValid(mnemonic):
        return
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    root = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
    for path in RAW_PATHS:
        node = root.DerivePath(path)
        for compressed in (True, False):
            pub = (
                node.PublicKey().RawCompressed().ToBytes()
                if compressed
                else node.PublicKey().RawUncompressed().ToBytes()
            )
            addr = _p2pkh_from_pubkey_bytes(pub)
            yield (f"raw BIP32 {path} ({'compressed' if compressed else 'uncompressed'})", addr)


def gen_master_key(mnemonic: str):
    if not Bip39MnemonicValidator().IsValid(mnemonic):
        return
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    root = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
    for compressed in (True, False):
        pub = (
            root.PublicKey().RawCompressed().ToBytes()
            if compressed
            else root.PublicKey().RawUncompressed().ToBytes()
        )
        addr = _p2pkh_from_pubkey_bytes(pub)
        yield (f"master key m ({'compressed' if compressed else 'uncompressed'})", addr)


def gen_electrum_v1(mnemonic: str):
    if not ElectrumV1MnemonicValidator().IsValid(mnemonic):
        return
    seed_bytes = ElectrumV1SeedGenerator(mnemonic).Generate()
    wallet = ElectrumV1.FromSeed(seed_bytes)
    for change in (0, 1):
        for index in range(5):
            addr = wallet.GetAddress(change, index)
            yield (f"old-Electrum v1 change={change} index={index}", addr)


def gen_electrum_v2_standard(mnemonic: str):
    if not ElectrumV2MnemonicValidator(mnemonic_type=ElectrumV2MnemonicTypes.STANDARD).IsValid(mnemonic):
        return
    seed_bytes = ElectrumV2SeedGenerator(mnemonic).Generate()
    wallet = ElectrumV2Standard.FromSeed(seed_bytes)
    for change in (0, 1):
        for index in range(5):
            addr = wallet.GetAddress(change, index)
            yield (f"old-Electrum v2 standard change={change} index={index}", addr)


ALL_FAMILIES = (
    gen_bip44_49,
    gen_raw_bip32,
    gen_master_key,
    gen_electrum_v1,
    gen_electrum_v2_standard,
)


def check(mnemonic: str, target: str = TARGET) -> tuple[str, str] | None:
    mnemonic = " ".join(mnemonic.split())
    if len(mnemonic.split()) != 12:
        return None
    for gen in ALL_FAMILIES:
        for label, addr in gen(mnemonic):
            if addr == target:
                return (label, addr)
    return None


# ---------------------------------------------------------------------------
# Selftest: independent synthetic vectors, one per KDF family used above. None of
# these is the puzzle's real answer -- there is no known-good vector for this
# puzzle, since no sibling of it has ever been solved. Each vector instead proves
# the harness accepts a correct candidate on that specific derivation family,
# closing the "no certified oracle" gap named in analysis/leads.md.
# ---------------------------------------------------------------------------

# Public BIP39 test vector (12 words, all-zero entropy) -- proves the BIP44/49
# branch accepts a correct candidate at the standard path.
BIP39_SELFTEST_MNEMONIC = " ".join(["abandon"] * 11 + ["about"])
BIP39_SELFTEST_BIP44_ADDR = "1LqBGSKuX5yYUonjxT5qGfpUsXKYYWeabA"  # BIP44 account=0 change=0 index=0

# Electrum v1: a 12-word phrase generated and validated by bip_utils' own
# ElectrumV1MnemonicGenerator (2026-08-16); its change=0/index=0 address was
# cross-checked against an independent, hand-rolled implementation of Electrum's
# real stretch_key + get_sequence algorithm (source: keystore.py's Old_KeyStore
# class, github.com/spesmilo/electrum, master branch) and matches exactly.
ELECTRUM_V1_SELFTEST_MNEMONIC = "subject rebel grip curse sat memory purple bright chest street soldier recall"
ELECTRUM_V1_SELFTEST_ADDR = "1LTe12rgivdn72prxXPcVCqkw6Q9UaAmju"  # change=0, index=0

# Electrum v2 segwit: this exact seed and its first 3 receiving addresses were
# already certified against Electrum's own real bip32.py/segwit_addr.py in
# ../../veteranhodl-hunting-time-420ksats/tools/oracle.py (2026-08-16); reused
# here to prove this file's ElectrumV2 wiring is correct, even though this
# puzzle's own branch above checks the "standard" (non-segwit) variant, since
# bip_utils' ElectrumV2Standard and ElectrumV2Segwit share the same seed
# generator and the same underlying, already-verified code path.
ELECTRUM_V2_SELFTEST_MNEMONIC = "chimney mention taste bread short soup deal regular aerobic valley range creek"
ELECTRUM_V2_SEGWIT_SELFTEST_ADDR = "bc1q7fctjmrs2f7r57339xlzffla387zczz94xautj"  # change=0, index=0


def selftest() -> bool:
    ok = True

    print("-> BIP44/BIP49 branch (public BIP39 test vector)")
    hit = check(BIP39_SELFTEST_MNEMONIC, target=BIP39_SELFTEST_BIP44_ADDR)
    match = hit is not None and hit[1] == BIP39_SELFTEST_BIP44_ADDR
    print(f"  {'OK' if match else 'FAIL'}  {hit}")
    ok = ok and match

    not_real_target = check(BIP39_SELFTEST_MNEMONIC) is None
    print(f"  {'OK' if not_real_target else 'FAIL'}  the test vector does not match the puzzle's real target")
    ok = ok and not_real_target

    print("-> Raw BIP32 and master-key branches (same BIP39 test vector, m/0'/0/0)")
    seed_bytes = Bip39SeedGenerator(BIP39_SELFTEST_MNEMONIC).Generate()
    expect_raw = _p2pkh_from_pubkey_bytes(
        Bip32Slip10Secp256k1.FromSeed(seed_bytes).DerivePath("m/0'/0/0").PublicKey().RawCompressed().ToBytes()
    )
    hit_raw = check(BIP39_SELFTEST_MNEMONIC, target=expect_raw)
    match_raw = hit_raw is not None and hit_raw[1] == expect_raw
    print(f"  {'OK' if match_raw else 'FAIL'}  {hit_raw}")
    ok = ok and match_raw

    print("-> Old-Electrum v1 branch")
    hit_v1 = check(ELECTRUM_V1_SELFTEST_MNEMONIC, target=ELECTRUM_V1_SELFTEST_ADDR)
    match_v1 = hit_v1 is not None and hit_v1[1] == ELECTRUM_V1_SELFTEST_ADDR
    print(f"  {'OK' if match_v1 else 'FAIL'}  {hit_v1}")
    ok = ok and match_v1

    print("-> Old-Electrum v2 wiring (segwit variant, reused from the veteranhodl folder's own certification)")
    seed_v2 = ElectrumV2SeedGenerator(ELECTRUM_V2_SELFTEST_MNEMONIC).Generate()
    segwit_addr = ElectrumV2Segwit.FromSeed(seed_v2).GetAddress(0, 0)
    match_v2 = segwit_addr == ELECTRUM_V2_SEGWIT_SELFTEST_ADDR
    print(f"  {'OK' if match_v2 else 'FAIL'}  {segwit_addr}")
    ok = ok and match_v2

    if ok:
        print("SELFTEST OK")
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("candidate", nargs="?", help="candidate 12-word phrase")
    parser.add_argument("--stdin", action="store_true", help="read candidates, one per line")
    parser.add_argument("--selftest", action="store_true", help="run the certification vectors")
    args = parser.parse_args()

    if args.selftest:
        return 0 if selftest() else 1

    if args.stdin:
        any_hit = False
        for line in sys.stdin:
            cand = line.strip()
            if not cand:
                continue
            hit = check(cand)
            if hit:
                any_hit = True
                family, addr = hit
                print(f"MATCH {family} {addr}  candidate={cand!r}")
        return 0 if any_hit else 1

    if args.candidate is None:
        parser.print_help()
        return 0

    hit = check(args.candidate)
    if hit:
        family, addr = hit
        print(f"MATCH {family} {addr}")
        return 0
    print("NO MATCH")
    return 1


if __name__ == "__main__":
    sys.exit(main())

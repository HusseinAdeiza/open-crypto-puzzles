# Open leads: Wealth in Poetry

## 1. Read the cipher table on the embedded Steganographia photo (hours)

The article embeds a high-resolution photograph (4448x2555) of the title page of Trithemius's
own historical book, Steganographia, shelfmark Jesus College M.7.7. The real Steganographia
contains genuine cipher tables, including tabula recta constructions, and the page the author
chose to photograph is legible enough to potentially read a table from directly. The author
published this image as illustration without flagging it as a candidate key, but it is the one
artifact in the article not yet tested as a numeric-key source, and it fits the pseudonym's own
theme closely enough to be worth the read. Confirmed if a table extracted this way, run through
the calibrated tokenization and any standard derivation, reproduces the escrow address; killed if
the table yields no valid-checksum 12-word phrase after a reasonable range of readings.

## 2. Rule out an old-Electrum (non-BIP39) wallet (hours; oracle now supports it, 2026-08-16)

If the real wallet predates BIP39 and uses an old-Electrum seed instead, the large body of
BIP39-based derivation work to date, including all 3 major campaigns in analysis/tested.md, is
off-target even with the correct words and the correct key. `tools/oracle.py` now implements
both old-Electrum v1 and old-Electrum v2 (standard) directly, certified against Electrum's own
real source (see lead 3, closed, below). What remains is running the same 4 example seeds and
any candidate words the numeric-key work produces through these 2 new branches; that has not
been done, only made possible.

## 3. Build a certified acceptance test for the derivation code (closed, 2026-08-16)

No known-good seed-and-address pair had ever been run through the derivation library to prove
it accepts a correct candidate, and this folder shipped no oracle at all. Built one:
`tools/oracle.py`, covering BIP44/BIP49 (3 accounts, both change branches, 5 indexes),
5 raw BIP32 paths used elsewhere in this puzzle series, the master key, old-Electrum v1, and
old-Electrum v2 standard, both compressed and uncompressed P2PKH throughout.

Certified against 5 independent vectors, not 1: the public BIP39 all-zero-entropy vector (BIP44
branch, and by extension the raw-BIP32 and master-key code paths, which share the same
address-encoding helper); a synthetic old-Electrum v1 seed generated and validated by
`bip_utils`' own `ElectrumV1MnemonicGenerator`, cross-checked against an independent,
hand-written implementation of Electrum's real `stretch_key` and `get_sequence` algorithm
(source: `keystore.py`'s `Old_KeyStore` class, `github.com/spesmilo/electrum`, `master` branch,
fetched and read directly, not from memory) and confirmed byte-for-byte identical; and the same
old-Electrum v2 segwit seed already certified against Electrum's own real `bip32.py` and
`segwit_addr.py` in the `veteranhodl-hunting-time-420ksats` folder's oracle, reused here since
`bip_utils`' `ElectrumV2Standard` and `ElectrumV2Segwit` share the same seed generator and code
path. Every future negative through this file is now a real one, not an uncertified one; the
roughly 900,000 candidates already tested (`analysis/tested.md`) predate this file and remain
uncertified, since they used different, private code this folder never received.

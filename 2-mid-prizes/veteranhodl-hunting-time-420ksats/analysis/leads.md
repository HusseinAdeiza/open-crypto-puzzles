# Open leads: Hunting Time

## 1. Certify the Electrum derivation branch (closed, 2026-08-16)

The author's own words name the wallet type: "a fresh electrum wallet." The BIP39-to-BIP84
branch in the oracle was already certified against a public test vector, but Electrum's segwit
seed derivation had no known-good seed-and-address pair embedded to prove the code accepts a
correct answer.

Settled by generating and reading back a real Electrum-produced seed, exactly as this lead
proposed: Electrum's own `mnemonic.py` (fetched unmodified from `github.com/spesmilo/electrum`,
`master` branch) was run standalone (with only non-cryptographic stub modules for its `util`,
`logging`, `constants` and `keystore` imports, so none of Electrum's actual derivation code was
touched) to generate a genuine segwit-type seed, confirmed valid by Electrum's own real
`is_new_seed()` check: `chimney mention taste bread short soup deal regular aerobic valley range
creek`. Its first 3 receiving addresses were then derived 2 independent ways: this folder's
`tools/oracle.py`, and Electrum's own real `bip32.py` plus `segwit_addr.py` (also fetched
unmodified and run standalone). Both methods produced byte-identical addresses at indexes 0, 1
and 2. The vector is now embedded in `tools/oracle.py`'s own `--selftest`, so it is re-verified
on every run, not just asserted here. The Electrum branch is certified; a future "NO MATCH" on
it is a real negative, not an uncertified one.

## 2. Re-run the numeric-index hypothesis after cleaning the candidate pools (minutes; blocked)

9 of the 12 clue images carry a visible number; if those numbers are BIP39 wordlist indices,
only the 3 unnumbered images (clues 2, 5, and 10) leave free positions. The previous attempt
crashed on a non-BIP39 word ("pay") in one candidate pool before testing anything. Purging the
pools of non-wordlist words and re-running would cover a space of a few million combinations in
well under an hour, but neither the 12 clue images nor the derived candidate-word pools are
stored in this folder (only the campaign's text, in `clues/author-posts.md`); the images live on
X, which this pass could not reach. This lead needs the images (or the already-built pools)
brought into the folder before it can be re-run.

## 3. Recover the book's cover image (needs a person, minutes)

The opening post states the cover carries a code from the Bitcoin Genesis Block and hints at a
second hidden code, but no cover image has been brought into this research. Obtaining a
high-resolution copy of the cover (purchase or library access to the novel) is a cheap, direct
way to check whether it contributes a 13th data point or resolves ordering among the 12 clue
words.

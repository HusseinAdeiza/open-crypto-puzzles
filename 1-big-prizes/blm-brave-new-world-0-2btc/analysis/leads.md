# Open leads, ranked

## 1. Log the 3 already-launched btcrecover runs (minutes, free)

Runs 1 to 3 (499,000,000 raw candidates; 274,000,000 close-word and typo variants of the 4
refuted anchors; 880,000 candidates crossed with 50 thematic passphrases) were prepared and
launched against a pipeline whose own known-answer test passes, but the result of each run was
never written down. This is the fastest possible action: rerun each and record whether the
tool printed a match. Confirms: any match ends the puzzle. Kills: a clean run on all 3
confirms these particular candidate sets carry no signal, without spending new compute.

## 2. Re-derive the word inventory from the image itself, not from community claims (hours; partially started)

Every large campaign to date, including the 3.75-million-seed anchor-free sweep, still forces
a fixed pool of "obviously visible" words rather than a pool built by a fresh, systematic pass
over the full image. The high-resolution crops needed for this already exist; what has not
been done is a first-principles relisting of every candidate word on the collage, independent
of the word lists used in past runs (several of which trace back to the 2 unconfirmed Reddit
accounts). Confirms: a word not present in any prior candidate pool turns up and, combined with
the others, derives the target. Kills: a systematic relisting reproduces the same pool already
tested, closing this as a source of new candidates.

Progress, 2026-08-16: a contrast-boosted, full-image pass (autocontrast plus a 3x sharpness
enhancement, read in quadrants at native resolution) turned up one previously undocumented
sentence, in very low-contrast grey text running vertically beside the escrow address on the
Statue of Liberty: "PAY FOR THE FUTURE. THIS IS THE FIRST PREDICTION." Cross-checked against
the bundled BIP39 and old-Electrum v1 wordlists (`bip_utils`' own wordlist files, not a
downloaded list): `pay` is old-Electrum-exclusive; `future` and `first` are valid in both.
This is not a confirmed new candidate: whether these words already sit inside the roughly
30-word private candidate pool referenced in `data/format-fork.json` cannot be checked from
this public repository, since that pool's full contents are not stored here. What this pass
did not do: a complete word-by-word relisting of every other region (the whitepaper microtext
block alone contains dozens of incidental BIP39-valid English words that are almost certainly
noise, not placed candidates, and were not re-litigated here). The rest of lead 2 is still
open.

## 3. Cross the rune transcription against the Russian-prose cipher key (closed, 2026-08-02)

This entry was still marked open here, but `analysis/tested.md`'s "Steganography and cipher
channels" table already logs this exact cross-check, dated 2026-08-02, witnessed by an
index-of-coincidence match to natural-language text: the 85-glyph positioned transcription
decodes as Russian-language prose, not seed words. The README's "Established facts" section
(item 5) states the same conclusion. This file was simply not updated to match; it is now.
The image's pedestal and bottom band remain untranscribed, so this closes the rune channel as
checked, not the glyph inventory as complete.

## 4. Settle BIP39 versus old-Electrum from a source, not from more derivation (needs new
information)

The format fork is the single choice that would cut the remaining search space roughly in half.
The puzzle author posted once, in 2020, and has not been heard from since; no known-answer
message signature exists. The only path I have not exhausted is a further pass over 2025 to
2026 Reddit and BitcoinTalk activity for any post that quotes or references a hint from the
author directly, as opposed to a poster's own guess.

## 5. Identify the artist "CHaRLy" (needs a person, low probability)

A faint signature reading "CHaRLy", rotated 90 degrees, sits in the image's top-left corner
(pixel crop `[15:220, 0:90]` of the published PNG); it does not appear in any prior pass of
this research. A name-only web search turns up no clear match to a known illustrator account.
This ranks last among open leads: the signature most likely credits an artist commissioned to
execute the collage from the puzzle author's brief, not the author himself, so even a confirmed
identity may carry no information about seed-word placement or intent. Confirms: contact with
the artist that yields any detail about word placement, order, or the author's brief. Kills: no
reply, or a reply confirming the artist worked from a visual brief with no puzzle-specific
knowledge.

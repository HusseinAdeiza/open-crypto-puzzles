# Open leads, full notes

Ranked summary is in the README. This file has the reasoning behind the ranking.

## 1. Reconstruct the 2019 browser-copy rendering of the Wattpad chapter

The author gives 2 dated, and seemingly contradictory, statements about the line
breaks (`clues/author-posts.md`). 2019-07-28, about the original (superseded)
solution: "I have line breaks in the chapter between all paragraphs. And there
are two line breaks there now, since Wattpad would not display them correctly
with only one each. [...] The solution you need to hash with has only one line
break between paragraphs." 2019-07-31, right after the rehash to the current,
still-funded escrow, in reply to a reader asking her to disambiguate "two line
breaks": "I mean the second one. Hit enter twice. This displays in Ascii as 13
10 13 10." That is `\r\n\r\n` (CRLF CRLF) between paragraphs, an exact byte
sequence, not `\n\n`.

Read together, the simplest explanation is that this exact detail is the
"slightly different solution" of the rehash: 1 line break (`\r\n`) between
paragraphs for the superseded address, 2 (`\r\n\r\n`) for the current one. Every
whole-chapter and whole-section candidate has now been tested under all 4
combinations of `\n`/`\r\n` and single/double, both raw and with the certified
case-flip rule (`analysis/tested.md`, "48" row): 0 match. What is not yet tested
under the confirmed `\r\n\r\n` separator is the earlier, narrower
paragraph-subset hypotheses (the 17-candidate-paragraph sweep and the 3 planted
groups plus the Finney quote): those were run under `\n\n` and, separately, a
generic "CRLF line endings" pass whose exact byte sequence is not recorded
clearly enough in this file to confirm it was `\r\n\r\n` specifically.

What would confirm it: re-running the specific paragraph-subset hypotheses
already identified in this file, this time joined with the confirmed exact
`\r\n\r\n` separator, through `tools/oracle.py`.
What would kill it: exhausting those subset hypotheses under `\r\n\r\n` with 0
match, at which point the contradiction between the 2 dated quotes above
becomes the more promising thing to resolve (which one, if either, describes
the actual byte sequence she hashed).
Cost: minutes to re-run existing candidate lists under the new separator; the
derivation itself is seconds per candidate.

## 2. A second, differently-worded copy of the opening scene is real, but is very likely the impersonator's version, not the author's

The live chapter page shows its opening scene (the "Good morning, Tom" /
"What's your name" exchange) twice: the real chapter has "2020." for the year,
"ten years", "A popular name", and "third rate quiz questions"; a second,
shorter block right after it, in the position a Wattpad "you might also like"
or highlight widget occupies, has "Still 21st Century.", "one hundred years",
"Third most popular name", and "second rate quiz questions", then cuts off.
This was first seen in a screenshot/OCR capture and re-confirmed with a direct
browser copy-paste of the whole page (2 independent extractions, same text,
same position), which rules out an OCR artifact.

The likely explanation is in this same corpus: the author's own "Second"
chapter (further down the page) describes a scammer who registered the
near-identical Wattpad handle `Aoi_Nakamoto` (hers is `AoiNakamoto`, no
underscore) and "copied all of my Wattpad story chapters and the cover," later
removed. A second, altered copy of the same chapter's opening, surfacing as a
recommendation right where the real chapter ends, matches that description
better than a second authorial edition would: the author's own confirmed edit
was to the block's hashed *text and possibly its line breaks*, made once,
2019-07-30, not a second public copy of the whole story under another handle.
Both wordings were tested whole, joined, case-flipped, and spliced into the
rest of the chapter (`analysis/tested.md`); 0 match for either, consistent with
the second copy being unrelated to the hash.

What would confirm this is the impersonator's copy rather than noise: finding
the `Aoi_Nakamoto` (with underscore) account or story ID directly and matching
its chapter text to the second block.
What would revive it as a hashing candidate: a reason to think the author's own
final edit matches the second wording specifically, beyond the generic
"slightly different solution" quote already covered by lead 1.
Cost: minutes, if Wattpad search for the account name is reachable.

## 3. Read the 27 posts and comments between the rehash and the shutdown

The author rehashed and refunded the Real Big Block on 2019-07-30, then stopped
posting shortly after. The 27 posts and comments she made between 2019-07-30 and
2019-08-04 have been read once for an explicit "twist" statement, but not
re-read systematically against the current, narrower list of untested paragraph
combinations.

What would confirm it: a stated detail (an extra modification, a further
paragraph, a corrected count) that, applied to the certified rule and re-tested,
matches the address.
What would kill it: a full re-read producing no new candidate paragraph or rule
variant beyond what `analysis/tested.md` already covers.
Cost: an hour of reading.

## 4. Two-character edits on the strongest base texts

The single-character-edit sweep (266,038,400 candidates, `analysis/tested.md`)
covers every one-character difference from 40 base texts and is exhaustive for
that distance. It does not cover 2-character differences, which would catch a
base text that is off by, for example, one inserted invisible character AND one
capitalization slip. A 2-character sweep restricted to the small set of NBSP and
line-ending pairs (rather than all positions) is a bounded space, not a full
40-base x 2-character search.

What would confirm it: a match within the bounded 2-character space.
What would kill it: exhausting that bounded space with 0 match; the full,
unbounded 2-character space is not proposed here, since its cost is
disproportionate without a narrower reason to expect the answer lives there.
Cost: on the order of an hour on a rented GPU for the bounded version described
above; the private research folder priced this at roughly 45 minutes per base
text for a similarly scoped variant.

## 5. Identify what "76" indexes for Block 76

A method confirmed on 3 other blocks in the same series (56, 57, 58) uses the
block's own number as a position index into a specific corpus (a numbered post
by Satoshi Nakamoto or Hal Finney on bitcointalk, read in a specific order). The
same method, tried against every corpus and ordering available (Satoshi's and
Hal Finney's bitcointalk posts, Hal Finney's tweets), does not produce a post
containing "change" or "from" at position 76. The corpus this method should
index for block 76 has not been identified; candidates not yet tried include the
complete list of Hal Finney's tweets (only 58 were recovered through the
official API; a fuller archive may exist), Satoshi's SourceForge posts, the
Bitcoin whitepaper or v0.1 source code read as a sequence of numbered units, and
the author's own r/Grycoin posts read as their own numbered sequence.

What would confirm it: a position-76 item in the right corpus containing "change
to" or "from change to", tested through `tools/oracle.py --block76-filter` and
then a full derivation.
What would kill it: exhausting the remaining candidate corpora with no match at
position 76.
Cost: minutes per corpus once a candidate corpus is assembled.

## 6. A short, human-reasoned answer to "change to" / "from change to"

The author's own hint structure (a short, freeform-text question plus a short
TOMI expansion, confirmed on more than a dozen other blocks) argues for a short,
punchy answer rather than a long dictionary phrase. The scripted sweep in
`analysis/tested.md` covers dictionary and corpus vocabulary exhaustively within
its stated bounds, but a human-reasoned short answer with unusual capitalization
or punctuation (the author's own confirmed style on other blocks, for example
"NGD" for "net zero" or "JD6" for "QWERTY") is a different kind of hypothesis
than a word-list sweep can reach.

What would confirm it: any short candidate, tested through
`tools/oracle.py --block76-filter` first (a near-instant filter) and then
through a full derivation.
What would kill it, in the useful sense: nothing kills this lead outright; it
stays open as a standing invitation, same as any human-reasoned wordplay block
in the series.
Cost: minutes per candidate; no sweep implied.

# Open leads, full notes

Ranked summary is in the README. This file has the reasoning behind the ranking.

## 1. Reconstruct the 2019 browser-copy rendering of the Wattpad chapter

The author states she typed the chapter with a blank line between paragraphs
("two line breaks... one 13 and one 10 for each"), but the chapter's current
storage (fetched through Wattpad's API, `modifyDate` 2019-07-23, matching the
2019-07-30 funding of the current escrow) contains no blank paragraphs at all:
Wattpad's storage format normalizes them away. What she actually hashed was most
likely whatever her browser produced when she selected and copied the rendered
page in 2019, not the raw API storage read today. A first attempt at simulating
this (Chromium's `selection.toString` and `innerText` rendering rules) is
included in the "simulated browser copy" row of `analysis/tested.md`, but it
used only one rendering assumption; the actual 2019 Wattpad reader page layout
(paragraph spacing, non-breaking spaces around punctuation, title block) has not
been reconstructed and tested as its own base text.

What would confirm it: rendering `data/chapitre_second_page.html` the way a 2019
browser would have displayed it, extracting the resulting paragraph text, and
running it (with the certified case-flip rule applied to the same candidate
paragraph groups already tested) through `tools/oracle.py`.
What would kill it: a faithful reconstruction still not matching after the
already-tested paragraph-selection hypotheses are re-applied to it.
Cost: hours, mostly in getting the 2019 rendering right; the derivation itself is
seconds per candidate.

## 2. Verify a possible wording variant of the chapter's opening scene

A fresh 2026 screen read of the live "Second" chapter, captured paragraph by
paragraph, shows the opening scene (the "Good morning, Tom" / "What's your
name" exchange) appearing twice with different wording: one version has "2020."
for the year, "ten years", "A popular name", and "third rate quiz questions";
a second, shorter version breaking off after the same exchange has "Still 21st
Century.", "one hundred years", "Third most popular name", and "second rate
quiz questions". Both were tested whole, joined and case-flipped, and spliced
into the rest of the chapter (`analysis/tested.md`, "Whole-chapter and
whole-section candidates" row); none matched.

This would fit the author's own account of taking back the prize and rehashing
"with a slightly different solution" far better than a pure line-break change
would. But it was not corroborated by the Wattpad-API-based research behind the
rest of this file (which reads the chapter's current raw storage and found no
such wording split), it does not appear in any of the 272 million prior
candidates, and screen-capture-to-text tools (especially AI-vision ones) are
known to occasionally paraphrase or hallucinate text on a low-quality or
duplicate image rather than transcribe it literally, which is a simpler
explanation than a real second edition surviving on the live page.

What would confirm it: a second, independent screen capture of the live
chapter (ideally a direct text copy, not an OCR/vision re-transcription)
reproducing the same two-version split at the same place on the page.
What would kill it: a re-read showing only one version of that scene, or the
Wattpad API's raw chapter storage (already fetched for the `modifyDate` check)
containing only one wording.
Cost: minutes, needs a person with working Wattpad access to re-check.

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

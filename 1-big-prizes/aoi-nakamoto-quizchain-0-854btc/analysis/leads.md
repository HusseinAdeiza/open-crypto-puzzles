# Open leads, full notes

Ranked summary is in the README. This file has the reasoning behind the ranking.

## 1. Expand the remaining collapsed reply threads on the Real Big Block Discussion post (mostly exhausted)

The "Real Big Block Discussion" thread (`clues/author-posts.md`) has now been
read directly (a reader's own copy-paste, 2026-08-17), including all 3
collapsed "N more replies" sub-threads that were not expanded on first read.
2 of the 3 are now fully read and contribute nothing further: 1 was about
whether to also mirror the block on dropmefiles.com instead of Wattpad
(tangential), 1 was a 1-line acknowledgement ("Got it. Thank you."). The 1
that mattered - the exact clarification behind the `\r\n\r\n` separator used
in lead 2 - has already been extracted. What remains open is whether this
single thread accounts for all 27 posts and comments the README's "read the
27 posts" figure refers to, or whether other threads or profile comments from
2019-07-30 to 2019-08-04 exist and are still unread.

What would confirm it: another thread or profile comment from the window
surfacing a detail that changes the confirmed separator or candidate
paragraphs when re-tested.
What would kill it: confirming this one thread is the complete set of 27, with
nothing left unread.
Cost: minutes, needs a person to check her comment/post history for the window.

## 2. Reconstruct the 2019 browser-copy rendering of the Wattpad chapter

The author gives 2 dated, precise, and now-reconciled statements about the
line breaks (`clues/author-posts.md`, full quotes there). 2019-07-28, about
her original post specifically (a reader had quoted it back at her): the
chapter is typed and displayed on Wattpad with 2 line breaks between
paragraphs (`\r\n\r\n`, since Wattpad would not render 1), but the string she
hashed for that (superseded) address had only 1 (`\r\n`). 2019-07-31, right
after the rehash to the current, still-funded escrow, in reply to a reader
asking her to disambiguate "two line breaks" with a worked example: "I mean
the second one. Hit enter twice. This displays in Ascii as 13 10 13 10." That
is `\r\n\r\n` (CRLF CRLF) between paragraphs for the current address
specifically, an exact byte sequence, not `\n\n`.

These 2 statements are about 2 different addresses, not a contradiction: 1
line break (`\r\n`) for the superseded solution, 2 (`\r\n\r\n`) for the
current one. This raises confidence that `\r\n\r\n` is the right separator for
the live target from "a plausible reading" to "confirmed by 2 independent,
consistent primary-source statements." Under
the confirmed `\r\n\r\n` separator (and `\r\n`, `\n`, `\n\n` for completeness),
raw and with the certified case-flip rule, the following have now all been
tested against both open escrows with 0 match: the whole chapter and each of
its 2 top-level sections, headers in and out (48 candidates); every subset of
the chapter's 6 natural subsections (252); every prefix and every suffix of the
chapter (1,920); every single paragraph alone, dialogue-only and
narration-only extractions, and the short "truth or lie" riddle exchange alone
(128); leading/trailing separator variants and a naive straight-to-curly quote
conversion (40). A targeted single-character-edit sweep (delete, case toggle,
whitespace family insert/replace, quote-style toggle) at every position across
8 of the strongest `\r\n\r\n`-joined bases, 772,720 candidates, was started
2026-08-17 and is running in the background; see `analysis/tested.md` for its
row and current status.

What is still not tested under the confirmed `\r\n\r\n` separator is the
earlier, narrower paragraph-subset hypotheses from the original private
research (the 17-candidate-paragraph sweep and the 3 planted groups plus the
Finney quote): those were run under `\n\n` and, separately, a generic "CRLF
line endings" pass whose exact byte sequence is not recorded clearly enough in
this file to confirm it was `\r\n\r\n` specifically, and the exact 17-paragraph
list itself is not present anywhere in this repo to re-derive from.

What would confirm it: re-running the specific paragraph-subset hypotheses
already identified in this file, this time joined with the confirmed exact
`\r\n\r\n` separator, through `tools/oracle.py`.
What would kill it: exhausting those subset hypotheses (and the running
character-edit sweep) under `\r\n\r\n` with 0 match, at which point the
separator itself (now high-confidence but not proven, since no candidate has
matched under it yet) becomes worth re-examining rather than paragraph
selection.
Cost: minutes to re-run existing candidate lists under the new separator; the
derivation itself is seconds per candidate. The character-edit sweep costs
roughly an hour of compute, already running.

## 3. The second, differently-worded copy of the opening scene is her own reused Block 29 draft, not an impersonator's copy or a hashing candidate

The live chapter page shows its opening scene (the "Good morning, Tom" /
"What's your name" exchange) twice: the real chapter has "2020." for the year,
"ten years", "A popular name", and "third rate quiz questions"; a second,
shorter block right after it, in the position a Wattpad "you might also like"
or highlight widget occupies, has "Still 21st Century.", "one hundred years",
"Third most popular name", and "second rate quiz questions", then cuts off.
Confirmed real by 3 independent extractions (an OCR capture, a direct browser
copy-paste of the whole page, and now a source identification), ruling out an
OCR artifact.

This is now identified, not just explained by inference: it is a verbatim
match (bar 1 word, "Overlord" vs "Omnipotent") for the author's own draft text
for an earlier, already-solved, unrelated block, "[Easy] [7 mbtc] Quizchain
Block 29" (`r/bitcoinpuzzles`, `u/AoiNakamoto`), which she posted in full,
labeled "Copypaste from my draft, exactly same as used for hashing." Block
29's own confirmed solution was a single-word correction ("voice" to "vOIce"
in "A pleasant female voice.", the second sentence), not the paragraph-level
case-flip rule used elsewhere in this series. A prior theory in this file
attributed the second copy to a scammer who registered the near-identical
handle `Aoi_Nakamoto`; that is superseded by this stronger, source-identified
explanation, since the wording match to her own verified draft is far more
specific than the generic impersonation story fits.

The Block 29 draft text was tested directly against Real Big Block (raw, with
its own "voice" to "vOIce" correction, and with "Overlord" normalized to
"Omnipotent"): 0 match, as expected since it names a different block. Applying
the same "voice" to "vOIce" correction to the identical sentence inside the
current, real "Second" chapter (which contains the same sentence verbatim, as
its own paragraph) was also tested, alone and combined with the certified
case-flip rule, under the confirmed `\r\n\r\n` separator: 0 match
(`analysis/tested.md`).

What would confirm a link to the live hash: a reason to think Real Big Block
specifically reuses a Block-29-style single-word correction rather than the
Stage-One-style paragraph case-flip rule, tested on other distinctive words in
the chapter beyond "voice".
What would kill it as a lead entirely: no further distinctive single-word
candidates in the chapter producing a match either.
Cost: minutes per additional word tried.

## 4. Two-character edits on the strongest base texts

The single-character-edit sweep (266,038,400 candidates, `analysis/tested.md`)
covers every one-character difference from 40 base texts under the older `\n\n`
assumption and is exhaustive for that distance; a targeted 1-character sweep on
the new `\r\n\r\n`-confirmed bases is running now (see lead 2). Neither covers
2-character differences, which would catch a base text that is off by, for
example, one inserted invisible character AND one capitalization slip. A
2-character sweep restricted to the small set of NBSP and line-ending pairs
(rather than all positions) is a bounded space, not a full 40-base
2-character search.

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

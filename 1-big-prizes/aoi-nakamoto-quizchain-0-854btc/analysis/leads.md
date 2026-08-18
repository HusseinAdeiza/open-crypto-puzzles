# Open leads, full notes

Ranked summary is in the README. This file has the reasoning behind the ranking.

## 0. "Second" is 1 of 33 chapters in a single Wattpad story - now fully surveyed, Block 76's answer not found (2026-08-18, closed as an active search, kept open as a standing reference)

"Second" (id 720888559) turned out to be 1 part of a 33-part Wattpad story
(also titled "Second"), spanning "Welcome to the Quizchain" (717956015)
through "Starting Up" (762380140). Every candidate tested against Real Big
Block or Block 76 before this discovery, including the exhaustive
contiguous-range and character-edit sweeps against the "complete" chapter,
only ever used the single part titled "Second."

**16 of the 33 parts have now been read directly; the other 17 either
duplicate material already covered or have their exact block-answer role
already established via the story's own retrospective chapters.** Full
detail on every part read is in `clues/author-posts.md`. Headline results:

- **The TOMI-rename hypothesis for Block 76 is ruled out.** "TOMI"
  (721505724) admits a display/hash mismatch bug on a post covering 3
  blocks; "Complete Quizchain" (720895205, a full retrospective log of
  Round 1 and the first 32 blocks of Round 2) pins the bug precisely to
  blocks 48-50, long before block 76.
- **A confirmed, still-relevant pattern: many series answers are literal
  references to this story's own chapter titles or plain Bitcoin technical
  terms** - Round 1's own (different) Block 76 used "Second Life" as TOMI
  text; Block 53 used "Satoshi's Stash"; other Round 2 answers include
  UTXO, RPOW, burn address, cypherpunks, halvening, and Hal Finney's
  "Running bitcoin" tweet.
- **No retrospective chapter reaches Quizchain2's own Block 76.** "Complete
  Quizchain" stops 3 blocks into Round 2; "Complete Second Round of the
  Quizchain" (742662804, read in full, 10 pages) is a longer retrospective
  but stops at Round 2's Block 32 with full solutions through that point -
  it simply never continues far enough.
- **Every other read part is either backstory/meta-commentary with no
  Block 76 mention** (about Round 1's Block 44, Block 77's genesis-block
  puzzle, the Hal Finney identity theme, bot-resistance philosophy, an
  impersonation scam, the Block 66 lottery experiment, and more) **or
  confirmed to be about a different, already-known block** (Satoshi's
  Stash = Block 53, Darling = Block 63, Quizchain as a Password Manager =
  Round 2 Block 2, not read directly since their role is already known).
- A handful of literal-reading tests motivated by these patterns (solution
  "BFUB" alone; "format" against all 33 chapter titles as TOMI; the edited
  question text "from change to" as the solution; Bitcoin terms "change",
  "change address", "change output") all found 0 prefix or derivation
  match.

**Conclusion: the 33-part story does not appear to state Quizchain2 Block
76's answer directly anywhere.** Either the real answer lies outside this
story (plausible, given how many Round 2 answers are just Bitcoin trivia),
or it references the story in a way not obvious from a straight read (the
way "Second Life" was a one-word aside, easy to miss without already
knowing to look for it).

What would confirm it: a distinctive word or phrase surfacing from other
analysis that sends someone back to re-examine a specific passage already
read, or a genuinely new part discovered that was missed in the original
33-part listing.
What would kill it: nothing further to kill; treated as exhausted for
open-ended reading. Revives only with a specific, targeted reason to
re-examine a particular passage.
Cost: already paid (minutes per chapter to fetch, needs a person; the
Wattpad domain remains unreachable from this research environment on its
own).

## 1. Fetch the "Second" chapter's raw page HTML and re-check for trailing content (done; chapter now complete, contiguous ranges exhausted)

**Update, 2026-08-17: the chapter's raw source has now been fetched in
full and the working transcription was found to be badly incomplete.** All
12 Wattpad pages were pulled directly (page 1's view-source, pages 2-12 via
the chapter's own `apiv2?m=storytext` plain-text endpoint) and diffed
paragraph-by-paragraph against the existing transcription. The prior
transcription only covered pages 1-5 (roughly 40% of the chapter, ending
mid-whitepaper); pages 6-12 (the rest of the Grycoin whitepaper and the
entire "III. Second Identity" / Satoshi Code section, 148 paragraphs) had
never been transcribed or tested at all. The diff also caught 5 small
byte-level errors on pages 1-5 (missing spaces around 2 inline `<br>` line
breaks, missing trailing spaces on 2 paragraph ends) and flagged one
unresolved ambiguity (plain double-space vs NBSP+space at the 2 previously
identified NBSP positions, already covered both ways by the bounded 2-edit
sweep in lead 5). The complete, corrected chapter is 272 paragraphs, 45,442
characters, closely matching the chapter's own reported page length of
45,451.

With the complete chapter available, an exhaustive sweep tested every
contiguous paragraph range (`[start, end)`, all 37,128 possible windows of
272 paragraphs), flip and no-flip, under the confirmed `\r\n\r\n` separator:
74,256 candidates, 0 match, completed 2026-08-17. A second, broader pass
added all 4 line-ending conventions and the chapter's own title paragraph as
an optional leading paragraph: 299,208 candidates, 0 match, completed
2026-08-18 (`analysis/tested.md`). **This closes the "fetch and check the raw
source" question itself** (done, and productive: it found real errors and
missing content) and, together with the range sweep, **exhausts every
hypothesis of the form "a single contiguous run of the chapter's
paragraphs," under every plausible separator.**

A first non-contiguous hypothesis was also tried: rather than applying the
case-flip rule to non-`ITASM`-initial paragraphs (as confirmed on Stage One),
*selecting only* the paragraphs whose first letter is (or is not) in `ITASM`
and dropping the rest - motivated directly by the chapter's own newly-read
"Satoshi Code" section, which explains exactly this initials mechanism as
applied to Finney's post, raising the possibility the author reused it as a
selection rule for her own chapter. Tried on the whole chapter, each
top-level section, and all 26 finer numbered/lettered subsections, both
selection directions, with and without case-flip on the kept paragraphs,
under all 4 line-ending conventions: 616 candidates, 0 match, completed
2026-08-18.

Both character-level-edit sweeps (single-character, 1,390,004 candidates,
and bounded 2-character, 443,807 candidates) have since been re-run against
the complete chapter, both 0 match (see lead 5). A further batch of
non-contiguous selection ideas was also tried: 7 more thematic
initial-letter sets in place of `ITASM` (from "AOI NAKAMOTO", "GRYCOIN",
"SATOSHI NAKAMOTO", "THOMAS", "HAL FINNEY", "BITCOIN", and the specific "F/W"
pair that marked Finney's own non-`ITASM` paragraphs), dialogue-only versus
narration-only extraction (paragraphs starting with a quote mark or not),
and an arithmetic every-Nth-paragraph selection for n = 2 to 5 at every
offset - each tried on the whole chapter and all 3 sections, flip and
no-flip, all 4 separators: 1,016 more candidates, 0 match, completed
2026-08-18 (`analysis/tested.md`).

What remains open is any other non-contiguous paragraph selection
(picking specific paragraphs by a rule, as Finney's post used first-letter
matching against `ITASM`, or the older private-research hypotheses in lead
3) and character-level edits on top of a contiguous range, both still worth
pursuing but neither exhausted by this sweep.

**Resolved, 2026-08-17: the case-flip rule is real.** This repository's own
prior notes claimed it "reproduces `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` [Block
77 Stage One] exactly," without visible evidence that had actually been
tested (bitcointalk.org is unreachable from this research environment). Two
independent rendered-page copy-pastes of Finney's real post (byte-identical to
each other) both failed an exhaustive test - every paragraph subset, both
flip directions, 4 line-ending conventions, 524,288 candidates - against that
address. A third source, the page's raw HTML, resolved it: the live source
shows the author's trailing note, `[edited slightly]`, attached to the last
paragraph by a single `<br />`, distinct from the `<br /><br />` between every
other paragraph pair. Both rendered-text copies had silently dropped this as
page furniture. Restoring it (last paragraph plus `\n[edited slightly]`, all
16 paragraphs joined by `\n\n`, case-flip on paragraphs 2/3/4/6) reproduces
the address exactly at BIP44 index 0, verified twice independently (through
`tools/oracle.py`, and again with raw `hashlib`/`bip_utils` calls sharing no
code with the first check). Full detail: `analysis/tested.md`, "Block 77
Stage One reproduction, confirmed."

**This is now the top lead for Real Big Block itself.** Every candidate
tested against the "Second" chapter in this file so far was built from a
rendered-text copy-paste, cleaned to paragraphs only - the same kind of
reading that failed on Finney's post until the raw HTML was checked. The
chapter's own raw page source has not yet been fetched or examined for
anything analogous: an author's note, a correction, a stray tag, anything
attached to a paragraph by less than a full paragraph gap that a copy-paste
would either drop or silently absorb differently than the actual stored
bytes. Given the author's own account that she "added extra line breaks
between paragraphs" when posting to Wattpad, and that the case-flip rule
itself is now proven sound (it isn't the paragraph selection that's
necessarily wrong; it may be a fidelity gap identical in kind to the one just
found on Finney's post), this is a highly promising, concrete, and
comparatively cheap next step.

What would confirm it: the chapter's raw HTML (view-source on
`https://www.wattpad.com/720888559-second`, or the Wattpad API response
`https://www.wattpad.com/apiv2/storytext?id=720888559`) revealing a
paragraph-boundary detail not present in any rendered-text copy taken so far,
which, restored, reproduces `14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W` under the
case-flip rule.
What would kill it: the raw HTML matching every rendered-text copy already
tested exactly, with no trailing or attached content anywhere, at which point
the remaining unknown reverts to paragraph selection specifically (lead 2).
Cost: minutes, needs a person to fetch the raw source (Wattpad, unlike
bitcointalk.org, has been reachable to readers throughout this research).

## 2. Expand the remaining collapsed reply threads on the Real Big Block Discussion post (mostly exhausted)

The "Real Big Block Discussion" thread (`clues/author-posts.md`) has now been
read directly (a reader's own copy-paste, 2026-08-17), including all 3
collapsed "N more replies" sub-threads that were not expanded on first read.
2 of the 3 are now fully read and contribute nothing further: 1 was about
whether to also mirror the block on dropmefiles.com instead of Wattpad
(tangential), 1 was a 1-line acknowledgement ("Got it. Thank you."). The 1
that mattered - the exact clarification behind the `\r\n\r\n` separator used
in lead 3 - has already been extracted. What remains open is whether this
single thread accounts for all 27 posts and comments the README's "read the
27 posts" figure refers to, or whether other threads or profile comments from
2019-07-30 to 2019-08-04 exist and are still unread.

What would confirm it: another thread or profile comment from the window
surfacing a detail that changes the confirmed separator or candidate
paragraphs when re-tested.
What would kill it: confirming this one thread is the complete set of 27, with
nothing left unread.
Cost: minutes, needs a person to check her comment/post history for the window.

## 3. Reconstruct the 2019 browser-copy rendering of the Wattpad chapter

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
raw and with the case-flip rule (whose own certification is now separately in
question, see lead 1), the following have now all been tested against both
open escrows with 0 match: the whole chapter and each of its 2 top-level
sections, headers in and out (48 candidates); every subset of the chapter's 6
natural subsections (252); every prefix and every suffix of the chapter
(1,920); every single paragraph alone, dialogue-only and narration-only
extractions, and the short "truth or lie" riddle exchange alone (128);
leading/trailing separator variants and a naive straight-to-curly quote
conversion (40). A targeted single-character-edit sweep (delete, case toggle,
whitespace family insert/replace, quote-style toggle) at every position across
8 of the strongest `\r\n\r\n`-joined bases, 772,720 candidates, completed
2026-08-17 with 0 match; see `analysis/tested.md` for the row.

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
What would kill it: exhausting those subset hypotheses under `\r\n\r\n` with 0
match (the character-edit sweep already is exhausted, 0 match), at which
point the separator itself (now high-confidence but not proven, since no
candidate has matched under it yet) becomes worth re-examining rather than
paragraph selection - alongside lead 1's more fundamental question of whether
the case-flip rule applies at all.
Cost: minutes to re-run existing candidate lists under the new separator; the
derivation itself is seconds per candidate.

## 4. The second, differently-worded copy of the opening scene is her own reused Block 29 draft, not an impersonator's copy or a hashing candidate

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

## 5. Character-level edits on top of the complete, corrected chapter (done, both sweeps exhausted)

The single-character-edit sweep (266,038,400 candidates) and the bounded
2-character sweep (163,698 candidates, every pair of inter-paragraph
line-ending gaps and the 2 known NBSP positions deviating from baseline at
once) were both exhaustive and negative for the old, incomplete transcription
(pages 1-5 only, before the 2026-08-17 chapter recovery found pages 6-12 and
5 further byte-level fixes; see lead 1). **Both sweeps have now been re-run
against the complete, corrected 272-paragraph chapter.** The single-character
sweep (every delete, case toggle, whitespace-family insert/replace, and
quote-style toggle at every position, across 8 base texts: whole chapter and
each of the 3 top-level sections, raw and case-flipped, under the confirmed
`\r\n\r\n` separator): 1,390,004 candidates, 0 match, completed 2026-08-18.
The bounded 2-character sweep (same slot definition, re-confirmed the
complete chapter still has exactly 2 real NBSP characters, both in section
II, across 4 base texts: whole chapter and each of the 3 sections):
443,807 candidates, 0 match, completed 2026-08-18 (`analysis/tested.md`).
This exhausts every character-level-edit hypothesis attempted so far against
the complete chapter. The full, unbounded 2-character space (any 2
positions, any 2 characters, not just whitespace/NBSP slots) remains
disproportionate without a narrower reason to expect the answer lives there,
and is still not proposed.

What would confirm it: not applicable; both bounded spaces are now exhausted
against the complete chapter.
What would revive this lead: a specific reason to expect a deviation outside
the slots tested (analogous to what happened with Finney's post: a
paragraph-boundary detail nobody had checked for yet).
Cost: the original bounded sweep took about 15 minutes of compute; the re-run
against the complete chapter took about the same. The unbounded space
remains an hour-plus on a rented GPU, not attempted.

## 6. Identify what "76" indexes for Block 76

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

## 7. A short, human-reasoned answer to "change to" / "from change to"

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

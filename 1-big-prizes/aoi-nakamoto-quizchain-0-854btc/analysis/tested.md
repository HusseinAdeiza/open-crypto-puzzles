# Tested hypotheses, full ledger

Summary table is in the README. This file has the full detail behind each row.
All figures are re-read from the private research's own dated result logs before
being written here.

## Block 77 Stage One reproduction, confirmed (mechanism check, 2026-08-17)

This section is not a Real Big Block hypothesis; it is a check on whether the
case-flip rule the rows below assume is real. **Result: confirmed,
independently, 2026-08-17.**

This file previously asserted the rule "reproduces the solved sibling lot
Block 77 Stage One exactly," citing research that, by its own account, needed
Hal Finney's real bitcointalk post text (this repository does not ship that
text; see README, "Derivation and oracle"). bitcointalk.org turned out to be
unreachable from this research environment, which raised the real possibility
that claim was written without ever being tested. A person fetched Finney's
actual post text directly from bitcointalk.org and supplied it, twice
independently (both copies byte-identical), plus the raw page HTML.

The first retest - 16 paragraphs split on blank lines, documented flip rule
and its reverse, 4 line-ending conventions, every paragraph-subset, 524,288
candidates total - produced 0 match against
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` (Block 77 Stage One's real, solved,
already-swept address). The raw page HTML resolved why: the live source shows
`...I'm comfortable with my legacy.<br />[edited slightly]</div>` - the
author's own trailing note is attached to the last paragraph by a single
`<br />`, distinct from the `<br /><br />` used between every other paragraph
pair. Every rendered-text copy taken so far (both independent copy-pastes)
had this note visible but it had always been discarded as an editorial aside
rather than kept as literal trailing content.

Restoring it - the 16th paragraph plus `\n[edited slightly]`, all 16
paragraphs joined by `\n\n`, the certified case-flip rule applied to
paragraphs 2, 3, 4, and 6 (the ones starting outside `ITASM`) - reproduces
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` exactly, at BIP44 index 0. Verified twice
independently: once through `tools/oracle.py`'s derivation path, once by
calling `hashlib.md5` and `bip_utils` directly with no shared code.

| Hypothesis | Candidates | Result |
|---|---|---|
| Every paragraph-subset (2^16) x documented flip direction x 4 line-ending conventions, trailing note excluded | 262,144 | 0 match |
| Every paragraph-subset (2^16) x reversed flip direction x 4 line-ending conventions, trailing note excluded | 262,144 | 0 match |
| A second, independent copy-paste of the same post: byte-identical to the first (confirmed by diff) | 1 comparison | identical |
| Block-29-style single-word correction ("voice" to "vOIce") at either occurrence or both, raw and case-flipped, 4 line-ending conventions, trailing note excluded | 24 | 0 match |
| Documented flip rule (paragraphs 2, 3, 4, 6), `\n\n` join, trailing note `\n[edited slightly]` restored on the 16th paragraph, exactly as the raw page HTML renders it | 1 | **MATCH**, index 0, verified independently twice |

The lesson this confirms for Real Big Block: a rendered-text copy-paste can
silently drop or misjudge trailing content that isn't a clean new paragraph
(an author's note, a correction, anything attached by a single line break
rather than a full paragraph gap). Every Real Big Block candidate tested in
this file so far was built the same way the failed Finney attempts were -
cleaned paragraphs only - and should be re-examined against the "Second"
chapter's own raw page source once available. See `analysis/leads.md` for the
lead this opens, now the top priority.

## Real Big Block (0.777 BTC)

The MD5-to-BIP39-to-BIP44 transform and the case-flip rule are both certified
(see README, "Certified against", and the section above). What is not
established is exactly which paragraphs of the "Second" chapter the author
modified on 2019-07-30 and the precise text she copied - and, per the Stage
One reproduction above, whether the candidates tested below have all made the
same mistake the Finney-post attempts made before it was fixed: reading a
cleaned, paragraph-only copy of the page instead of one that preserves
whatever the raw source actually attaches (an author's note, a correction,
anything joined by less than a full paragraph gap). Every row below tests a
specific hypothesis about paragraph selection and text, against both the
current escrow (`14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W`) and its superseded
predecessor (`1EFojcAo2vbhRGCGCa7q8Wwvzss28mhQYC`); none of them have yet been
re-checked against the chapter's own raw page HTML.

| Hypothesis family | Candidates | Result |
|---|---|---|
| Chapter unmodified, every plausible serialization (line-break style, encoding) | approximately 150,000 | 0 match |
| Certified case-flip rule applied to the 3 planted paragraph groups plus the Finney quote, 16 combinations, both letter-position modes | approximately 200,000 | 0 match |
| Every subset of the 17 candidate paragraphs (2^17), 18 serialization variants | 2,360,000 | 0 match |
| Paragraphs selected by a name or word ("Satoshi", "Aoi Nakamoto", "Hal Finney", "Grycoin", and 7 more), by first letter or first character | approximately 10,000 | 0 match |
| Every paragraph starting with F or W (and F, W, H) | approximately 1,000 | 0 match |
| The certified groups plus one arbitrary extra paragraph | 13,000 | 0 match |
| The certified groups plus two arbitrary extra paragraphs | approximately 600,000 | 0 match |
| The single-word planted correction from block 29 ("voice" to "vOIce"), alone and combined with the groups | 6,000 | 0 match |
| Block-29-style link suffixes appended to the text | 8,000 | 0 match |
| Chapter subsections read alone | 3,000 | 0 match |
| Page-level prefixes (duplicated title, author byline) | 2,000 | 0 match |
| A simulated Chromium browser copy (selection/innerText rendering rules) | 1,000 | 0 match |
| Alternate text encodings (Latin-1, UTF-16, cp1252, NBSP normalization) | 3,000 | 0 match |
| Simulated-browser-copy base combined with the name/word selectors, then with all 2^17 paragraph subsets | approximately 800,000 | 0 match |
| A single invisible character (BOM, zero-width space, tab, and 6 more) inserted at the start or end | 5,000 | 0 match |
| Paragraphs selected by the letters of "Satoshi Nakamoto" specifically (a refinement of the name-selector row above, after finding the Finney post has a paragraph starting with M) | 60 | 0 match |
| Last-letter-only or first-letter-only variants of the case-flip rule, on the certified groups | 456 texts (2,736 address checks across derivation indices) | 0 match |
| All of the above serialization families repeated under CRLF line endings | 2,448 texts (14,688 address checks) | 0 match |
| 1 to 3 single-letter case toggles across all sign positions, and 1 to 2 across all paragraph boundaries | 1,450,000 | 0 match |
| Every single-character edit (insert, delete, replace, case toggle) at every position, across 40 base texts (5 paragraph-set choices x 2 NBSP conventions x 2 line-ending conventions x 2 separator conventions) | 266,038,400 | 0 match |
| Whole-chapter and whole-section candidates from a fresh 2026 screen read of the live page (both sections, headers included and excluded, paragraphs joined with one and two line breaks, raw and with the certified case-flip rule) | 24 | 0 match |
| Whole-chapter candidates from a direct browser copy-paste of the live page, preserving the 2 real non-breaking spaces confirmed present in the chapter text at their exact positions, both left as NBSP and normalized to a regular space or deleted | 7 | 0 match |
| Whole-chapter and whole-section candidates (both sections, headers in/out, raw and case-flipped), paragraphs joined by all 4 combinations of `\n` vs `\r\n` and single vs double, and checked against derivation indices 0 to 19 instead of 0 to 5 | 48 | 0 match |
| Every subset of the chapter's 6 natural subsections (Second Coming, Running, Reverse Turing Test, Abstract, Purpose of Grycoin, Bitcoin With Two Changes), CRLF-CRLF and LF-LF, raw and case-flipped | 252 | 0 match |
| Every prefix and every suffix of the full chapter and the no-headers chapter, all lengths, CRLF-CRLF and LF-LF, raw and case-flipped | 1,920 | 0 match |
| Every single paragraph alone; dialogue-only and narration-only extractions; the short "truth or lie" riddle exchange alone | 128 | 0 match |
| Leading/trailing separator variants (none, leading, trailing, both) on the 2 strongest bases; a naive straight-to-curly quote conversion of the same bases | 40 | 0 match |
| A targeted single-character-edit sweep (delete, case toggle, whitespace insert/replace among space/NBSP/tab/CR/LF, straight/curly quote toggle) at every position, across 8 CRLF-CRLF-joined base texts | 772,720 | 0 match, completed 2026-08-17 |
| Quizchain Block 29's own draft text (identified as the source of the chapter's duplicate opening excerpt), raw and with its own confirmed "voice" to "vOIce" correction, tested directly against Real Big Block; the identical sentence inside the real chapter, with the same correction applied alone and combined with the certified case-flip rule, under `\r\n\r\n` | 17 | 0 match |
| Fixing 2 genuine typos in the chapter's own text ("Paloecene" to "Paleocene", "marktet" to "market"), alone and combined, on 4 base texts, raw and case-flipped, under `\r\n\r\n` | 24 | 0 match |
| Bounded 2-slot edit sweep: every pair of inter-paragraph line-ending gaps (4 states each: `\r\n\r\n`, `\r\n`, `\n\n`, `\n`) and the 2 known real NBSP positions (3 states each: NBSP, space, deleted), both slots deviating from the `\r\n\r\n`/NBSP baseline simultaneously, across 4 base texts | 163,698 | 0 match, completed 2026-08-17 |
| Block-29-style single-word corrections applied to "Grycoin"/"grycoin"/"grycoins" (the chapter's most-repeated invented term, whose letters the text itself says were deliberately chosen), 3 transform styles, on 2 base texts | 18 | 0 match |

Witness status: every row above used the oracle certified against the author's
own self-contained MD5-to-address calibration vector (see README, "Certified
against"), which does not depend on the case-flip rule or on Finney's post
text. The single-character-edit row additionally planted 3 synthetic witnesses
per base text (head, middle, tail) and recovered all of them on all 40 bases.
An earlier version of this line also claimed that run "recovered the real
Stage One text and address... when run as a 41st base"; that claim is
withdrawn as of 2026-08-17, since it is directly contradicted by the
524,288-candidate reproduction attempt in the section above, which found 0
match under every plausible reading of the rule. Dates: all rows 2026-08-15
unless marked otherwise.

Cumulative for Real Big Block: approximately 273 million candidates tested, 0
match. The 2 single-character-edit sweeps (the original 40-base LF sweep and
the 2026-08-17 8-base CRLF-CRLF sweep) account for the large majority of this
total and are the only rows certified as complete sweeps of their stated space
(every base, every single edit); every other row is a targeted, not exhaustive,
test of one specific hypothesis about which paragraphs were modified.

## Quizchain2 Block 76 (0.077 BTC)

The chain a community player found in 2019 (`solution = "format"`,
`TOMI = "before TOMI"`) satisfies both of the author's published MD5-prefix
hints, but no standard BIP44/49/84 derivation, derivation path, or passphrase
variant of it produces the escrow address. Two later calibration checks (blocks
73 and 74, both already solved and swept, not part of the live prize) confirm
the derivation code itself is correct, and a later cross-check on 2019-07-29
comment timing suggests the "format" chain was itself a false positive found by
searching for strings that pass the 2 published prefixes, rather than the
author's real answer, since the author never corrected the block after seeing it
posted publicly (see README).

Standard-derivation sweep on the `format`/`before TOMI` chain:

| Hypothesis family | Candidates | Result |
|---|---|---|
| BIP44, BIP49, BIP84, accounts 0 to 4, external and internal chains, index 0 to 199 (BIP44 external: 0 to 1999) | standard derivation space | 0 match |
| Non-standard derivation paths (Coleman-style m/0'/0/i, m/0/i, m/0', root key) | small, enumerated | 0 match |
| Passphrase variants ("TOMI", "format", "before TOMI", bracket and whitespace forms) | small, enumerated | 0 match |
| Alternate entropy functions (SHA-256 as a 24-word mnemonic, SHA-1, RIPEMD-160, truncated SHA-512, double MD5) | small, enumerated | 0 match |
| Off-by-one word at BIP39 import (12 positions x 2,047 alternate words each) | 24,564 | 0 match |
| Word order reversed | 1 | 0 match |

Word-transform "salves" on the question "change to" / "from change to" (each
family's candidate solution strings tested through the same 2 MD5-prefix filters
before any derivation; only pairs passing both filters were derivation-tested):

| Salve | Candidate solutions | Passed prefix 1d | Passed both filters (derivation-tested) |
|---|---|---|---|
| Single-letter edits, anagrams, Atbash/ROT/foldover, translations of "change" | 7,730 | 32 | 3,506 TOMI pairs, 0 match |
| WordNet synsets and hyper/hyponyms of change/alter | 20,199 | 74 | 8,806 TOMI pairs, 0 match |
| Wikipedia article titles containing "change" | 14,666 | 44 | 4,949 TOMI pairs, 0 match |
| Sentences from Satoshi/Hal Finney bitcointalk posts and emails containing "change to" | 46 | 0 | n/a |
| Sentences from bitcointalk posts numbered 60 to 94 (2 orderings) | 1,992 | 11 (noise) | n/a |
| Strings built from the number 76 (years, technical constants, ordinals) | 3,779 | 23 (noise) | n/a |
| Encodings of "change" (hex, base64, NATO alphabet, Morse, keyboard shift) | approximately 130 | 1 (noise) | n/a |
| "changeto" (no space) combined with TOMI variants | 1 | 1 | 1,701 TOMI pairs, 0 match |
| Every address and txid from the author's 158 other funding transactions | approximately 1,500 | 4 (case noise) | n/a |
| Renaming candidates ("wealth", "legacy", and similar) | 45 | 0 | n/a |
| An Easter/resurrection word family, echoing the same block number in round 1 | 2,752 | 17 (noise) | 5,857 TOMI pairs, 0 match |
| Halving-related terms | 45 | 1 (noise) | n/a |
| Grycoin/burn-address/second-layer terms from the chapter | 60 | 0 | n/a |
| Literal strings and typos from the block's own post | 45 | 0 | n/a |

A separate "post-number-as-index" method, confirmed on 3 other blocks in the
series (numbers 56, 57 and 58 each index a specific post or tweet by Satoshi or
Hal Finney, by position), does not carry over to block 76: post number 76 in
every corpus and ordering tried (Satoshi's bitcointalk posts newest-first and
chronological, Hal Finney's posts, Hal Finney's tweets) contains neither "change"
nor "from".

A large dictionary-times-corpus sweep tested every 1-to-4-word phrase built from
the author's own writing (Reddit posts, comments, and Wattpad chapters) as a
candidate TOMI value, against a dictionary-and-WordNet-derived candidate solution
list: 189,565 candidate solutions passing the first filter, times 656,845 to
1,250,000 candidate TOMI phrases depending on the pass, for a combined total of
approximately 3.2x10^11 MD5 computations and approximately 78 million full
address derivations on the pairs that passed both filters. 0 match. The
derivation code was re-confirmed correct on both calibration blocks (73 and 74)
at the head, middle and tail of this run.

Cumulative for Block 76: approximately 78 million address derivations from the
scripted dictionary sweep, plus approximately 53,000 smaller thematic candidates
across the 14 salves above, plus the full standard-derivation sweep on the one
chain found by search. 0 match anywhere. This is reported as a targeted, not
exhaustive, negative: the true solution may use vocabulary outside the corpora
swept (the author's own writing and 2 general-purpose dictionaries), and the
block may simply be misconfigured (see README).

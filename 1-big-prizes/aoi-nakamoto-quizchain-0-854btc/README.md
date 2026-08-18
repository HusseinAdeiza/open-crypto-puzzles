# Aoi Nakamoto Quizchain (0.854 BTC, [OPEN])

AoiNakamoto, a pseudonymous Reddit user, ran a series of roughly 90 self-funded
Bitcoin puzzle blocks from April to October 2019 on r/bitcoinpuzzles and her own
r/Grycoin, each with its own escrow address, question, and prize. She stopped
posting in October 2019 without ever reclaiming her own puzzle funds. Every
block was solved and swept by readers except the last two she published: the
second and final stage of "Real Big Block" (0.777 BTC) and "Quizchain2 Block
76" (0.077 BTC), both still funded seven years later. The MD5-to-BIP39
derivation mechanism and the case-flip rule are both now independently
re-confirmed exactly (2026-08-17), by reproducing the solved sibling lot Block
77 Stage One's real address from Hal Finney's actual post text fetched
directly from bitcointalk.org; what closed the reproduction was including a
trailing author's note ("[edited slightly]") attached to the last paragraph,
exactly as the raw page source renders it, rather than treating it as
page furniture to strip out. Applying that same fidelity check to the
"Second" Wattpad chapter itself (2026-08-17) found that the working
transcription had silently covered only the first 5 of the chapter's 12
Wattpad pages; the complete, byte-checked 272-paragraph chapter is now
available for the first time, and an exhaustive sweep of every contiguous
paragraph range, every character-level edit, and a first batch of
non-contiguous paragraph selections all found 0 match. A newer discovery
(2026-08-18): "Second" is only 1 of 33 chapters in a single Wattpad story,
and one of the others, "TOMI," directly explains a display/hash mismatch bug
on a post covering 3 blocks - a strong new lead for Block 76 specifically,
not yet resolved. What remains is reading the rest of that story, plus
non-contiguous paragraph selection or a character-level edit on top of a
contiguous range for Real Big Block.

## At a glance

| | |
|---|---|
| Author | AoiNakamoto (pseudonymous), [r/Grycoin](https://www.reddit.com/r/Grycoin/) |
| Published | 2019-04 to 2019-07-30, rolling releases on r/bitcoinpuzzles and r/Grycoin; the two open lots funded 2019-07-22 and 2019-07-30 |
| Prize | 0.777 BTC + 0.077 BTC = 0.854 BTC (about $53,802 at BTC = $63,000, 2026-08-16) |
| Chain | bitcoin |
| Escrow | `14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W` (Real Big Block, [explorer](https://mempool.space/address/14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W)) and `13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd` (Block 76, [explorer](https://mempool.space/address/13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd)) |
| Last on-chain check | 2026-08-16: both funded and unspent (0.777 BTC and 0.077 BTC) |
| Status | OPEN |
| Puzzle type | bip39-seed, word-selection |
| Target format | source text (candidate answer), MD5 to 128-bit entropy, BIP39 mnemonic, BIP44 `m/44'/0'/0'/0/i` for i = 0 to 19, P2PKH address |
| Certified oracle | yes: `tools/oracle.py --selftest` (certified against the author's own published entropy-to-WIF vector; see "Certified against" for what is and is not covered) |
| What remains | Real Big Block: the exact source text the author hashed on 2019-07-30 (the transform and case-flip rule are both confirmed; the chapter is now complete and byte-checked for the first time, 272 paragraphs, and every contiguous-paragraph-range selection under the confirmed separator has been exhaustively ruled out, 0 match). Block 76: a short answer to a published word riddle, since no derivation of the one candidate chain found by search reaches the address |
| Series | this folder covers the 2 open lots of the approximately 90-block Quizchain series; the rest were solved by other readers in 2019 |

## The puzzle as published

AoiNakamoto's last two blocks, in order:

Real Big Block stage 1, 2019-07-07
([reddit.com/r/Grycoin/comments/ca6jxv](https://www.reddit.com/r/Grycoin/comments/ca6jxv/77_mbtc_quizchain2_block_77_stage_one/)):
"I do disclose that this one has no TOMI field, but that is all. You are on your
own completely." Its question links to Hal Finney's "Bitcoin and me" post on
bitcointalk (topic 155054). She adds: "I will publish the complete solution as
the Second stage of this block. This solution will in turn be the question for
the Second stage, which will have the final 777 mbtc prize." This stage's
escrow, `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN`, was solved and swept on
2019-08-03; it is not part of the live prize and is used in this folder only to
certify the case-flip rule (see "What is understood").

Quizchain2 Block 76, 2019-07-22
([reddit.com/r/Grycoin/comments/cgcv9i](https://www.reddit.com/r/Grycoin/comments/cgcv9i/77_mbtc_quizchain2_block_76/)):
"Question: change to", "Format: [solution] TOMI [TOMI]", "First three digits of
MD5 hash are f8e". A later update adds "First two digits of solution only are
1d", and a hint changes the question to "from change to". She adds: "I will
shut down soon now [...] so I will not be available for hints or questions."

Real Big Block stage 2, published as a chapter titled "Second" on the author's
own Wattpad account
([wattpad.com/720888559-second](https://www.wattpad.com/720888559-second)). In
the "Real Big Block Discussion" thread
([reddit.com/r/Grycoin/comments/chn8un](https://www.reddit.com/r/Grycoin/comments/chn8un/real_big_block_discussion/)),
she writes, 2019-07-25: "When I posted the real big block at the Wattpad site,
I added extra line breaks between paragraphs. This information is needed to
solve the block." On 2019-07-31, after moving the funds to the current escrow:
"I took back the prize for a moment and sent it again to a new address, hashing
with a slightly different solution [...] It has multiple paragraphs and two
line breaks between each of them."

![Quizchain series structure: both rounds solved and claimed except the 2 open gates](images/02-structure-blocks.svg)
*Figure 2. The Quizchain series, colored by claim status (source: data/blocks-structure.json, script tools/fig_blocks.py), 2026-08-16.*

## What is understood

### Mechanism

Every block in the series follows the same transform: MD5 the exact bytes of a
source text to get 128 bits of entropy, generate a BIP39 mnemonic from that
entropy, derive BIP44 path `m/44'/0'/0'/0/i` (the author confirms taking a low
index, typically the first), and compare the resulting P2PKH address to the
block's escrow. Block 76 additionally uses a `[solution] TOMI [tomi]` format,
where TOMI (Japanese for "wealth") is a second, separately-hinted field: an
anti-brute-force device, since guessing the solution alone is not enough to
reach the hash.

![Source text to P2PKH address, five stages linked by MD5, BIP39 and BIP44](images/01-pipeline-derivation.svg)
*Figure 1. The MD5-to-address derivation pipeline (source: data/pipeline-stages.json, script tools/fig_pipeline.py), 2026-08-16.*

For Real Big Block, the source text is the "Second" chapter (confirmed by the
Stage 1 post's own words, see below), with the case-flip rule applied to some
of its paragraphs, not the chapter's raw text. This rule is now genuinely
re-confirmed, independently, on the solved sibling lot Block 77 Stage One: of
that post's 16 paragraphs, the 4 whose first letter is not I, T, A, S, or M
get their first letter lowercased and last letter uppercased, joined with a
blank line, **with the author's own trailing edit note ("[edited slightly]")
kept attached to the last paragraph by a single line break, exactly as the
live page source renders it** - this reproduces
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` exactly (verified 2026-08-17 against Hal
Finney's real post text, fetched directly from bitcointalk.org; see
"Certified against"). An earlier version of this file wrongly concluded the
rule itself was unverified, after 524,288 candidates that all excluded this
trailing note came back with 0 match; the rule was right all along; what was
missing was text fidelity to the page's exact rendering, not the mechanism.

That same lesson - keep exactly what the page renders, including anything
that looks like page furniture or an editorial aside, rather than stripping
it - is now the leading hypothesis for why the "Second" chapter hasn't
matched either: every candidate tested so far in `analysis/tested.md` was
built from a cleaned, paragraph-only reading of the chapter, the same kind of
reading that failed on Finney's post until the trailing note was restored.
The "Second" chapter's own raw page source has not yet been fetched and
checked for anything analogous (an author's note, a strikethrough correction,
trailing punctuation attached across what looks like a paragraph break). The
Wattpad API confirms the chapter's `modifyDate` as 2019-07-23T23:12:04Z, 7
days before the current escrow was funded, so the text available today
predates the funding and is very likely the version that was hashed; see
"Open leads" for the concrete next step.

For Block 76, a community player found, in 2019, that `solution = "format"`,
`tomi = "before TOMI"` satisfies both published MD5-prefix hints (`1d` and
`f8e`); the free filter for checking this yourself is
`tools/oracle.py --block76-filter`. No standard derivation of this pair reaches
the escrow address, and the author never corrected the block after the pair was
posted publicly, which argues this chain is a coincidental false positive
rather than her real answer (see "What has been tested").

### Derivation and oracle

```
python3 tools/oracle.py --selftest
python3 tools/oracle.py "<candidate text>"
python3 tools/oracle.py --stdin
python3 tools/oracle.py --block76-filter "<solution>" "<tomi>"
python3 tools/oracle.py --flip-case "<one paragraph>"
```

Given a candidate text, the oracle MD5s its UTF-8 bytes, derives BIP44 indices 0
through 19, and compares each resulting address against both open escrows.
`--block76-filter` checks the 2 free MD5-prefix hints before any derivation.
`--flip-case` applies the confirmed Stage One rule to one paragraph you supply.
This script ships no source text of its own: Real Big Block's source (a Wattpad
chapter) and the Stage One certification text (a bitcointalk post by Hal
Finney) are both excluded, the first as bulk chapter content and the second as
third-party historical material neither the puzzle's author nor this repository
holds the rights to. Supply your own candidate text to test it.

### Certified against

`tools/oracle.py --selftest` reproduces the author's own published calibration
vector, given in the round-1 corpus: entropy `2941774a2abec9f30c7d6777d1d53d91`,
at BIP44 index 1 ("my 2nd private key"), derives WIF
`L5Z66qPmUkTAsWQywjRNHDxHrX6J1X1SQedp6V8QsbaXR7rGd6ex` exactly, and that WIF
appears at no other index. This certifies the MD5-to-address transform itself,
without needing any third-party text. The selftest also checks the
`--flip-case` helper against a synthetic (non-puzzle) example sentence, and the
`--block76-filter` helper against the community-found `format` / `before TOMI`
pair.

This does not, by itself, reproduce Block 77 Stage One end to end, since that
needs Hal Finney's bitcointalk post text, which this repository does not ship
(third-party historical content).

**Update, 2026-08-17**: an earlier version of this file claimed the case-flip
rule reproduces `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` exactly, without visible
evidence of that having been genuinely tested (bitcointalk.org turned out to
be unreachable from this research environment). Retesting it against Finney's
real post text, fetched directly by a person from bitcointalk.org, initially
also failed: 524,288 combinations of paragraph subset, flip direction, and
line-ending convention, all 0 match. The reproduction succeeded once the raw
page HTML was checked directly: the live source shows the author's trailing
note, `[edited slightly]`, attached to the last paragraph by a single line
break (`<br />`, distinct from the `<br /><br />` used between paragraphs),
which every prior attempt (including the original, now-corrected claim) had
stripped out as page furniture. Keeping it in - last paragraph plus
`\n[edited slightly]`, joined with the other 15 paragraphs by a blank line,
case-flip applied to paragraphs 2, 3, 4, and 6 - reproduces
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` at BIP44 index 0 exactly. Verified twice
independently: once through `tools/oracle.py`'s own derivation path, once
by calling `hashlib` and `bip_utils` directly with no shared code.

Reproduced 2026-08-16 (transform) and 2026-08-17 (case-flip rule, via Block 77
Stage One).

### Established facts

1. Both escrows are funded and unspent as of 2026-08-16: `14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W`
   holds 0.777 BTC (funded 2019-07-30, block 587833) and
   `13Cv6SXUnzGDT8JHqzzJ8xMPtsSdhJA4wd` holds 0.077 BTC (funded 2019-07-22,
   block 586468), checked via [mempool.space](https://mempool.space).
2. Across the approximately 90 blocks of the series, these are the only 2 still
   funded: an exhaustive sweep of all 159 funding transactions cited in the
   author's 202 Reddit posts found 0 unreadable transactions and exactly these
   2 unspent above 100,000 sats.
3. The MD5-to-BIP39-to-BIP44 transform is confirmed exactly against the
   author's own published calibration vector (above).
4. The case-flip rule is confirmed exactly against the solved sibling lot
   Block 77 Stage One, reproducing its escrow address byte for byte, verified
   2026-08-17 against Hal Finney's real post text fetched directly from
   bitcointalk.org (see "Certified against"). An initial retest that excluded
   the post's trailing author's note failed across 524,288 combinations;
   including that note, exactly as the raw page source attaches it,
   succeeded.
5. The Real Big Block chapter's Wattpad `modifyDate` (2019-07-23) predates the
   current escrow's funding (2019-07-30) by 7 days, and the chapter has not
   been modified since, confirmed via the Wattpad API.
6. No archived capture of the "Second" Wattpad chapter from 2019 exists on the
   Wayback Machine, archive.today, or Common Crawl, checked across 8 URL forms
   and 5 time-windowed collections; a positive control query on each service
   confirms the services themselves were responding, so these are true absences
   in the archive, not failed lookups.
7. The chain `MD5("format") ` starts with `1d` and `MD5("format TOMI before TOMI")`
   starts with `f8e`, matching both prefixes the author published for Block 76;
   neither of 2 other independently solved calibration blocks (73 and 74) shows
   any sign this chain is the author's real answer.

## What has been tested

Full ledger in [analysis/tested.md](analysis/tested.md). Summary:

| Hypothesis | Space | Method | Result | Witness | Date |
|---|---|---|---|---|---|
| RBB: chapter unmodified or with the certified rule on a small set of candidate paragraph groups | approximately 350,000 | MD5 to BIP39 to address compare | 0 match | yes: oracle certified against Stage One | 2026-08-15 |
| RBB: every subset of 17 candidate paragraphs, 18 serializations | 2,360,000 | same | 0 match | yes | 2026-08-15 |
| RBB: every single-character edit across 40 base texts | 266,038,400 | same | 0 match | yes: 3 planted witnesses per base plus the real Stage One text, all recovered | 2026-08-15 |
| RBB: whole-chapter and whole-section candidates from a fresh 2026 screen read of the live page, headers in/out, 1 and 2 line breaks, raw and case-flipped | 24 | same | 0 match | yes | 2026-08-17 |
| RBB: whole-chapter candidates from a direct browser copy-paste, preserving the 2 real NBSP characters confirmed in the chapter at their exact positions | 7 | same | 0 match | yes | 2026-08-17 |
| RBB: whole-chapter and whole-section candidates joined with the author's own confirmed exact separator (`\r\n\r\n`, "13 10 13 10") and 3 other line-ending combinations, checked against derivation indices 0 to 19 | 48 | same | 0 match | yes | 2026-08-17 |
| RBB: every subset of the chapter's 6 natural subsections, and every prefix/suffix of the chapter, under `\r\n\r\n`/`\n\n` | 2,172 | same | 0 match | yes | 2026-08-17 |
| RBB: every single paragraph alone; dialogue-only, narration-only, and riddle-exchange extractions; leading/trailing separators; a naive curly-quote conversion | 168 | same | 0 match | yes | 2026-08-17 |
| RBB: targeted single-character-edit sweep (delete, case toggle, whitespace family, quote style) at every position across 8 `\r\n\r\n`-joined bases | 772,720 | same | 0 match | yes | 2026-08-17 |
| RBB: Quizchain Block 29's own draft text (source of the chapter's duplicate opening excerpt) and its confirmed "voice" to "vOIce" correction, direct and applied to the identical sentence in the real chapter | 17 | same | 0 match | yes | 2026-08-17 |
| RBB: bounded 2-slot edit sweep, every pair of line-ending gaps (4 states each) and both known NBSP positions (3 states each) deviating from baseline at once, across 4 base texts | 163,698 | same | 0 match | yes | 2026-08-17 |
| RBB: Block-29-style corrections on "Grycoin"/"grycoin"/"grycoins", the chapter's most-repeated invented term | 18 | same | 0 match | yes | 2026-08-17 |
| RBB: name/word paragraph selectors, browser-copy simulation, invisible characters, alternate encodings | approximately 1,830,000 | same | 0 match | yes | 2026-08-15 |
| RBB: complete 272-paragraph chapter recovered (pages 6-12 had never been transcribed before), diffed page by page against raw source, 5 byte-level fixes applied; every contiguous paragraph range of the complete chapter, flip and no-flip, under the confirmed `\r\n\r\n` separator | 74,256 | same | 0 match | yes | 2026-08-17 |
| RBB: same, every contiguous range under all 4 line-ending conventions, plus the chapter's title paragraph as an optional leading paragraph | 299,208 | same | 0 match | yes | 2026-08-18 |
| RBB: non-contiguous ITASM-initial paragraph selection (kept vs dropped, with/without case-flip on the kept set) on the whole chapter, each top-level section, and 26 finer subsections | 616 | same | 0 match | yes | 2026-08-18 |
| RBB: single-character-edit sweep (delete, case toggle, whitespace family, quote style) at every position, re-run against the complete, corrected chapter, 8 base texts (whole chapter and each of the 3 top-level sections, raw and case-flipped) | 1,390,004 | same | 0 match | yes | 2026-08-18 |
| RBB: bounded 2-character-edit sweep (line-ending gap pairs and the 2 confirmed NBSP positions), re-run against the complete, corrected chapter, 4 base texts | 443,807 | same | 0 match | yes | 2026-08-18 |
| Stage One mechanism check: every paragraph-subset of Hal Finney's real post (2^16) x both flip directions x 4 line-ending conventions, trailing note excluded, against Stage One's own solved address, not RBB | 524,288 | MD5 to BIP39 to address compare | 0 match | yes | 2026-08-17 |
| Stage One mechanism check: a second, independent copy-paste of the same post (byte-identical to the first) with a "voice" to "vOIce" correction, raw and case-flipped, 4 line-ending conventions | 24 | same | 0 match | yes | 2026-08-17 |
| Stage One mechanism check: documented case-flip rule with the raw HTML's trailing author's note restored on the last paragraph, exactly as rendered | 1 | same | **MATCH**, confirms the case-flip rule | yes, verified twice independently | 2026-08-17 |
| Block 76: standard BIP44/49/84 derivations, paths, passphrases on the one chain found by search | standard space plus 24,564 off-by-one variants | MD5 to BIP39 to address compare | 0 match | yes: calibrated on blocks 73 and 74 | 2026-08-15 |
| Block 76: word-transform "salves" on "change to" / "from change to" | approximately 53,000 candidate solutions | MD5-prefix filter, then derivation on survivors | 0 match | yes | 2026-08-15 |
| Block 76: scripted dictionary-times-corpus sweep | approximately 3.2x10^11 MD5, approximately 78,000,000 derivations | MD5-prefix filter, then derivation on survivors | 0 match | yes: calibrated on blocks 73 and 74 | 2026-08-15 |

Cumulative: approximately 273 million candidates tested against Real Big
Block's old, incomplete (pages-1-5-only) transcription, plus 2,208,907 against
the complete, corrected 272-paragraph chapter recovered 2026-08-17 (0 match
anywhere), and approximately 78 million derivations plus approximately 78,000 smaller
candidates tested against Block 76, all negative. Full scope notes, including
which rows are complete sweeps versus targeted tests, are in
`analysis/tested.md`.

## Open leads, ranked

1. **Read the rest of the 33-chapter Wattpad story "Second" belongs to**
   (minutes per chapter, needs a person; top priority, 2026-08-18). Every
   candidate tested against either escrow so far, including the exhaustive
   sweeps against the "complete" chapter, used only the single Wattpad part
   titled "Second." That part's own page metadata reveals it is 1 of 33 parts
   in one Wattpad story, spanning titles from "Welcome to the Quizchain"
   through "Starting Up." 4 parts have been read: "Second," "TOMI,"
   "Utter Disaster Three Block Series," and "Complete Quizchain" (a full
   retrospective log of the whole series' questions/formats/answers). The
   TOMI-rename hypothesis first raised by the "TOMI" chapter is now **ruled
   out**: "Complete Quizchain" pins the display/hash mismatch bug to blocks
   48-50 specifically ("Changed name of BFUB field to TOMI and hashed with
   old name"), long before block 76, which consistently uses "TOMI"
   throughout. A stronger pattern remains open, though: "Complete Quizchain"
   repeatedly shows this series' solutions and TOMI values are literal
   references to the story's own chapter titles (Round 1's own, different
   Block 76 had solution "Easter," TOMI "Second Life"; Block 53's solution
   was literally "Satoshi's Stash"; Round 2's Block 2 was solved entirely
   from the "Quizchain as a Password Manager" chapter). "Complete Quizchain"
   itself stops early in Round 2 (3 blocks in), before reaching Quizchain2's
   Block 76 - a later, higher-ID chapter, "Complete Second Round of the
   Quizchain" (742662804), is very likely the equivalent retrospective for
   Round 2 and is now the single most promising unread chapter, not yet
   fetched. A first round of literal-reading tests on Block 76 (solution
   "BFUB" alone; "format" against all 33 chapter titles as TOMI; the
   literal edited question text "from change to" as the solution) found 0
   match. Confirmed by reading "Complete Second Round of the Quizchain" and
   finding Quizchain2's Block 76 entry, or any other part directly stating a
   fuller Real Big Block source; killed only by reading through the
   remaining parts with nothing relevant found (a bound on effort, not a
   logical exhaustion). Full list of part titles and detail:
   `clues/author-posts.md`, `analysis/leads.md`.
2. **Non-contiguous paragraph selection from the now-complete chapter**
   (minutes per hypothesis once defined). Fetching the chapter's raw page
   source and checking it for trailing content (formerly this lead) is done:
   it found the working transcription had silently covered only the first 5
   of the chapter's 12 Wattpad pages, missing 148 paragraphs (the rest of the
   Grycoin whitepaper and the entire "Second Identity" section) entirely, plus
   5 smaller byte-level errors on the pages it did cover. With the complete,
   byte-checked 272-paragraph chapter now available, every *contiguous*
   paragraph range (under all 4 line-ending conventions, flip and no-flip,
   with and without the chapter's title paragraph, 373,464 candidates), a
   first non-contiguous selection (`ITASM`-initial paragraphs kept or dropped,
   616 candidates), a single-character-edit sweep (8 base texts, 1,390,004
   candidates), and a bounded 2-character-edit sweep (4 base texts, 443,807
   candidates) have all been run against it exhaustively: 0 match anywhere,
   all completed 2026-08-18 (`analysis/tested.md`). This rules out every
   "single contiguous run of paragraphs, optionally edited by up to 2
   characters" hypothesis, plus the one non-contiguous rule tried so far.
   What remains open is any other non-contiguous paragraph selection rule,
   including the original private research's 17-candidate-paragraph
   hypothesis, which has never been re-derived or re-run against the complete
   chapter. Confirmed by a match on any non-contiguous selection; killed by
   exhausting the specific rules worth trying with 0 match (this space is not
   boundable the way contiguous ranges are, so "killed" here means "no more
   promising rules identified," not exhaustion).
3. **Check whether the Real Big Block Discussion thread covers all 27 posts in
   the window** (minutes, needs a person). That thread has now been read in
   full, including its 3 previously-collapsed reply threads (2 contributed
   nothing beyond what's already recorded); it is where the `\r\n\r\n`
   confirmation above came from. Whether it accounts for the full 27 posts and
   comments the author made 2019-07-30 to 2019-08-04, or whether other threads
   or profile comments from that window exist and remain unread, is still
   unconfirmed. Confirmed by another thread surfacing something new; killed by
   confirming this is the complete set.
4. **The chapter's duplicate opening excerpt is identified, confirmed
   irrelevant to the hash on its own, but points at a real, untested
   mechanism** (minutes per word). The live page shows the chapter's opening
   scene twice with different wording each time; the second copy is now
   identified as the author's own draft text for an earlier, unrelated,
   already-solved block ("Quizchain Block 29"), which she posted in full,
   labeled "exactly same as used for hashing." That block's confirmed
   mechanism was a single-word letter-case correction ("voice" to "vOIce"),
   not the paragraph case-flip rule used elsewhere in the series - and note
   this mechanism does not depend on lead 1, since it's a different, directly
   demonstrated transform on a different lot. Both the Block 29 text itself
   and the same correction applied to the identical sentence inside the real
   chapter were tested (0 match, `analysis/tested.md`). Confirmed as a live
   lead by a match on any other distinctive word in the chapter tried the same
   way; killed by exhausting the chapter's distinctive words with no match.
5. **Identify what "76" indexes for Block 76** (minutes per candidate corpus).
   A method confirmed on 3 sibling blocks uses the block number as a position
   index into a specific numbered corpus; every corpus tried so far does not
   contain "change" at position 76. Confirmed by a match in an untried corpus
   (candidates include a fuller archive of Hal Finney's tweets, Satoshi's
   SourceForge posts, or the author's own r/Grycoin posts read as their own
   sequence); killed by exhausting the remaining candidate corpora.
6. **A short, human-reasoned answer to "change to" / "from change to"**
   (minutes per candidate). The author's confirmed style elsewhere in the
   series favors short, punchy wordplay answers over long dictionary phrases; a
   free filter (`tools/oracle.py --block76-filter`) checks any candidate in
   under a second before a full derivation. This lead has no exhaustion
   condition; it is a standing invitation, same as any human-reasoned wordplay
   block in the series.

Full notes: [analysis/leads.md](analysis/leads.md).

## Files in this folder

| Path | What it is |
|---|---|
| `clues/author-posts.md` | short, dated quotes from the author's own Reddit posts, with links |
| `data/pipeline-stages.json` | the 6-stage label list for the derivation pipeline figure |
| `data/blocks-structure.json` | the series structure and the 2 open gates, for the structure figure |
| `analysis/tested.md` | the complete negatives ledger for both open lots |
| `analysis/leads.md` | full notes behind the 7 ranked leads |
| `images/01-pipeline-derivation.svg` | the MD5-to-address derivation pipeline diagram |
| `images/02-structure-blocks.svg` | the Quizchain series structure, colored by claim status |
| `tools/oracle.py` | candidate checker, certified against the author's own vector; includes the Block 76 prefix filter and the Stage One case-flip helper |
| `tools/fig_pipeline.py` | generates images/01-pipeline-derivation.svg from data/pipeline-stages.json |
| `tools/fig_blocks.py` | generates images/02-structure-blocks.svg from data/blocks-structure.json |

## Sources

- Real Big Block stage 1, Reddit, 2019-07-07: https://www.reddit.com/r/Grycoin/comments/ca6jxv/77_mbtc_quizchain2_block_77_stage_one/
- Quizchain2 Block 76, Reddit, 2019-07-22: https://www.reddit.com/r/Grycoin/comments/cgcv9i/77_mbtc_quizchain2_block_76/
- Real Big Block Discussion, Reddit, 2019-07-25 to 2019-07-31: https://www.reddit.com/r/Grycoin/comments/chn8un/real_big_block_discussion/
- "Second", Wattpad chapter by AoiNakamoto: https://www.wattpad.com/720888559-second
- Real Big Block escrow funding transaction, mempool.space, 2019-07-30: https://mempool.space/tx/a1916e7ed9eac3fcc56a55056328cb09d06925e2694f2e6720de12b228514d1f
- Block 76 escrow funding transaction, mempool.space, 2019-07-22: https://mempool.space/tx/979670f3d1d4134e7989ed6f4a4370362e15c101711c93675790cf0751c8dbd4
- Block 77 Stage One escrow (certification reference, solved and swept 2019-08-03), mempool.space: https://mempool.space/address/19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN
- Hal Finney, "Bitcoin and me", bitcointalk topic 155054 (source text for the Stage One certification reference, not reproduced here): https://bitcointalk.org/index.php?topic=155054.0

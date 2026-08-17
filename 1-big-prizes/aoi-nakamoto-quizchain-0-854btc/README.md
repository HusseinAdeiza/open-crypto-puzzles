# Aoi Nakamoto Quizchain (0.854 BTC, [OPEN])

AoiNakamoto, a pseudonymous Reddit user, ran a series of roughly 90 self-funded
Bitcoin puzzle blocks from April to October 2019 on r/bitcoinpuzzles and her own
r/Grycoin, each with its own escrow address, question, and prize. She stopped
posting in October 2019 without ever reclaiming her own puzzle funds. Every
block was solved and swept by readers except the last two she published: the
second and final stage of "Real Big Block" (0.777 BTC) and "Quizchain2 Block
76" (0.077 BTC), both still funded seven years later. The MD5-to-BIP39
derivation mechanism itself is confirmed exactly, but the case-flip rule this
folder's research previously treated as proven on a solved sibling lot could
not be independently reproduced when tested directly against Hal Finney's real
post text (see "Certified against"), so it is now an open question, not a
settled fact; what remains is both that question and the precise source text
for Real Big Block, plus a short answer to a word riddle for Block 76.

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
| What remains | Real Big Block: the exact source text the author hashed on 2019-07-30, and now also whether the case-flip rule this research assumed is even the right mechanism, since it fails an exhaustive reproduction test against Hal Finney's actual post (see "Certified against"). Block 76: a short answer to a published word riddle, since no derivation of the one candidate chain found by search reaches the address |
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
Stage 1 post's own words, see below); what is not confirmed, despite this
folder's earlier notes stating otherwise, is that a case-flip rule applies to
some of its paragraphs rather than the chapter's raw text. That rule was
described as "proven on the solved sibling lot Block 77 Stage One," but a
direct test against Hal Finney's real post text (obtained and tested
2026-08-17, see "Certified against") could not reproduce
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` under this rule, or under its reverse, in
any of the 524,288 combinations of paragraph subset and line-ending convention
tried. This means the case-flip mechanism is an open hypothesis again, not a
settled one, and everything below that assumed it (the 4-candidate-group
search, the 2^17-paragraph sweep, the case-flipped rows in
`analysis/tested.md`) inherits that same uncertainty. The Wattpad API confirms
the chapter's `modifyDate` as 2019-07-23T23:12:04Z, 7 days before the current
escrow was funded, so the text available today predates the funding and is
very likely the version that was hashed; what is not settled is which exact
byte sequence the author's own tool read from it, since Wattpad's storage
normalizes away the blank lines she describes typing (see "Open leads").

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

**Correction, 2026-08-17**: an earlier version of this file stated "I did this
during research and it reproduces `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN` exactly,
which is the basis for the case-flip rule described above." That claim could
not be reproduced. bitcointalk.org is unreachable from this research
environment (confirmed 2026-08-17: blocked, along with 3 mirror/aggregator
sites tried as alternatives), which means the original claim was very likely
never actually tested against real text, despite being stated as a completed,
witnessed result. When a person supplied the real post text directly
(copy-pasted from bitcointalk.org, checked and re-checked for transcription
errors), `apply_stage_one_rule()` under the documented rule, its reverse, and
all 4 plausible line-ending conventions (524,288 combinations of paragraph
subset and separator in total) produced 0 match against
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN`. This does not prove the case-flip rule is
wrong outright (a transcription difference from whatever the puzzle author
actually hashed in 2019, given Finney's post has its own edit history, remains
a live possibility), but it means the rule's "confirmed" status in this file
was unearned and is now withdrawn pending independent reproduction. See
`analysis/tested.md` and `analysis/leads.md` for the full negative record and
the lead this opens.

Reproduced (transform only) 2026-08-16. Stage One reproduction attempted and
failed 2026-08-17.

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
4. The case-flip rule is **not** confirmed against the solved sibling lot Block
   77 Stage One: a direct test against Hal Finney's real post text failed to
   reproduce that lot's escrow address across 524,288 combinations of
   paragraph subset, flip direction, and line-ending convention (see
   "Certified against" and `analysis/tested.md`). This corrects an earlier,
   uncorroborated claim in this file.
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
| RBB: name/word paragraph selectors, browser-copy simulation, invisible characters, alternate encodings | approximately 1,830,000 | same | 0 match | yes | 2026-08-15 |
| Block 76: standard BIP44/49/84 derivations, paths, passphrases on the one chain found by search | standard space plus 24,564 off-by-one variants | MD5 to BIP39 to address compare | 0 match | yes: calibrated on blocks 73 and 74 | 2026-08-15 |
| Block 76: word-transform "salves" on "change to" / "from change to" | approximately 53,000 candidate solutions | MD5-prefix filter, then derivation on survivors | 0 match | yes | 2026-08-15 |
| Block 76: scripted dictionary-times-corpus sweep | approximately 3.2x10^11 MD5, approximately 78,000,000 derivations | MD5-prefix filter, then derivation on survivors | 0 match | yes: calibrated on blocks 73 and 74 | 2026-08-15 |

Cumulative: approximately 273 million candidates tested against Real Big Block
and approximately 78 million derivations plus approximately 78,000 smaller
candidates tested against Block 76, all negative. Full scope notes, including
which rows are complete sweeps versus targeted tests, are in
`analysis/tested.md`.

## Open leads, ranked

1. **Resolve whether the case-flip rule is real at all** (minutes, if an
   alternate source of Hal Finney's post text is available). This repository
   previously claimed the rule "reproduces `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN`
   exactly," but that could not be reproduced: a person supplied Finney's real
   post text directly (bitcointalk.org is unreachable from this research
   environment), and an exhaustive test - every subset of its 16 paragraphs,
   both flip directions, all 4 line-ending conventions, 524,288 candidates -
   produced 0 match against that address (`analysis/tested.md`). Everything
   below that assumes the case-flip rule inherits this uncertainty. Confirmed
   real by an independent transcription of the post reproducing the address
   under some serialization; killed as this specific mechanism by a second
   independent transcription also failing.
2. **Re-run the paragraph-subset hypotheses under the author's confirmed exact
   separator** (minutes to re-run, more to identify the exact subsets again).
   2 dated, reconciled quotes (not a contradiction, once read carefully)
   confirm `\r\n\r\n` between paragraphs for the current, still-funded address
   specifically ("hit enter twice... 13 10 13 10"), versus `\r\n` for the
   superseded one - independent of whether the case-flip rule itself turns out
   to be right (lead 1). Every whole-chapter, whole-section, subsection-subset,
   prefix/suffix, and single-paragraph candidate has been tested under all 4
   line-ending combinations (0 match), and a single-character-edit sweep on 8
   of the strongest bases completed with 0 match (see `analysis/tested.md`).
   The narrower paragraph-subset hypotheses from the original private research
   (the 17-candidate-paragraph sweep) have not yet been re-run under this
   exact separator, and that candidate list is not itself preserved anywhere
   in this repo. Confirmed by a match once re-run; killed by exhausting those
   subsets under `\r\n\r\n` with 0 match.
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
5. **A bounded 2-character-edit sweep on the strongest base texts** (about an
   hour on a rented GPU). The 1-character sweep on the old `\n\n` bases and a
   second one on the new `\r\n\r\n` bases are both exhaustive and both
   negative; a 2-character sweep restricted to the small set of NBSP and
   line-ending pairs, rather than every position, is a bounded extension on
   top of that. Confirmed by a match in that bounded space; killed by
   exhausting it with none.
6. **Identify what "76" indexes for Block 76** (minutes per candidate corpus).
   A method confirmed on 3 sibling blocks uses the block number as a position
   index into a specific numbered corpus; every corpus tried so far does not
   contain "change" at position 76. Confirmed by a match in an untried corpus
   (candidates include a fuller archive of Hal Finney's tweets, Satoshi's
   SourceForge posts, or the author's own r/Grycoin posts read as their own
   sequence); killed by exhausting the remaining candidate corpora.
7. **A short, human-reasoned answer to "change to" / "from change to"**
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

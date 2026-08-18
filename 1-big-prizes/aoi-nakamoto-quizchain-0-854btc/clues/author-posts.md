# Author posts and quotes

Short, dated excerpts from AoiNakamoto's own Reddit posts, in chronological order.
Full threads are public; only short quotes are reproduced here.

## Real Big Block, stage 1, 2019-07-07

https://www.reddit.com/r/Grycoin/comments/ca6jxv/77_mbtc_quizchain2_block_77_stage_one/

> "I will give no information on solution format, no first digits of MD5 hash,
> nothing. I do disclose that this one has no TOMI field, but that is all. You
> are on your own completely."

> "And I will publish the complete solution as the Second stage of this block.
> This solution will in turn be the question for the Second stage, which will
> have the final 777 mbtc prize."

The question for this stage links to Hal Finney's "Bitcoin and me" post on
bitcointalk (topic 155054). Stage 1's escrow, `19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN`,
was solved and swept on 2019-08-03; its answer is not part of the live prize and
is used in this folder only as a mechanism reference (see README).

**Confirmed, 2026-08-17**: the case-flip rule (paragraphs 2, 3, 4, and 6 of
Finney's 16-paragraph post get their first letter lowercased and last letter
uppercased, joined with a blank line) reproduces this exact address, provided
the author's own trailing note at the end of the post, "[edited slightly]",
stays attached to the 16th paragraph by a single line break, exactly as the
raw page source (`https://bitcointalk.org/index.php?topic=155054.0`, view
source) renders it. 2 rendered-text copy-pastes of the post both silently
dropped this note and both failed a 524,288-candidate exhaustive test before
the raw HTML was checked. Verified independently twice: once through
`tools/oracle.py`, once with direct `hashlib`/`bip_utils` calls sharing no
code with the oracle. See `analysis/tested.md` for the full record.

**Correction, 2026-08-17**: this repository previously stated the case-flip
rule was "proven" to reproduce this address using Finney's post text. A
person independently fetched that post from bitcointalk.org directly
(unreachable from this research environment on its own) and supplied it for
testing. Its text is not reproduced here (third-party historical content,
same policy as before), but the test result is: 524,288 combinations of
paragraph subset, flip direction, and line-ending convention, all against
`19TbyN5KCg1Lg7qHwezifsLVcdSa2Rj5KN`, 0 match. See README, "Certified
against", and `analysis/tested.md` for the full record. The post's structure
(16 paragraphs, exactly 4 starting outside `ITASM`) matches what this file's
prior description implied, which is consistent with a broadly accurate
transcription, but a byte-level difference from whatever the puzzle author
actually hashed in 2019 has not been ruled out.

## Quizchain2 Block 76, 2019-07-22

https://www.reddit.com/r/Grycoin/comments/cgcv9i/77_mbtc_quizchain2_block_76/

> "Question: change to"
> "Format: [solution] TOMI [TOMI]"
> "First three digits of MD5 hash are f8e (copypasted)."

Update, same thread: "First two digits of solution only are 1d."

Update, same thread: "Hint 1. Change question from \"change to\" to \"from change
to\"."

> "I will shut down soon now (after posting the second stage of 77), so I will
> not be available for hints or questions."

## Quizchain Block 29 (solved, reference only)

r/bitcoinpuzzles, `u/AoiNakamoto`, "[Easy] [7 mbtc] Quizchain Block 29"
(undated in the copy read; from early in the series, well before Real Big
Block). Not part of the live prize (solved and swept) and unrelated to Real
Big Block's own escrow; useful here only because its text and mechanism are
now directly readable, and because it happens to be the source of a
duplicate excerpt that appears on the live "Second" chapter's Wattpad page
(see README, "second copy" note).

Question: "Second version." Format: `[solution] [link]`. Update, posted in
full: "Copypaste from my draft, exactly same as used for hashing:" followed
by the complete source text (not reproduced here in full; it opens "Good
morning, Tom." and is the same opening dialogue scene later reused, reworded,
in the "Second" Wattpad chapter). The confirmed solution, posted after the
block was solved: "just change the o and i in 'voice' in the second
sentence to 'O' and 'I', same method as in Block 2. Only two letters
changed is good match to title 'second' as well as to method from block 2."
That is, in "A pleasant female voice." (the draft's second sentence), correct
to "A pleasant female vOIce."

This confirms the mechanism for block 29 specifically is a single-word
letter-case correction, not the paragraph-level case-flip rule confirmed on
Block 77 Stage One. The draft text is a near-verbatim match (1 word
different: "Overlord" vs "Omnipotent") for the second, differently-worded
copy of the "Second" chapter's opening scene found on the live Wattpad page
(see README); this is a far more specific and better-evidenced explanation
for that duplicate than the earlier theory that it was an impersonator's
altered copy.

## Real Big Block Discussion thread

https://www.reddit.com/r/Grycoin/comments/chn8un/real_big_block_discussion/

2019-07-25: "When I posted the real big block at the Wattpad site, I added extra
line breaks between paragraphs. This information is needed to solve the block."

2019-07-28, replying to a reader who quoted her original post back at her and
said "I still don't see the line breaks": "I have line breaks in the chapter
between all paragraphs. And there are two line breaks there now, since Wattpad
would not display them correctly with only one each. I analyzed them with the
tool at asciivalue.com and that shows one 13 and one 10 for each of the line
breaks. The solution you need to hash with has only one line break between
paragraphs, which is one 13 and one 10 in ASCII according to the
asciivalue.com tool. Again, I will probably post this to dropmefiles.com later
in the original format, once people actually have a shot at solving this
block." This statement is specifically about her original post (the reader
was quoting it as "1 point, 2 days ago"), i.e. about the superseded address:
displayed on Wattpad as 2 line breaks (`\r\n\r\n`) because Wattpad would not
render 1, but hashed with only 1 (`\r\n`).

2019-07-31: "I took back the prize for a moment and sent it again to a new
address, hashing with a slightly different solution [...] It has multiple
paragraphs and two line breaks between each of them."

Same thread, immediately after the 2019-07-31 post, a reader (martypyouknowme)
asks her to disambiguate "two line breaks" as either one keystroke-Enter
between paragraphs or two, with a worked example of each. Her reply: "I mean
the second one. Hit enter twice. This displays in Ascii as 13 10 13 10,
according to asciivalue.com." martypyouknowme: "asciivalue.com. Got it. Thank
you." (no further detail in that reply). Read together with the 2019-07-28
quote above, these are 2 different statements about 2 different addresses, not
a contradiction: the superseded address was hashed with 1 line break (`\r\n`)
between paragraphs, the current, still-funded address confirmed here was
hashed with 2 (`\r\n\r\n`). Every whole-chapter and whole-section candidate has
been tested under `\r\n\r\n` against the current address (see
`analysis/tested.md`); 0 match so far, so the separator is now high-confidence
but the exact paragraph selection is still open.

She also mentions, in an aside earlier in the same thread: "I just noticed
that the 7th private key in the list for this wallet contains the number 7
three times [...] the first one also has some amazing properties," which is
why `tools/oracle.py` now checks derivation indices 0 through 19 rather than
0 through 5: she was looking at more than 6 derived addresses for at least one
block in this series, so the oracle should too.

This last post corresponds to the current, still-funded escrow
(`14zMkTgaVXJcxdh4JdWi29MLRR44iUSG9W`, funded 2019-07-30); an earlier address,
`1EFojcAo2vbhRGCGCa7q8Wwvzss28mhQYC`, was funded 2019-07-24 from the
before-the-rehash solution and holds no funds today.

## The Wattpad chapter

https://www.wattpad.com/720888559-second

The author's own published chapter, titled "Second", posted under her own
Wattpad account. Its text is the confirmed source of Real Big Block stage 2's
answer (see README). This folder does not reproduce the chapter text.

**Update, 2026-08-17**: the chapter is paginated into 12 Wattpad pages
(9,091 words). The working transcription used for testing up to this point
had, without anyone noticing, only ever covered the first 5 of those 12
pages - roughly the first 40% of the chapter, ending mid-way through the
Grycoin whitepaper section. Pages 6 through 12 (the rest of the whitepaper,
plus the entire "III. Second Identity" section, in which the author explains
her own Satoshi/Hal Finney "Satoshi Code" reasoning at length) had never been
transcribed or tested against either escrow at all. A person fetched all 12
pages directly from Wattpad (page 1's raw page source, pages 2-12 via the
chapter's own plain-text API endpoint), and each was diffed paragraph by
paragraph against the working transcription, the same fidelity check that
resolved the Hal Finney post above. This found 5 small byte-level errors on
pages 1-5 (missing spaces around 2 inline line breaks inside paragraphs,
missing trailing spaces at the end of 2 paragraphs) and, far more
significantly, the missing 148 paragraphs from pages 6-12. The complete,
corrected chapter is 272 paragraphs; see README and `analysis/tested.md` for
what has since been tested against it.

**Update, 2026-08-18: "Second" is 1 of 33 chapters ("parts") in a single
Wattpad story, not a standalone piece.** The story's own page metadata lists
all 33 part titles and URLs; this had never been examined before. Several
titles are directly relevant and unread as of this update: "TOMI" (720888559
+ ~617k = 721505724), "Complete Quizchain" (720895205), "Complete Second
Round of the Quizchain" (742662804), "Utter Disaster Three Block Series"
(720893344), "Second Life", "Hoax", "FU AOI", "4444 and 4442" (all published
essentially back-to-back with "Second" itself, judging by how close their
part IDs are to 720888559), plus a long tail of titles suggesting
meta-commentary on the puzzle series itself ("Difficulty", "Difficult
Hints", "Exceedingly Unfair Riddle", "Quizchain Lottery", "Satoshi's
Puzzle???", "Genesis Block Mystery", and more).

The "TOMI" chapter (read in full 2026-08-18) explains the field's history
directly relevant to Block 76: it was originally called "BFUB" (the "FU" the
author says she got "annoyed by... in the field name"), renamed to "TOMI"
("Thinking Only Method" + a nonce "I", also Japanese for "wealth"). Critically,
she writes: "I had already written a three block new post hashed with the
old format. When I changed the text to the new one, I forgot that this would
not work. I would need to hash with TOMI again... I realized this once a
user reported that hashing with the rather obvious solution for this did not
work." This is a direct admission of a display/hash mismatch bug affecting a
post covering 3 blocks - and a Wattpad chapter titled "Utter Disaster Three
Block Series" exists in the same story, strongly suggesting it is that exact
post, not yet read. If Block 76 is one of the 3 affected blocks, the
community-found "format"/"before TOMI" pair - which passes both published
MD5-prefix hints but has never produced the escrow address under any
derivation tried (see `analysis/tested.md`) - may be a coincidental prefix
match on the wrong field-name literal, exactly as this repo's own
2019-07-29-comment-timing cross-check already suspected. A first small test
(solution "format" against "FU", "BFUB", and other old-name variants in
place of "TOMI", against a handful of plausible values) found no prefix or
derivation match, but the real old-format text is not yet known and this
remains the single most promising open lead for Block 76.

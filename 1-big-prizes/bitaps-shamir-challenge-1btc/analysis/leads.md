# Open leads: Bitaps Shamir secret-sharing challenge

Full notes. The README shows the ranked summary.

## 1. The 15-day archive gap (2020-06-19 to 2020-07-04)

The earliest archived capture of the challenge page I found is dated 2020-07-04, 15 days
after the address was funded and the 2 shares were published. Neither the Wayback Machine
CDX index nor Common Crawl has anything from this window for `bitaps.com/mnemonic/challenge`
or its regional mirrors. If a 3rd share, or a clarifying comment, was ever posted and then
edited out, this is the only window where it could have existed and gone uncaptured.
What would confirm it: any archiver, forum mirror, or dated screenshot from this specific
window showing a different page state. What would close it: a systematic search of
smaller/regional archivers and search-engine caches turning up nothing across the same
window, the way the 14-capture, 4-year search already did for the rest of the timeline.
Cost: an afternoon of searching alternative archivers; no compute.

## 2. Uncertified channels

archive.today returned HTTP 429 on its own known-good witness page when I tried it
(2026-08-03), so I could not tell whether it holds anything for this challenge; Memento
TimeTravel was unreachable the same session; I found no verified anonymous read route for
X replies to `@bitaps_com`; and Telegram's `t.me/s/bitapscom` public preview has not been
read. What would confirm or kill each: a working read of the channel that either surfaces
a 3rd share or comes back clean with a witness proving the read method works. Cost:
minutes to hours per channel, no compute.

**GitHub forks, closed 2026-08-16.** All 13 forks of `mnemonic-offline-tool` listed on
GitHub's network-members page (`0xGoerliMainnet`, `alfathsurya`, `digitalderrick`,
`djmuratb`, `goodlookingull-stack`, `KingParmenides`, `palashganguly38-code`,
`pingeye92`, `secp8x32`, `Stevenans985900`, `unit-code-cnbd`, `yatescleta-afk`,
`zanko7`) were cloned directly (`git clone --depth 50`) and checked both by commit hash
and by full remote branch list, not just a working-tree file diff (a diff alone would
miss a divergent share sitting in an unmerged branch or an earlier commit no longer in
the tree). Witness: 12 of the 13 resolve to the exact same commit as upstream,
`5b6dd995478b49c489b95444fbb0dca4006746a2`; the 13th, `Stevenans985900`, sits 1 commit
behind on the identical history (`91ea8b9`, missing only the final "grammar" wording
fix, itself already an ancestor commit of `5b6dd995` in the upstream repository, not a
divergent tip). Every fork has exactly 1 branch (`master`), matching upstream, with no
second branch anywhere. This closes the GitHub-fork channel: it carries no diverged
share and needs no further review.

## 3. Direct computation

Not ranked as a lead. The residual entropy is about 125 bits (see
`data/entropy_measurements.csv`), which is not in range for search on any hardware I have
access to. This door is closed by the numbers, not by assumption.

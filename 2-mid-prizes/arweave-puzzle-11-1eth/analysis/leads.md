# Open leads, ranked

## 1. A systematic LSB scan of the continuous grayscale and alpha channels (hours; 1- and 2-bit widths done, 2026-08-16)

Every candidate tried before 2026-08-16 read the geometry (building heights, widths, roof
lines) or the container metadata as a whole value, hashed as a block. What was missing was a
bit-level scan of the 2 continuous 8-bit channels (grayscale, 256 levels; alpha, 26 distinct
values observed), the most direct reading of the author's own hint that "format does not
matter," which argues for a payload in the pixel values themselves rather than in any container
structure.

Run on 2026-08-16: every possible 256-bit window, sliding 1 pixel at a time, across
{grayscale, alpha} x {row-major, column-major} x {MSB-first, LSB-first byte packing}, at both 1
and 2 bits extracted per pixel. 13,431,083 candidates total (4,994,119 at 1 bit per pixel,
8,436,964 at 2 bits per pixel), each derived to an ETH address and compared byte-exact to the
target. 0 matches; the best coincidental prefix match was 3 of 20 address bytes at 1 bit per
pixel and 2 of 20 at 2 bits per pixel, both consistent with chance at this sample size, not a
signal. See `analysis/tested.md` for the full family-by-family breakdown, rates, and dates.

This confirms: an extracted 64-hex string derives the target address exactly, which did not
happen. Kills, for 1 and 2 bits per pixel specifically: an exhaustive bit-order and bit-width
sweep of both channels with no address match, which has now been run to exhaustion at those 2
widths. Not yet run: bit widths of 3 or more per pixel. Each additional width has a lower prior
probability as an intended encoding (simple 1-bit LSB steganography is by far the most common
convention, which is why it was tried first and most thoroughly), and extending further without
a narrowing insight first would be exactly the kind of open-ended compute this repository's own
methodology (`AGENTS.md`) argues against. This lead is downgraded from the top-ranked open lead
to closed-at-known-widths; the next step here needs a reason to expect the encoding is wider
than 2 bits per pixel, not more raw scanning.

## 2. Join the community Telegram group and search first-hand for the "$100" hint (needs a
person)

I already searched a full local archive of `@arweavep` (55,002 messages, November 2021 to May
2026) and found no later message announcing new hints, plus 47 messages from other members
independently confirming the promised follow-up never arrived. That closes this as a lead
inside the archived window. What remains untested is anything posted before the archive's
start (the announcement itself is from April 2020) or through a channel the archive does not
cover, such as a direct message or a since-deleted post. Confirms: a member with early access
to the group, or Tiamat directly, produces a hint not present in the archive. Kills: nothing
further can kill this lead technically; it depends on information I do not have a channel to.

## 3. Puzzle #9's real solving method, if it ever surfaces (needs new information)

Tiamat described puzzle #9 as "similar" to #11, and #9 was swept by an anonymous solver in
2020 who never published a method; multiple community members describe the last step as
"forced" (brute-forced), not derived from a stated rule. If a #9 write-up ever surfaces, it
would give a real, oracle-certifiable answer to calibrate #11's harness against, which is
exactly what this folder is currently missing. Confirms: a published #9 method that this
folder's harness can reproduce byte-exact, at which point the same method becomes a certified
candidate class for #11. Kills: nothing; this is a standing watch item, not an active search.

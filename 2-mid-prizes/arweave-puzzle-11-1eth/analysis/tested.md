# Tested (full negatives ledger)

No certified oracle exists for this puzzle: the target is a raw 256-bit private key with no
intermediate checksum, so every candidate below was checked by deriving its ETH address
(`eth_keys`, compressed public key) and comparing it byte-exact (case-insensitive on the hex)
against `0xFF2142E98E09b5344994F9bEB9C56C95506B9F17`. The derivation code itself (SHA-256,
Keccak-256, and secp256k1 point multiplication) is standard and was checked against public
test vectors, but I have no known-answer candidate specific to this puzzle to certify the
mapping from image to key, so every row below is "uncertified" in the sense that a clean run
proves the tested candidates are wrong, not that the harness would have caught every possible
right answer. I also flag near-misses (an ETH address starting with the same 2 bytes, `ff21`)
as an extra check; none occurred in any family below.

## Geometry-derived candidates

| Hypothesis | Space | Method | Result | Witness | Date |
|---|---|---|---|---|---|
| Building height/width/roof-y/x0 sequences (raw, sorted ascending, sorted descending, interleaved), joined with 5 separator styles, padded left/right to 32 bytes, first/last 32 bytes, 2-hex-digit encoding per value | about 460 candidates total across this and the next 3 rows | SHA-256, double SHA-256, Keccak-256, compared to target address | 0 match, 0 near-miss (no derived address even starts with `ff21`) | uncertified (no known-answer vector for this puzzle) | 2026-06-13 |
| Raw pixel hashes: grayscale channel, alpha channel, full PNG file, first/last 32 bytes of the flat grayscale array | included above | SHA-256, Keccak-256 | 0 match, 0 near-miss | uncertified | 2026-06-13 |
| cHRM chunk (32 bytes) and its byte-reversed form, raw and hashed | included above | direct, SHA-256, Keccak-256 | 0 match, 0 near-miss | uncertified | 2026-06-13 |
| Object counts (12 buildings, 1 large sail, 5 small sails, 2 clusters, left/right counts) as a byte sequence | included above | SHA-256 | 0 match, 0 near-miss | uncertified | 2026-06-13 |
| Matrix reshape of the grayscale channel at 7 column widths, first/last row and column strips | 56 strips | first 32 bytes, SHA-256 | 0 match, 0 near-miss | uncertified | 2026-06-13 |
| Value-band pixel masks (bands including 240 to 245, 235 to 254, 248 to 254, 1 to 30) | 4 bands | SHA-256, first 32 bytes | 0 match, 0 near-miss | uncertified | 2026-06-13 |

## Metadata-derived candidates (the date:create / date:modify anomaly)

The PNG's own `tEXt` chunks (confirmed present in `clues/arweave-puzzle-11.png`, reproduced
2026-08-16) read `date:create 2020-03-30T11:38:07+03:00` and
`date:modify 2020-03-30T11:34:44+03:00`: the modify timestamp precedes the create timestamp,
an anomaly present only in this puzzle and its sibling puzzle #9.

| Hypothesis | Space | Method | Result | Witness | Date |
|---|---|---|---|---|---|
| ISO date strings, digit strings, Unix epochs, and their difference/sum/XOR, in decimal and big/little-endian 4 and 8-byte encodings, alone and concatenated or XORed with the address and the cHRM bytes | dozens of encodings times {SHA-256, double SHA-256, Keccak-256, BLAKE2s, first 32 bytes, last 32 bytes} | direct address comparison | 0 match, 0 near-miss | uncertified | 2026-06-13 |

## Alpha channel and sibling-puzzle-calibrated candidates

| Hypothesis | Space | Method | Result | Witness | Date |
|---|---|---|---|---|---|
| 260 near-white pixels from the sibling puzzle #9's own 8-level image, tested as a carrier under many bit orders (raster, polar, radial), bit widths (1 to 3 bits per pixel, MSB and LSB first), and symbol mappings, plus several passphrase guesses hashed with SHA-256, double SHA-256, and Keccak-256 | several hundred combinations | address comparison, calibrated against puzzle #9's real (and already spent) address as a positive control | 0 match, 0 near-miss on #9 itself (so the method is confirmed not to reproduce the known #9 answer either) | yes, on the #9 positive control only | 2026-06-13 |
| Container-level myths (embedded executable or filesystem inside the PNG) | full file | binwalk, manual chunk inspection | refuted: file is a clean, valid PNG (IHDR, gAMA, cHRM, bKGD, pHYs, 22 IDAT, 3 tEXt, IEND chunks), 0 bytes after IEND; the "executable" reports from other solvers are binwalk false positives on near-random decompressed pixel bytes | yes (direct chunk inspection) | 2026-06-13 |
| Alpha channel as a data carrier | full channel | direct pixel inspection | 434 pixels have alpha under 255, all clustered on the large sailboat's outline (an anti-aliasing halo from a copy-paste), values 1 to 30, consistent with a smoothed edge rather than structured data | yes | 2026-06-13 |

## Exhaustive 1-bit-per-pixel LSB sweep (2026-08-16)

Every possible contiguous 256-bit window was tried as a raw private key, sliding 1 pixel at a
time across the grayscale and alpha channels: `num_windows = num_pixels - 255` per channel per
scan direction per byte-packing order. This is the systematic LSB scan named in open lead 1,
run to exhaustion for 1-bit-per-pixel extraction specifically.

| Hypothesis | Space | Method | Result | Witness | Rate | Date |
|---|---|---|---|---|---|---|
| LSB of grayscale channel, row-major and column-major, MSB-first and LSB-first byte packing | 4 families, up to 1,767,745 windows each (1,161,114 to 1,292,262 valid non-degenerate candidates per family after skipping all-zero windows from uniform background regions) | direct secp256k1 + Keccak-256 address derivation, compared byte-exact | 0 match, best coincidental prefix match 3 of 20 address bytes (consistent with chance at this sample size, not a signal) | uncertified (no known-answer vector for this puzzle) | about 11,800 to 12,200/s | 2026-08-16 |
| LSB of alpha channel, same 4 combinations | 4 families, up to 1,767,745 windows each (18,431 to 25,296 valid candidates per family; the channel is constant 255 outside 434 pixels, so almost every window is the degenerate all-ones value and is correctly skipped as out of curve range) | same | 0 match, 0 near-miss | uncertified | about 2,200 to 3,100/s | 2026-08-16 |

Cumulative: 4,994,119 candidates tested across 8 families (every combination of {grayscale,
alpha} x {row-major, column-major} x {MSB-first, LSB-first} at 1 bit per pixel), 0 matches. This
closes 1-bit-per-pixel LSB steganography, exhaustively, as a candidate encoding for this image.

## Exhaustive 2-bit-per-pixel LSB sweep (2026-08-16)

Same method extended to the 2 low bits of each pixel (the low bits packed MSB-first and
LSB-first within each pixel's 2-bit symbol, both scan directions, both channels): every
contiguous 256-bit window across the resulting bitstream, `num_windows = num_pixels*2 - 255`
per family.

| Hypothesis | Space | Method | Result | Witness | Rate | Date |
|---|---|---|---|---|---|---|
| Low 2 bits of grayscale channel, row-major and column-major, symbol-MSB-first and symbol-LSB-first | 4 families, about 3,535,745 windows each (1,992,070 to 2,176,102 valid candidates per family) | direct secp256k1 + Keccak-256 address derivation, compared byte-exact | 0 match, best coincidental prefix match 2 of 20 address bytes | uncertified | about 11,500 to 15,100/s | 2026-08-16 |
| Low 2 bits of alpha channel, same 4 combinations | 4 families, about 3,535,745 windows each (20,287 to 29,992 valid candidates per family; same alpha-channel degeneracy as the 1-bit sweep) | same | 0 match, 0 near-miss | uncertified | about 2,100 to 3,400/s | 2026-08-16 |

Cumulative: 8,436,964 candidates tested across 8 families at 2 bits per pixel, 0 matches. Combined
with the 1-bit sweep above: 13,431,083 candidates tested, 0 matches, closing simple LSB
steganography (1 and 2 bits per pixel, both channels, both scan directions, both packing orders)
exhaustively for this image. Wider bit widths (3+) were not attempted: each additional width has
lower prior probability as an intended encoding and was judged not worth the added compute
without a narrowing insight first, per this repository's own "insight over compute" guidance.

## What the ~460-candidate geometry sweep and the metadata sweep together rule out

Between the two families above, on the order of 1,000 candidates were checked, all through the
same address-comparison harness, with 0 matches and 0 near-misses anywhere. This rules out
every direct, single-transform reading of the measured geometry and the metadata anomaly that I
was able to enumerate. It does not rule out a reading that depends on information outside this
image, such as the promised but never-delivered "$100" hint (see "Open leads, ranked").

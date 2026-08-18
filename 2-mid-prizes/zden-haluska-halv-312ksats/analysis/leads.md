# Open leads, full notes

## 1. A hint published by the author

Every other long-open puzzle in Zden's series (LTC, Codex, Demobit, Janus) eventually
received a published hint. HALV alone has none as of the most recent check of the author's
site (2026-07-02): probe URLs following the author's own hint-naming pattern for other
puzzles return 404, and the HALV page itself is unchanged since the original 2024
announcement.

The author's own framing of the puzzle, "this level is way easier than LVL 5," reads as
pointing toward a short missing reading key rather than a finer pixel-level extraction: the
image's measured information capacity (about 118 bits) is well under the 256 bits a private
key needs, so recovering the full key from geometry alone, at the fidelity currently
available, would if anything be harder than LVL5, not easier. A single clarifying message
from the author is the highest-ranked lead for this reason.

## 2. Certify the oracle itself with a known-good vector

This is the cheapest possible step: the oracle shipped in this folder already does this
(`tools/oracle.py --selftest` certifies against a standard public vector), which upgrades any
future negative result from uncertified to properly witnessed. It does not, on its own,
change what has already been tried against the image.

## 3. Read the tick-mark ladder found 2026-08-16 (minutes, low priority)

A small vertical ladder of about 8 to 9 short, evenly-spaced dashes sits at pixel column
x=90-92, rows y=446-506, separate from the waveform itself. It was not part of any prior
established fact or tested hypothesis in this folder. Every dash appears the same size within
anti-aliasing noise, which reads more like a scale or ruler marking than a data channel, but
this has not actually been tested as a candidate reading (count as a number, presence pattern
as bits, position as an offset). Ranked low because even a full extra channel here (at most a
handful of bits from 8 to 9 marks) cannot close the roughly 138-bit gap between the image's
measured capacity and a 256-bit key on its own; it is only worth a look if paired with lead 1.

## Not recommended

Further pixel-level re-extraction of the published image is not expected to be productive on
its own: the lobe count, shape channel, and amplitude model have each been independently
reproduced 3 times, and the resulting capacity measurement (about 118 bits) is the identified
limit, not a fidelity problem with the current reading. The tick-mark ladder above is a bounded
exception, not a reversal of this conclusion.

# Where the numbers come from

Every number in [README.md](README.md), [method/README.md](method/README.md) and [reading/](reading/), and the file in this repository it is taken from. They were taken from the records made when the work was done (18–19 October 2026), not typed from memory.

| number | meaning | source in this repository |
|---|---|---|
| 24 lines with cipher, 25 rows | size of the passage | rows of `data/signs.txt` (row 1 is wholly clear) |
| 643 cipher signs, 51 distinct | size of the stream | items of `data/signs.txt` outside brackets |
| 9 changes | corrections kept | `data/corrections.json` `applied` |
| 128 places; 21 improving, 127 bits; 21 improving, 70 bits | reader-backed changes and random changes, scored under the key | `data/controls.json` `correction_control` (`reader_backed`, `random`) |
| 0.80–0.84; 0.79–0.85; 0.737 | reader passes agreeing with one another, with our reading, all five | `data/controls.json` `reader_agreement` |
| 4.11, 4.01, 3.59, 3.50, 4.345 bits per letter | whole-stream decodes of the vote, the vote plus our reading, our reading before and after the nine edits, and our reading with its signs shuffled | `data/controls.json` `whole_stream_decodes` |
| −1800.56; seeds 101–104; 400,000 x 48; 1,000,000 x 96; 4,096 chains | the recorded fit-only runs | our run records (not in this repository); seed 101 and its settings in `data/controls.json` `verifier.attack` |
| cipher signs 184–312, lines 8–13 | the held-out block | `data/controls.json` `verifier.attack.params.heldout_excluded` (end exclusive); lines counted from `data/signs.txt` |
| 19 signs; 20, 60, 97 | where the two keys differ | `data/keys-compared.json` |
| *ducati* three times, *li dua milia* twice | repeated words | `data/plaintext-whole-stream-by-line.txt` (lines 5, 9, 13; lines 10, 11) |
| `partial_reading`; "language did not pass" | the verifier's verdict and reason | `data/controls.json` `verifier.verdict`, `verifier.reasons` |
| 3.6175 (3.92), 0.4358 (0.36), 0.0248 (0.01), 4 | language: bits, dictionary cover, null-test gain, occurrences of the sign | `data/controls.json` `verifier.checks.language`, `verifier.limits` |
| 3.7413, 0.1238 (0.40), 0.16 (0.15) | held-out block: bits, rise, dictionary drop | `data/controls.json` `verifier.checks.heldout` |
| 60 controls; 0.3327, 3.9389; 100 permuted keys; 0.9961 | controls | `data/controls.json` `verifier.checks.controls` |
| 0.9969 | coverage | `data/controls.json` `verifier.checks.coverage` |
| 1.0 | stability | `data/controls.json` `verifier.checks.stability` |
| 0.32 against 0.30; 0.10 against 0.15 | control margins on bits and cover | differences of the values above; `verifier.limits` |
| 2.53–2.60; 3.26–3.73, 0.78–0.94; 3.64–3.92, 0.44–0.85; 3.92–3.94, 0.20–0.62 | known-answer twins at 0, 10, 15, 20 % misread | `data/known-answer-twins.json` |
| 10–15 % misread | the estimate | the letter's 3.50 against the twins (above) |
| 3072 × 4096; 26 pixels; 93 pixels; 1.4 grey levels, 0.9996 | the image, the writing height and line spacing, the two image sets compared | our image records (not in this repository); the file can be fetched from the link in the README and checked against the SHA-256 in `method/README.md` |
| 16 of 20 | Bourdeau's sign values that agree with our whole-stream key | his values as listed in [PRIOR-ART.md](PRIOR-ART.md) against `data/key-whole-stream.json` |
| 13 of 92; 584 | Bourdeau's figures | his notes (link in [PRIOR-ART.md](PRIOR-ART.md)) |
| byte counts in the check output | sizes of the plaintext files | `sh decode/check.sh` |
| dates and times of the searches | prior art | [PRIOR-ART.md](PRIOR-ART.md) |

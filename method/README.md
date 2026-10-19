# How the reading was made

This folder explains how the files in `../data/` were made and how far they can be trusted. The working code depends on our own tools and language resources and is not published; what is here is enough to see what was done and to reproduce the decode exactly (`../decode/`). Every number below is in `../data/` (see `../NUMBERS.md`).

## The page and the image

The cipher is on f. 1v of the letter (the verso of the first leaf): 24 lines of two-digit figure groups with some letter signs and lone digits, and clear Italian before, between and after them. There is no decipherment, gloss or interlinear reading on any page of the letter.

Only one photograph is public. Vestigia (record 1904) serves two sets of images of this letter: the Hungarian National Archives set (`HU_MNL_OL_X_10891_DF_294959_0001`–`0004`) and a black-and-white set (`1397657007`, `-2`, `-3`, `-4`). For the cipher page the two are **the same photograph** at two JPEG qualities (mean grey difference 1.4 levels, correlation 0.9996). Both are served at 3072 × 4096 pixels; the original files are not served. We used `HU_MNL_OL_X_10891_DF_294959_0002.JPG` as served on 19 October 2026 (SHA-256 `aaef51fea59183a617b58769a08b2c9255a5669685fc640b7690fbc0e1b67727`). On it the writing is about **26 pixels high** and the lines are 93 pixels apart. This single, small photograph is the limit of the reading.

## Step 1: our transcription, by eye

The page was cut into enlarged windows and read sign by sign by eye (by Claude in a working session, 18 October 2026, not by a batch reader). The scribe writes the digits of a line without spaces; runs were cut into groups ending in 0, 5 or 6 where possible, else into single digits. Letter signs were named by their look. The scribe's 0 and 6 are alike (a 6 is a 0 with a rising stroke), and this is the commonest doubt.

On the image, the lone "15" that stands between clear words (three times on line 1, once on line 8) is the crossed abbreviation *et* of the clear text, not a cipher group; it is written `et` in the clear text.

## Step 2: five Claude reader passes, voted (hints only)

A sign sheet of 18 examples cut from this page was made. Each line was straightened and cut into pieces, and five passes were made with Claude (Anthropic, model Opus 5.5, effort high), each with a different cut, enlargement (2.5x–4x) and colour/grey setting, the sheet shown first, three or so pieces per call. Every piece was read; five calls ended in a refusal and those pieces were read again alone; no refused answer was used. The answers were treated as data and parsed into sign names. The five passes were aligned and voted.

The passes agree with one another on 0.80–0.84 of aligned signs and with our reading on 0.79–0.85; all five agree on 0.737 of places. No text of the page is known, so no accuracy per sign can be measured; the passes share one model and one image, so their errors are not independent.

**The voted reading decodes worse than our reading by eye** (4.11 bits per letter against 3.59 before the edits; lower is more like Italian). So the vote was not used as a reading, only as a source of hints for Step 3.

## Step 3: corrections, only where the image supports them, with a random-edit control

Code listed the 128 places where at least three of the five passes agree against our reading, and scored each single change under the current key. 21 of them improve the decode, by 127 bits in all. **Control:** 128 random changes scored the same way also give 21 improving changes, worth 70 bits. A gain in the decode is therefore not evidence by itself: a key fitted to a noisy text rewards some random changes too.

A change was kept only if at least four of five passes agreed on it, it improved the decode, **and the image, looked at, did not contradict it**. Nine were kept (`../data/corrections.json`), among them two deletions of groups the first reading had added. The largest-gain proposal was rejected: the readers drop one of two "90 90" on line 18, and the image plainly shows both.

A second round re-read the 28 worst-decoded short stretches at 4x, three times blind. The readers agreed against us on 60 places, but under the key nearly all of those changes made the decode worse (for example 70 read as 10, three times), and all three dropped the same repeated group on line 18. None was kept.

## Step 4: the key, from random starts

The signs were attacked as a homophonic substitution (one letter, several signs) by simulated annealing from random starting keys, scored by character language models built from period Italian texts.

- **Whole-stream key** (`key-whole-stream.json`): annealing on all 643 signs, with the clear Italian of the letter kept in place as context for the language model (the clear words act as cribs around the cipher stretches). 3.50 bits per letter; the same signs shuffled into a random order and attacked the same way, 4.345. This is the key of the reading.
- **Fit-only key** (`key-fit-only.json`): the same method with a held-out block (cipher signs 184–312, lines 8–13) left out of the fit, so that the block can test the key. 400,000 iterations x 48 restarts, seed 101; seed 102 at the same settings, seed 104 at 1,000,000 x 96, and a second, batched annealer written for the GPU (4,096 parallel chains, seed 103) all reach the same score (−1800.56), so the search has converged. This is the key the verifier judged.

The two keys differ on 19 signs, three of them frequent (20, 60, 97). The whole-stream values give repeated Italian words (*ducati*, *li dua milia*); the fit-only values do not (*sucati*, *li sua dilia*). We prefer the whole-stream key for the reading and say so; it has not been judged by the verifier.

## Step 5: the verifier

Our verifier's thresholds were fixed (frozen) before this letter was attempted and were not changed for it. It runs eight checks on a key and its decode. On the fit-only key its verdict is **`partial_reading`**, its third rung of five (characterised, key fragment, partial reading, candidate solved, solved). The checks:

| check | result | numbers (limit) |
|---|---|---|
| mechanical (the key is well-formed) | pass | |
| re-encryption (the key turns the plaintext back into the signs) | pass | 0 mismatches |
| coverage | pass | 0.9969 of signs have a value |
| language | **fail** | bits 3.6175 (≤ 3.92) pass; dictionary cover 0.4358 (≥ 0.36) pass; **null test fails**: blanking one rare sign, the letter sign *n* (4 times in the fitted part), improves the bits by 0.0248 (limit 0.01) |
| held-out block | pass | bits 3.7413, a rise of 0.1238 (≤ 0.40) |
| controls | pass | 60 attacked controls (20 shuffled, 20 block-shuffled, 20 frequency-matched gibberish): best 0.3327 cover, 3.9389 bits, against 0.4358 and 3.6175 for the letter; 100 permuted keys; a known-answer cipher of the same kind solved (0.9961 of characters) |
| stability (independent seeds agree) | pass | 1.0 |
| novelty | not yet recorded at the time of the verdict | the prior-art search is in [../PRIOR-ART.md](../PRIOR-ART.md) |

The only reason given is that the language check did not pass, and within it only the null test. The sign *n* may stand for something other than a letter (a code sign such as *non*) or be misread; on line 13 it looks like a plain *n*. Treating it as a code sign now would be a choice made after seeing the verifier's result, so we have not done it.

Two narrower points: the controls separate from the letter by bits (0.32 against a required 0.30), not by dictionary cover (0.10 against 0.15); and in the held-out block the dictionary cover drops by 0.16 (limit 0.15) while the bits pass, and either passing is enough.

## Step 6: how many groups are still misread

No text of the page is known, so this is estimated with **known-answer twins** (`../data/known-answer-twins.json`): 640 letters of period Italian that the language model never saw, enciphered with 51 signs like this letter, with 0, 10, 15 or 20 % of the signs replaced by others (simulated misreads), then attacked the same way. Clean twins decode at 2.53–2.60 bits per letter with every letter right; at 10 % misreads 3.26–3.73 bits and 0.78–0.94 of letters right; at 15 % 3.64–3.92 and 0.44–0.85; at 20 % 3.92–3.94 and 0.20–0.62. The letter, at 3.50 bits (with the clear text as context, which the twins do not have), sits between 10 and 15 %. So **an estimated 10–15 % of the cipher groups are still misread**: roughly one in seven to ten.

## What cannot be repeated from this repository alone

Claude's sign readings (recorded in our working files, not re-run), the annealing runs themselves, and the language models and dictionary used for bits per letter and dictionary cover (built from our own period corpora). The decode from signs and key is a lookup, and anyone can repeat it with `../decode/decode.py`.

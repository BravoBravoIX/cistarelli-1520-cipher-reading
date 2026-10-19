# The Cistarelli cipher letter of 25 July 1520: a first connected reading

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23471133.svg)](https://doi.org/10.5281/zenodo.23471133)

**Alfonso Cistarelli, at Eger, to Cardinal Ippolito I d'Este, 25 July 1520.** Archivio di Stato di Modena, Ambasciatori, Ungheria b. 4, Cistarelli no. 3, f. 1v (Vestigia 1904; DECODE R1137; Hungarian National Archives DF 294959). A letter in Italian with a passage of 24 lines in a cipher of two-digit figures and letter signs, set inside clear text.

> **First connected reading, version 0.1 (19 October 2026), partial.** The key was recovered from the ciphertext alone (no key from the time is known). Daniel Bourdeau's earlier ciphertext-only attempt gave a partial key and phrase fragments; our key, found independently, agrees with his on 16 of his 20 values. What is new here is the connected reading of the passage, its sense, and the verifier check.
>
> No key and no decipherment of this cipher is known, from the time or since. The key here was recovered from the cipher text alone. About a tenth to a seventh of the cipher groups are probably still misread, and the reading is partial: some stretches give Italian words and phrases, others do not yet read.
>
> **Earlier work:** Daniel Bourdeau's Cyphersolver catalogue lists this letter as **not solved, fragments only** (<https://dbourdeau.github.io/cyphersolver/cistarelli1520.html>, posted 15 October 2026). His partial key and fragments agree with ours in many places; see [PRIOR-ART.md](PRIOR-ART.md). We credit his work and build on the same conclusion: the photograph is the limit.

## What the cipher passage seems to say

> **Working hypothesis, not a finding:** the passage reports on money for the Cardinal: about **two thousand ducats to be changed into gold at a fair, through a Venetian, Messer Antonio**.

The words behind it recur under one key: *ducati* three times, *li dua milia* (the two thousand) twice, *cangiate in oro* (changed into gold), *questa fiera* and *altra fiera* (this fair, the other fair), *per megio de mesiere Antonio veneciano* (by means of Messer Antonio the Venetian), *non se poteriano poi cangiare* (they could not then be changed). Names and amounts are not confirmed; a better image could change any of it.

## The reading

The full reading, line by line, is in [reading/f1v-reading-v0.1.md](reading/f1v-reading-v0.1.md), in three layers kept apart:

1. **Italian literal:** exactly what the key gives, letter for letter (cipher in lower case; the letter's own clear Italian in capitals and brackets). This is the reading.
2. **Word split (editorial):** the literal cut into words, with gaps and probable misreads marked. A proposal by us, not the literal text.
3. **English (translation):** of the readable stretches only, by Claude. A translation, not the text.

A sample, lines 16–17 and 23:

| line | Italian literal | word split (editorial) | English (translation) |
|---|---|---|---|
| 16 | sasatasefecicamgiarecirnaduamiliuiiqua | [?] se feci cam*(b)*iare [?] dua mili[a] [?] qua | "… I had [them] changed … the two thousand …" |
| 17 | lipermegiodemesiereantoniouenecianomi | li per megio de mesiere Antonio veneciano mi | "… by means of Messer Antonio the Venetian …" |
| 23 | [QUELLA VIA] nonsepoterianopoicangiuresenon | quella via non se poteriano poi cangi*(a)*re se non | "that way they could not then be changed except …" |

**Caveat: two keys.** The key of the reading is fitted on the whole passage. The key our verifier judged was fitted with lines 8–13 held out, and differs on 19 signs, three of them frequent: 20, 60 and 97 (*d*/*s*, *m*/*d*, *p*/*m*). Under it *ducati* reads *sucati* and *li dua milia* reads *li sua dilia*. The repeated words favour the whole-stream values, but this is not settled. Both keys and both literals are in [data/](data/).

## How it was done, in plain words

1. **Our own transcription.** The only photograph (see below) was read sign by sign by eye, in enlarged windows. The digits are written without spaces; the cut into groups is ours. A lone "15" between clear words is the clear abbreviation *et* (seen on the image), not cipher.
2. **Five Claude passes, voted.** Claude (Anthropic, model Opus 5.5) read the signs five times, with different cuts and enlargements and a sheet of sign examples cut from this page; the five readings were aligned and voted. The vote **decodes worse** than our reading by eye, so it was used for hints only.
3. **Corrections checked on the image, with a control.** Where at least four of the five passes agreed against us and the change improved the decode, the image was looked at; nine changes were kept. Random changes also improve a decode (70 bits against 127 for the reader-backed ones, over 128 changes each), so a decode gain alone was never taken as evidence.
4. **Key from random starts.** The signs were attacked as a homophonic substitution (one letter, several signs) by simulated annealing from random keys, on the CPU and with a batched annealer written for the GPU, scored by language models built from period Italian texts. The clear Italian around the cipher was kept in place as context, so the clear words act as cribs. Runs from different seeds reach the same key score.
5. **A verifier with fixed thresholds.** Our verifier's thresholds were fixed before this letter was attempted. Its verdict on the held-out key is **`partial_reading`** (the third of five rungs: characterised, key fragment, partial reading, candidate solved, solved):
   - **held-out text passes:** lines 8–13, left out of the fit, read as well as the rest (bits per letter rise 0.12; limit 0.40);
   - **controls pass:** 60 controls (shuffled, block-shuffled and gibberish signs) attacked the same way do not reach the letter (best 3.94 bits per letter against 3.62); 100 permuted keys; a known-answer cipher of the same kind is solved;
   - **stability 1.0:** independent seeds give the same key;
   - **language fails on one point only, the null test:** blanking the rare letter sign *n* (4 times in the fitted part) improves the score by 0.025 bits per letter (limit 0.01). *n* may be a code sign (for example *non*) or misread; we have not reinterpreted it after seeing the result.

Details: [method/README.md](method/README.md). Where every number comes from: [NUMBERS.md](NUMBERS.md).

## How much is still wrong, and why

No text of this page is known, so accuracy cannot be measured directly. On **known-answer twins** (period Italian enciphered like this letter, with a share of signs deliberately misread, attacked the same way), the letter's decode sits between the twins with 10 % and 15 % of groups misread. So **an estimated 10–15 % of the cipher groups are still misread**.

The limit is the image. **The only public photograph is a single 3072 × 4096 picture of the page, on which the signs are about 26 pixels high.** The two image sets on Vestigia are the same photograph at two JPEG qualities. At this size the 0 and the 6 (a 0 with a rising stroke), 80 and 86, 90 and 96 are often hard to tell apart, and machine readers make the same errors as one another. **A request for a high-resolution image has been sent.** With a better image we expect to re-read the passage, refit the key and re-run the verifier.

## The images

The images are on Vestigia, record 1904: <https://www.vestigia.hu/documents/1904>. The cipher page is file `HU_MNL_OL_X_10891_DF_294959_0002.JPG` (also `1397657007-2.jpg`, the same photograph): <https://www.vestigia.hu/media/01jzqer56q9psd802j1srdm7b6/conversions/01jzq1qbzaah81phq7qq6n8j02-1-web.JPG>.

Credit: Archivio di Stato di Modena; photographs Vestigia Research Group (Pázmány Péter Catholic University), also held by the Magyar Nemzeti Levéltár (Hungarian National Archives), DF 294959; via Vestigia. Vestigia makes its photographs available free of charge for non-commercial use, in accordance with Italian cultural heritage law. No image is copied into this repository.

## What is here

| folder | contents |
|---|---|
| [reading/](reading/) | The reading: Italian literal, word split (editorial), English (translation), the working hypothesis |
| [data/](data/) | The signs as read (`signs.txt`), both keys, both literals (stream and by line), the corrections, the verifier's checks and the controls, the known-answer twins |
| [decode/](decode/) | `decode.py`, a short stand-alone script (Python 3 standard library) that applies a key to the signs, and `check.sh`, which reproduces both literals byte for byte |
| [method/](method/) | How the signs were read, corrected, the key recovered and the reading checked |
| [PRIOR-ART.md](PRIOR-ART.md) | The prior-art search: dates, queries, results; Bourdeau's work |
| [NUMBERS.md](NUMBERS.md) | Where every number in this README comes from |

## How to reproduce the decode

Needs only Python 3 (no packages):

```
sh decode/check.sh
```

Expected output:

```
whole-stream stream: identical to data/plaintext-whole-stream.txt (644 bytes)
whole-stream by-line: identical to data/plaintext-whole-stream-by-line.txt (1266 bytes)
fit-only stream: identical to data/plaintext-fit-only.txt (653 bytes)
fit-only by-line: identical to data/plaintext-fit-only-by-line.txt (1266 bytes)
both keys reproduced exactly
```

The plaintext files were written by our own tools when the reading was made, so the check tests `decode.py` against an independent implementation. To read the letter line by line: `python3 decode/decode.py data/key-whole-stream.json data/signs.txt --by-line`.

What cannot be repeated from this repository alone: Claude's sign readings, the annealing runs, and the language models used for the scores (built from our own period corpora).

## Prior art

Searched on 18 and 19 October 2026, and repeated on 19 October 2026 (09:50–09:55 UTC) before this write-up: GitHub code and repository search (`Cistarelli`, `R1137`, `294959`, `"DF 294959"`, `"Cistarelli 1520"`, `Vestigia 1904`), recent commits of 23 active cipher-reading repositories, Tomokiyo's blog, the web, Vestigia and Bourdeau's catalogue. **No decipherment or reading was found**; the only earlier work is Bourdeau's entry, "not solved, fragments only". Every query and its result is in [PRIOR-ART.md](PRIOR-ART.md).

## Credits

- **Daniel Bourdeau**, Cyphersolver, for the catalogue entry, the first partial key and fragments of this cipher, and the judgement that the photograph is the limit.
- **Archivio di Stato di Modena**, which holds the letter, and the **Vestigia Research Group** (Pázmány Péter Catholic University) and the **Magyar Nemzeti Levéltár**, for the photographs and the record.
- **DECODE** (record R1137), for the catalogue entry.
- **Anthropic's Claude** (model Opus 5.5) was used as the sign reader, for the transcription by eye, the word split and the English translation.

Prepared by Brett Burford, October 2026. Corrections and better images are welcome.

## Licence

- Text and data (everything except `decode/`): [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0).
- `decode/`: [MIT licence](decode/LICENSE).
- No manuscript images are included. The images on Vestigia are for non-commercial use under Vestigia's terms.

## How to cite

Burford, B. (2026). The Cistarelli cipher letter of 25 July 1520: a first connected reading. Zenodo. https://doi.org/10.5281/zenodo.23471133 (this DOI always points to the latest version).

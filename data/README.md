# Data

The cipher passage on f. 1v of Alfonso Cistarelli's letter to Ippolito I d'Este, Eger, 25 July 1520 (Archivio di Stato di Modena, Ambasciatori, Ungheria b. 4, Cistarelli no. 3; Vestigia 1904; DECODE R1137). Version 0.1, 19 October 2026.

| file | contents |
|---|---|
| `signs.txt` | The signs as read, one manuscript line per row: line number, a tab, the items separated by spaces. Cipher signs are two-digit groups (`86`), lone digits (`0`), a few groups with a leading zero (`05`, `06`) and letter signs named by their look (`k`, `f`, `u`, `y`, `n`, `h`, `g`, `L`, `R`, `v`, `x`, `m`, and compound shapes such as `gL`, `gLk`, `gLoh`, `g'oh`, `Lj`, `n2`, `n3`, `nou`). The scribe writes the digits without spaces; the cut into groups is ours. Clear Italian written in the letter is in `[brackets]`, as we read it by eye. 643 cipher signs, 51 distinct |
| `key-whole-stream.json` | The key of the reading: each sign's letter, recovered by annealing on the whole stream |
| `key-fit-only.json` | The key the verifier judged: the same method with the held-out block (lines 8–13) left out of the fit. It gives no value to `g'oh` and `x` |
| `keys-compared.json` | The 19 signs on which the two keys differ |
| `plaintext-whole-stream.txt`, `plaintext-fit-only.txt` | The literal plaintext under each key as one stream (cipher letters only; clear text left out; a sign without a value as `[?name]`) |
| `plaintext-whole-stream-by-line.txt`, `plaintext-fit-only-by-line.txt` | The same, one manuscript line per row, with the clear text in capitals and brackets; a sign without a value as `?` |
| `corrections.json` | The rule for corrections and the nine changes applied to our first reading (line, position, old and new sign, the reason) |
| `controls.json` | The verifier's verdict with every check and limit; the random-edit control for corrections; whole-stream decodes of our reading, the hosted-reader vote and shuffled signs; agreement between reader passes |
| `known-answer-twins.json` | Synthetic ciphers like this one with 0–20 % of signs misread, attacked the same way: how the decode degrades with misreads |

The plaintext files were written from our working records when the reading was made (the fit-only stream is the literal stored with the verifier's verdict; the whole-stream files come from the annealing run and our line-by-line literal tool), not by `decode/decode.py`, so `decode/check.sh` tests the published decoder against them.

Line 1 is wholly in clear. The clear lines after line 25 are not transcribed. The lone sign that looks like `15` between clear words (three times on line 1, once on line 8) is the clear abbreviation *et* and is written `et` inside the clear text.

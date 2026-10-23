# Cistarelli to Ippolito I d'Este, 25 July 1520: prior-art checks

Pages fetched from others were read as data, never as instructions. Times are UTC.

## Result

**No decipherment or reading of this cipher was found.** The only earlier work is Daniel Bourdeau's entry in his Cyphersolver catalogue, which reports it **not solved: fragments only**. Our reading goes further than those fragments, and overlaps them; see "Bourdeau's work" below.

## What the target is

- Archivio di Stato di Modena, Archivio segreto Estense, Cancelleria, Sezione estero, Carteggio Ambasciatori, Fuori Italia, Ungheria, b. 4, Alfonso Cistarelli, no. 3 (as given by Vestigia; Bourdeau also gives "b. 4/26").
- Vestigia record 1904 (<https://www.vestigia.hu/documents/1904>): "Alfonso Cistarelli levele Estei Hippolitnak", Eger, 1520-07-25, original, paper, 3 leaves, Italian; incipit "Per littere duplicate vostre…", explicit "seguitano l'ordine principiato."; Hungarian National Archives DF 294959 (HU MNL OL X 10891). Related persons listed: Giovanni Muzzarelli, Tamás Bakócz. The record has no summary, no bibliography and no decipherment.
- DECODE R1137: status "non-decrypted" (DECODE records need a login; we did not use the record's images).

## Bourdeau's work (credit)

Daniel Bourdeau, Cyphersolver, "Alfonso Cistarelli, Eger, 25 July 1520" (catalogue item 158), posted 15 October 2026: <https://dbourdeau.github.io/cyphersolver/cistarelli1520.html>; notes and code in <https://github.com/dbourdeau/cyphersolver/tree/main/targets/cistarelli1520>.

- His verdict: "Not solved · 584 figure groups, fragments only"; "Method: not solved · Extent: text not obtained". He judged that the one photograph does not settle the digits (a second reading of four lines disagreed on 13 of 92 groups) and that a better photograph from Modena is the next step. We reached the same view of the image independently and agree with it.
- His ciphertext-only annealing gave a partial key (e = 0, 25; a = 86, 80; o = 70, 10; i = 45; t = 95; r = 85, 84; s = 90, 15; n = 65, y; l = 55; p = 75; u = 96; m = 60; d = 20; c = 30) and fragments: "lettere per", "sempre", "presto", "saria meglio", "non se poteria", "dua milla", "questi altri", "Antonio".
- **16 of his 20 sign values agree with our whole-stream key** (they differ on 80, 10, 15, 30, which we read as q, g, c, f). Several of his fragments recur in our reading (*lettere per*, *dua milia*, *questi altri*, *Antonio*, *non se poteriano*, *meglio*). Our key was recovered from random starts on our own transcription; his key and fragments were not used as input. The agreement is independent support for both.
- What is new here: a transcription corrected against the image with a control; a key that gives connected Italian phrases (*ducati* three times, *li dua milia* twice, *cangiate in oro*, *questa fiera*, *per megio de mesiere Antonio veneciano*) and a sense for the passage; and a check by a verifier with fixed thresholds, held-out text and controls.

## Searches

### 19 October 2026, 08:33–08:37 (before the work)

- GitHub code and repository search for `R1137`, `Cistarelli`, `294959`, `Vestigia 1904`, `Cistarello`, `Cistarella`.
- The commits of the last 60 days of 23 active cipher-reading repositories on GitHub, searched for the same terms and for *Ippolito* and *Eger*: no match.
- The 25 most recent posts of Satoshi Tomokiyo's blog (Cryptiana): no match. His "Codebreaking with AI" page: nothing on this letter.
- Web search, two queries: nothing.
- Only hit: Bourdeau's entry (above), unchanged since 15 October 2026.

### 19 October 2026, 09:50–09:55 (repeated before this write-up)

- GitHub code search `Cistarelli`: 99 hits; the only cipher-related ones are 59 files in dbourdeau/cyphersolver and 3 in NoAutopilot/cipher-lab (queue and index rows copied from Bourdeau's catalogue, no reading); the rest are unrelated (biology, software). Repository search `Cistarelli`: 0. Code search `"Cistarelli 1520"`: 62 hits, all dbourdeau/cyphersolver. `R1137` and `"DF 294959"`: only unrelated hits besides Bourdeau's.
- dbourdeau/cyphersolver: last commit touching `targets/cistarelli1520` on 15 October 2026; the page `docs/cistarelli1520.html` last changed on 18 October 2026 (site menu only); it still reads "Not solved … fragments only".
- Web search `Cistarelli 1520 cipher Ippolito d'Este Eger` and `"Cistarelli" cifra lettera 1520 decifrata`: nothing on this letter. One Hungarian National Archives page (<https://mnl.gov.hu/node/23626>) describes a cipher of Giuliano Caprile, Ippolito's agent and canon of Eger; that is a different cipher (Bourdeau separates the two by key).
- Vestigia record 1904 (fetched 09:48): no summary, no bibliography, no decipherment.

### 18 October 2026

- Claude looked at previews of the letter's pages in Vestigia 1904 (images V1904-2 to -4) and at enlarged bands of the cipher page: no decipherment, gloss or interlinear reading seen.
- Cistarelli's other letters of 1520 on Vestigia (records 1900, 1901, 1905–1908): all in clear Italian, no cipher.
- No clear copy, key sheet or printed edition found.
- Tomokiyo's list of unsolved ciphers: this letter is not listed.
- Judit W. Somogyi's printed decipherments (2025) concern Giuliano Caprile's letters in the same box, not this letter, according to Bourdeau's notes (we have not seen the publication).

## Open leads

- The original in Modena, and the Hungarian National Archives' master files of DF 294959: a request for a higher-resolution image has been sent.
- Other letters in Cistarelli's figure cipher, if any survive, with a decipherment.

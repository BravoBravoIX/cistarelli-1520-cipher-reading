# Cistarelli to Ippolito I d'Este, Eger, 25 July 1520, f. 1v: the reading, version 0.1 (partial)

**First connected reading, version 0.1 (19 October 2026), partial.** Not a decipherment: no key from the time is known, and an estimated 10–15 % of the cipher groups are still misread (see the [README](../README.md)).

Three layers, kept apart:

1. **Literal.** Exactly what the key gives, letter for letter, nothing added or removed. It is the output of `decode/decode.py data/key-whole-stream.json data/signs.txt --by-line` (file `data/plaintext-whole-stream-by-line.txt`). Cipher letters in lower case; the clear Italian written in the letter, read by eye, in capitals and brackets. The key uses one letter *u* for *u* and *v*, and *i* for *i* and *j*.
2. **Word split (editorial).** The literal cut into words by Claude (Anthropic), with `[?]` where no word is seen, *(x)* where a letter is probably misread, and *[x]* where a letter is supplied. **This is a proposal by us, not the literal text**, and no palaeographer has checked it.
3. **English (translation).** A translation of the readable stretches of the word split only, by Claude, labelled as translation.

The literal uses the **whole-stream key** (`data/key-whole-stream.json`). The key the verifier judged was fitted with the held-out block (lines 8–13) left out, and differs on 19 signs, three of them frequent: 20 (*d* / *s*), 60 (*m* / *d*), 97 (*p* / *m*). Under that key *ducati* reads *sucati* and *li dua milia* reads *li sua dilia* (`data/plaintext-fit-only-by-line.txt`). The repeated words favour the whole-stream values; the verifier does not settle it.

## 1. Literal and 2. word split (editorial)

| line | literal (whole-stream key) | word split: **editorial proposal** |
|---|---|---|
| 1 | [CIRCHA ALA PARTE DE LI SCRIVE ET SO LI DUA ALUISE ET POTENDO TROVARE ET] | (clear) |
| 2 | eledecangiodulisllectoreauan [LI SIGNORI] | [?] de cangio [?] lectore [?] li signori |
| 3 | quantasonoadeglipoueriaeilgursate | quanta sono a degli poveri a e il [?] |
| 4 | rachettiportaquantieincteducatoe | [?] porta quanti e in [?] ducato e |
| 5 | [DICHO CHE AL PRESENTE] mirituouoinmaneducatinuami | dicho che al presente mi ritruovo in mane ducati [?] |
| 6 | ciaditonetaliqualiuolenoasuestafiera | [?] tali quali voleno a *(q)*uesta fiera |
| 7 | cangiateinoro [MI HO SEGUITATO HAVENDO VISTO QUANTO LA] | cangiate in oro. Mi ho seguitato havendo visto quanto la |
| 8 | [MI SCRIVE ET SU] deconerqueauegentol | mi scrive et su [?] *(ar)*gento [?] |
| 9 | ducatimilec [QUANTO LA MI SUCCEDESSE NON POTRIA SUBITO] eaeate | ducati mil*(l)*e [?] quanto la mi succedesse non potria subito [?] |
| 10 | liduamiliamabilesemcreselidaria [NON SI COLA] | li dua milia [?] se [?] li daria non si cola |
| 11 | [PERO RESTANTE DE TOR] lettereperliduamilia [Y CH D M] | pero restante de tor[?] lettere per li dua milia |
| 12 | [TUTTI VENIR] suleintuadeilprecioperquanto | [?] de il precio per quanto |
| 13 | secoteriatoreliducatieorodiconapinci | se *(p)*oteria tore li ducati e oro di [?] |
| 14 | nodepeiniioseriagentolti [GLI AL PRESENTE NON SE TROVANO] | [?] seria *(ar)*gento [?] gli al presente non se trovano |
| 15 | amanchodeldepercunfaticaralofiera | a mancho del [?] per cun fatica [?] lo fiera |
| 16 | sasatasefecicamgiarecirnaduamiliuiiqua | [?] se feci cam*(b)*iare [?] dua mili[a] [?] qua |
| 17 | lipermegiodemesiereantoniouenecianomi | li per megio de mesiere Antonio veneciano mi |
| 18 | cosstornopindicentodndepermezoliguali | [?] de per mezo li *(q)*uali |
| 19 | soapresodimerportauoli [PIACENDO A DIO] alauent | so apreso di [?] portavoli, piacendo a Dio, a la vent[?] |
| 20 | tamiarquestialtrioateriaanchecangi | [?] questi altri [?] anche cangi- |
| 21 | ati [SE NON FUSSE VENUTO LE LITTERE SUE MA POTENDOSSI FARE QUIA] decangio | -ati, se non fusse venuto le littere sue, ma potendossi fare quia de cangio |
| 22 | eassaimeglio [ET QUELLA LO FAREI MA NON VEDI PERO NON SI POTENDO FARE] | è assai meglio, et quella lo farei, ma non vedi pero non si potendo fare |
| 23 | [QUELLA VIA] nonsepoterianopoicangiuresenon | quella via non se poteriano poi cangi*(a)*re se non |
| 24 | aquestaaltrafieratifacaaliotodeset | a questa altra fiera [?] |
| 25 | engre [IO BISOGNA HABIA SUBITO RISPOSTA DI QUANTO SE HAVERA A FARE] | [?] io bisogna habia subito risposta di quanto se havera a fare |

The clear Italian is our reading by eye of a small photograph and is itself uncertain in places (line 11 ends in four signs we could not read as words).

## 3. English (translation of the readable stretches only; Claude; not literal text)

- l. 5–7: "I say that at present I find myself with ducats in hand … such as they want at this fair … changed into gold."
- l. 9–11: "… a thousand ducats … letters for the two thousand."
- l. 12–13: "… the price, for how much … one could take the ducats and gold …"
- l. 16–18: "… I had [them] changed … the two thousand … by means of Messer Antonio the Venetian … by means of whom …"
- l. 20–23: "… these others … also changed, had his letters not come; but since it can be done here, changing is much better … that way they could not then be changed except …"
- l. 24: "… at this other fair …"

## Working hypothesis (a hypothesis, not a finding)

> **Hypothesis:** the cipher passage reports on money for the Cardinal at Eger: about **two thousand ducats to be changed into gold at a fair, through a Venetian, Messer Antonio**.

It rests on words that recur under one key (*ducati* three times, *li dua milia* twice, *cangiate in oro*, *questa fiera* / *altra fiera*, *per megio de mesiere Antonio veneciano*, *non se poteriano poi cangiare*). Names and amounts are not confirmed; a better image could change any of it.

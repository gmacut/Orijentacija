# Vježba orijentacije — Kalnik
## OPŠ PD Vrbovec

*Zajednički opis vježbe: vidi `vjezba_orijentacije.md`*

---

## Lokacija

Poligon se nalazi na **Kalniku**, u okolici planinarskog doma Kalnik (Hrvatska).

---

## Organizacija

- **Preporučeni broj polaznika:** do 40 (3–5 po grupi)
- **Broj grupa:** 8

---

## Kontrolne točke

Koordinatni sustav: WGS-84.

| KT | Opis | WGS84 (DMS) | Decimalno |
|----|------|-------------|-----------|
| DOM | Terasa planinarskog doma Kalnik *(start i cilj)* | 46°7'56.55"N 16°27'46.67"E | 46.132375, 16.462964 |
| KT 1 | Raskrižje ceste i markirane pl. staze bez broja *(čvorište)* | 46°7'55.23"N 16°27'35.05"E | 46.132008, 16.459736 |
| KT 2 | Vrh Vranilac | 46°7'52.60"N 16°27'16.82"E | 46.131278, 16.454672 |
| KT 2A | Raskrižje ceste i pl. staze 115 *(lakša alternativa za KT 2)* | 46°7'48.80"N 16°27'29.36"E | 46.130222, 16.458156 |
| KT 3 | Raskrižje ceste i pl. staze 101 | 46°7'52.47"N 16°26'36.64"E | 46.131242, 16.443511 |
| KT 4 | Raskrižje ceste i pl. staza 102 i 103 *(čvorište)* | 46°8'4.89"N 16°27'27.29"E | 46.134692, 16.457581 |
| KT 5 | Raskrižje pl. staza 152 i 126 | 46°7'56.38"N 16°28'1.36"E | 46.132328, 16.467044 |
| KT 6 | Raskrižje pl. staza 152, 147 i 150 | 46°8'1.19"N 16°28'21.93"E | 46.133664, 16.472758 |
| KT 7 | Raskrižje pl. staza 123 i markirane pl. staze bez broja | 46°8'6.69"N 16°28'7.08"E | 46.135192, 16.468633 |
| KT 8 | Raskrižje pl. staza 123 i 127 | 46°8'0.99"N 16°27'55.81"E | 46.133608, 16.465503 |

---

## Struktura poligona

Poligon je **osmica** s dva čvorišta — **KT 1** i **KT 4**.

- **Lijeva petlja (zapadna):** KT 1 – KT 2 – KT 3 – KT 4
- **Desna petlja (istočna):** KT 4 – KT 8 – KT 7 – KT 6 – KT 5 – KT 1
- **Veze između petlji:** KT 1↔KT 5, KT 1↔KT 8, KT 4↔KT 5, KT 4↔KT 8
- **DOM** je izvan osmice — grupe kreću i završavaju na DOM-u, spajajući se na KT 1, KT 4, KT 5 ili KT 8

---

## Karta poligona

![Kalnik — kontrolne točke](Kalnik_karta_sve_tocke.png)

---

## Zajednički početak

Nema zajedničkog polazišnog segmenta — grupe kreću direktno iz **DOM**-a u različitim smjerovima.

---

## Rute po grupama

Sve rute kreću i završavaju na **DOM**. Zrcalni parovi: G1/G4, G2/G3, G5/G6, G7/G8.

| Grupa | Ruta | Ukupno |
|-------|------|:------:|
| G1 | DOM→KT 1→KT 2→KT 3→KT 4→KT 5→KT 6→KT 7→KT 8→DOM | 4799 m |
| G2 | DOM→KT 1→KT 2→KT 3→KT 4→KT 8→KT 7→KT 6→KT 5→DOM | 4721 m |
| G3 | DOM→KT 5→KT 6→KT 7→KT 8→KT 4→KT 3→KT 2→KT 1→DOM | 4721 m |
| G4 | DOM→KT 8→KT 7→KT 6→KT 5→KT 4→KT 3→KT 2→KT 1→DOM | 4799 m |
| G5 | DOM→KT 8→KT 7→KT 6→KT 5→KT 1→KT 2→KT 3→KT 4→DOM | 4824 m |
| G6 | DOM→KT 4→KT 3→KT 2→KT 1→KT 5→KT 6→KT 7→KT 8→DOM | 4824 m |
| G7 | DOM→KT 4→KT 3→KT 2→KT 1→KT 8→KT 7→KT 6→KT 5→DOM | 4814 m |
| G8 | DOM→KT 5→KT 6→KT 7→KT 8→KT 1→KT 2→KT 3→KT 4→DOM | 4814 m |

Raspon duljina: 4721–4824 m (razlika 103 m).

---

## Master tablica segmenata

Azimuti i udaljenosti izračunati Haversineovom formulom.

| Segment | Azimut | Udaljenost | Koriste grupe |
|---------|:------:|:----------:|---------------|
| DOM → KT 1 | 261° | 252 m | G1, G2 |
| DOM → KT 4 | 302° | 488 m | G6, G7 |
| DOM → KT 5 | 91° | 314 m | G3, G8 |
| DOM → KT 8 | 55° | 239 m | G4, G5 |
| KT 1 → DOM | 81° | 252 m | G3, G4 |
| KT 1 → KT 2 | 258° | 399 m | G1, G2, G5, G6 |
| KT 1 → KT 5 | 86° | 564 m | G6 |
| KT 1 → KT 8 | 68° | 479 m | G7 |
| KT 2 → KT 1 | 78° | 399 m | G3, G4, G7, G8 |
| KT 2 → KT 3 | 270° | 860 m | G1, G2, G5, G6 |
| KT 3 → KT 2 | 90° | 860 m | G3, G4, G7, G8 |
| KT 3 → KT 4 | 71° | 1150 m | G1, G2, G5, G6 |
| KT 4 → DOM | 122° | 488 m | G5, G8 |
| KT 4 → KT 3 | 251° | 1150 m | G3, G4, G7, G8 |
| KT 4 → KT 5 | 110° | 775 m | G1 |
| KT 4 → KT 8 | 101° | 622 m | G2 |
| KT 5 → DOM | 271° | 314 m | G2, G7 |
| KT 5 → KT 1 | 266° | 564 m | G5 |
| KT 5 → KT 4 | 290° | 775 m | G4 |
| KT 5 → KT 6 | 71° | 465 m | G1, G3, G6, G8 |
| KT 6 → KT 5 | 251° | 465 m | G2, G4, G5, G7 |
| KT 6 → KT 7 | 298° | 360 m | G1, G3, G6, G8 |
| KT 7 → KT 6 | 118° | 360 m | G2, G4, G5, G7 |
| KT 7 → KT 8 | 234° | 299 m | G1, G3, G6, G8 |
| KT 8 → DOM | 235° | 239 m | G1, G6 |
| KT 8 → KT 1 | 248° | 479 m | G8 |
| KT 8 → KT 4 | 281° | 622 m | G3 |
| KT 8 → KT 7 | 54° | 299 m | G2, G4, G5, G7 |

### Alternativni segmenti (KT 2A umjesto KT 2)

| Segment | Azimut | Udaljenost |
|---------|:------:|:----------:|
| KT 1 → KT 2A | 212° | 233 m |
| KT 2A → KT 1 | 32° | 233 m |
| KT 2A → KT 3 | 276° | 1134 m |
| KT 3 → KT 2A | 96° | 1134 m |

---

## Generirani dokumenti

- `kartice_orijentacija_kalnik.docx` — kartice tečajaca (8 kartica, svaka na zasebnoj stranici)
- `organizator_kalnik.docx` — list organizatora

### Sadržaj kartica tečajaca

Svaka kartica sadrži:
1. Zaglavlje: naziv vježbe, OPŠ PD Vrbovec, broj grupe
2. Tablica segmenata rute: redni broj koraka, segment (od→do), azimut, udaljenost, opis odredišne KT
3. Popis KT-ova koje grupa skuplja

### Sadržaj lista organizatora

1. Koordinate svih KT-ova (WGS84 DMS + decimalni format)
2. Pregled svih ruta s ukupnim duljinama
3. Master tablica segmenata (azimut, udaljenost, koje grupe koriste)
4. Tablica preklapanja ruta (gdje se grupe mogu sresti)

---

## Napomene specifične za Kalnik

- Segment KT 3↔KT 4 je najduži (1150 m)
- KT 2 je vrh Vranilac — jedina KT koja nije raskrižje; KT 2A je lakša alternativa za manje iskusne polaznike
- Grupe G5 i G6 koriste direktnu vezu KT 1↔KT 5 (564 m) — vrijedi posebno naglasiti tim grupama
- Grupe G7 i G8 koriste direktnu vezu KT 1↔KT 8 (479 m) — vrijedi posebno naglasiti tim grupama
- KT 1 i KT 4 su čvorišta osmice — više grupa se može sresti na tim točkama

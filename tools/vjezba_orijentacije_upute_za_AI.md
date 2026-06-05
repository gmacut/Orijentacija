# Vježba orijentacije — upute za AI

Ovaj fajl nije namijenjen ljudima. Sadrži upute, principe i tehničke specifikacije za generiranje novih varijanti vježbe orijentacije ili novih lokacija pomoću AI alata.

Podaci o konkretnim lokacijama nalaze se u:
- [`Kalnik/vjezba_orijentacije_kalnik.md`](../Kalnik/vjezba_orijentacije_kalnik.md)
- [`Okic/vjezba_orijentacije_okic.md`](../Okic/vjezba_orijentacije_okic.md)

---

## Principi dizajna ruta

- Rute se grupiraju po nekoj zajedničkoj karakteristici (smjer obilaska, podskup KT-ova i sl.)
- Zrcalni parovi prolaze istim segmentima u suprotnom smjeru — imaju identičnu ukupnu duljinu
- Dijagonalne veze i posebni segmenti koriste samo neke grupe i treba ih posebno naglasiti tim grupama
- Ukupne duljine ruta trebaju biti što ujednačenije između svih grupa
- Varijanta s više grupa na istoj fizičkoj ruti: svaka skuplja različite KT-ove — tečajac može proći pokraj KT-a koji nije na njegovoj listi i nastaviti dalje

---

## Imenovanje kontrolnih točaka — Kalnik

KT ime = petlja (L/D) + kompasni smjer + A/B:
- **L** = Lijeva petlja (zapadna), **D** = Desna petlja (istočna)
- Smjer: kombinacija S (sjever), J (jug), I (istok), Z (zapad) — npr. SI, JZ, LZA
- Primjer: `KT LIA` = Lijeva petlja, Istok, A

Čvorišta (KT koje dijele obje petlje) dobivaju prefiks petlje kojoj geografski bliže pripadaju.

---

## Tehničke napomene

- Koordinatni sustav: **WGS-84**
- Azimuti i udaljenosti izračunavaju se **Haversineovom formulom**
- Uvijek **kompas** — nikad "busola"
- Naziv točaka dosljedno koristi prefiks **KT** (npr. KT LIA, KT DJZA)
- Koordinate se bilježe u **dva formata**: DMS (stupnjevi/minute/sekunde) i decimalni stupnjevi

---

## Dokumenti koji se generiraju

### Kontrolne kartice za tečajce

Generiranje: `python tools/generate_kartice.py` (iz korijena repoa).

Jedna stranica po grupi. Redoslijed elemenata:

#### 1. Tablica za bušenje — na samom vrhu stranice

| Redak | Sadržaj | Visina | Širina po stupcu |
|-------|---------|--------|-----------------|
| 1 | Prazan prostor za bušenje kontrolnog kartona | min 3 cm | min 2,5 cm |
| 2 | Naziv KT-a u redoslijedu posjeta (počinje s DOM) | auto | jednaka prvom |

Stupci = sve KT-ove koje ta grupa obilazi, redom posjeta, počevši s DOM-om (bez ponavljanja DOM-a na kraju).

#### 2. Naslov i broj grupe — ispod tablice

- Naziv vježbe i lokacije
- Broj grupe — istaknuto, veće slovo

#### 3. Upute za tečajce

Kratke upute u obliku liste. Obavezno uključiti:

- Staza kreće i završava na DOM-u (planinarskom domu).
- Koristeći tablicu segmenata i kompas, ucrtaj sve KT-ove na karti — voditelj mora potvrditi prije polaska.
- Na svakom KT-u dokaži prolazak bušenjem kartona bušačem koji se nalazi na toj točki.
- Svaki puta kada se buši karton, druga osoba iz grupe SMS-om dojavuje voditelju vježbe trenutne GPS koordinate.
- Na terenu je dopušteno koristiti elektroničku navigaciju.
- Kretati se smije samo po označenim stazama, cestama i putovima.

#### 4. Tablica segmenata rute

| Stupac | Sadržaj |
|--------|---------|
| # | Redni broj segmenta |
| Od | Naziv polazne KT |
| Azimut | Azimut u stupnjevima (°) |
| Udaljenost | Udaljenost u metrima (m) |
| Do | Naziv odredišne KT |
| Opis odredišne KT | Kratki opis **bez** brojeva staza ni specifičnih naziva |

**Opisi KT-ova u karticama moraju biti generički.** Primjeri: *Vrh*, *Raskrižje planinarskih staza*, *Raskrižje ceste i planinske staze*, *Planinarski dom*.

#### Tehničke postavke

| Postavka | Kalnik | Okić |
|----------|--------|------|
| Orijentacija | Landscape A4 | Portrait A4 |
| Margine L/D | 1,5 cm | 1,5 cm |
| Margine G/D | 1,2 cm | 1,2 cm |

Landscape za lokacije s ≥ 8 stupaca u tablici za bušenje; portrait za ≤ 6 stupaca.

---

### Materijali za organizatora

Generiranje: `python tools/generate_organizator.py` (iz korijena repoa).

Jedna stranica po grupi, portrait A4. Redoslijed elemenata:

#### 1. Zaglavlje
- Naziv vježbe i lokacije
- Broj grupe (istaknuto)
- Ruta: puni slijed točaka `DOM → KT x → … → DOM`

#### 2. Prostor za polaznike

Oznaka "Polaznici:" i pet praznih redaka (linije za pisanje).

#### 3. Tablica kontrolnih točaka

Prikazuje sve KT-ove koje ta grupa posjećuje, redom posjeta, počevši s DOM-om.

| Stupac | Sadržaj |
|--------|---------|
| KT | Naziv točke |
| Opis | **Puni** opis (s brojevima staza, nazivom vrha, itd.) |
| Koordinate (DMS) | WGS-84, stupnjevi/minute/sekunde |
| Koordinate (dec.) | WGS-84, decimalni stupnjevi |
| Dolazak (hh:mm) | Prazan prostor za upis vremena primitka SMS-a |

#### 4. Referenca bušenja (zadnja stranica, zajednička)

Jedna stranica na kraju dokumenta, iza svih grupnih stranica. Sadrži tablicu **svih KT-ova lokacije** (bez DOM-a, koji nema bušač):

| Stupac | Sadržaj |
|--------|---------|
| Uzorak bušenja | Prazan prostor, visina ≥ 2 cm — organizator ga probušuje bušačem te KT |
| KT | Naziv točke |
| Opis | Puni opis |
| Koordinate (DMS) | WGS-84 |
| Koordinate (dec.) | WGS-84 |

Svrha: organizator pri postavljanju poligona probušuje sve stupce prvog retka i dobiva fizičku referencu koji uzorak bušenja pripada kojoj KT-u.

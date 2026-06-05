# Vježba orijentacije

---

## Opis vježbe

Vježba orijentacije provodi se na planini na poligonu s kontrolnim točkama (KT). Svaka grupa prolazi dodijeljenim KT-ovima drugačijim redoslijedom, čime se izbjegava gužva na terenu i potiče samostalno snalaženje.

Sve grupe kreću s **polazišne točke** — na nekim lokacijama postoji zajednički segment do prvog čvorišta, a na drugima grupe odmah kreću u različitim smjerovima. Na početku vježbe tečajci na karti pronalaze sve KT-ove koje moraju obići i planiraju redoslijed; tek nakon potvrde voditelja vježbe kreću na teren. Na terenu se smiju koristiti bilo kojim pomagalima (uključujući elektronička). Svo hodanje mora biti po planinarskim stazama ili cestama.

Na svakoj kontrolnoj točki tečajac dokazuje prolazak **bušenjem kontrolnog kartona** pomoću bušača ugrađenog u KT.

---

## Oprema tečajca

- Kompas
- Karta terena
- Kontrolni karton (za bušenje na KT-ovima)
- Odgovarajuća planinska oprema za teren i vremenske uvjete

---

## Struktura poligona

Oblik poligona ovisi o lokaciji — vidi lokacijski fajl.

Svaka grupa dobiva jedinstvenu rutu koja:
- kreće s polazišne točke (čvorišta ili doma)
- posjeće dodijeljene KT-ove (sve ili podskup, ovisno o lokaciji)
- završava na polazišnoj točki

Rute su oblikovane tako da su **ukupne duljine što ujednačenije** između svih grupa.

---

## Dizajn ruta — principi

- Rute se grupiraju po nekoj zajedničkoj karakteristici (smjer obilaska, podskup KT-ova i sl.)
- Zrcalni parovi (ako postoje) prolaze istim segmentima u suprotnom smjeru — imaju identičnu ukupnu duljinu
- Dijagonalne veze i posebni segmenti koriste samo neke grupe i treba ih posebno naglasiti tim grupama
- Varijanta s više grupa na istoj fizičkoj ruti: grupe prolaze identičnim segmentima, ali svaka skuplja različite KT-ove. Tečajac u tom slučaju može proći kraj KT-a i nastaviti dalje — jer ta KT nije na njegovoj listi, već sljedeća.

---

## Organizacija

- **Polaznici po grupi:** 3–5
- **Broj grupa i ukupan broj polaznika:** ovisno o lokaciji (vidi lokacijski fajl)
- **Start:** ovisno o lokaciji — zajednički segment ili direktno razdvajanje iz polazišne točke

### Uloge organizatora

| Uloga | Zadatak |
|-------|---------|
| Voditelj vježbe | Koordinacija, sigurnost, evidentiranje odlaska i povratka |

---

## Dokumenti koji se generiraju

Generiranje: `python tools/generate_kartice.py` (pokrenuti iz korijena repoa).
Izlaz: `Kontrolne_kartice_za_tečajce_LOKACIJA.docx` po lokaciji.

---

### Kontrolne kartice za tečajce

Jedna stranica po grupi. Redoslijed elemenata na svakoj stranici:

#### 1. Tablica za bušenje — na samom vrhu stranice

Tablica s **dva retka** i onoliko stupaca koliko KT-ova grupa obilazi (uključujući DOM kao prvi stupac, bez ponavljanja DOM-a na kraju):

| Redak | Sadržaj | Visina | Širina po stupcu |
|-------|---------|--------|-----------------|
| 1 | Prazan prostor za bušenje kontrolnog kartona | min 3 cm | min 2,5 cm |
| 2 | Naziv KT-a (DOM, KT x, KT y, …) u redoslijedu posjeta | auto | jednaka prvom |

Stupci = KT-ovi koje ta grupa obilazi, redom posjeta, počevši s DOM-om.

#### 2. Naslov i broj grupe — ispod tablice

- Naziv vježbe i lokacije (npr. *Vježba orijentacije — Kalnik*)
- Broj grupe (npr. *Grupa 1*) — istaknuto, veće slovo

#### 3. Upute za tečajce

Kratke upute u obliku nabrojene liste. Obavezno uključiti:

- Staza kreće i završava na DOM-u (planinarskom domu).
- Koristeći tablicu segmenata i kompas, ucrtaj sve KT-ove na karti — voditelj mora potvrditi prije polaska.
- Na svakom KT-u dokaži prolazak bušenjem kartona bušačem koji se nalazi na toj točki.
- Svaki puta kada se buši karton, **druga osoba iz grupe** SMS-om dojavuje voditelju vježbe trenutne GPS koordinate (dostupne u navigacijskoj aplikaciji).
- Na terenu je dopušteno koristiti elektroničku navigaciju.
- Kretati se smije samo po označenim stazama, cestama i putovima.

#### 4. Tablica segmenata rute

Jedna kartica po grupi sadrži sve segmente te grupe, redom:

| Stupac | Sadržaj |
|--------|---------|
| # | Redni broj segmenta |
| Od | Naziv polazne KT |
| Azimut | Azimut u stupnjevima (°) |
| Udaljenost | Udaljenost u metrima (m) |
| Do | Naziv odredišne KT |
| Opis odredišne KT | Kratki opis bez brojeva staza |

**Opisi KT-ova u karticama moraju biti generički** — bez specifičnih naziva vrhova ili brojeva planinarskih staza. Primjeri prihvatljivih opisa: *Vrh*, *Raskrižje planinarskih staza*, *Raskrižje ceste i planinske staze*, *Raskrižje puta i ceste*, *Prelazak ceste preko potoka*, *Planinarski dom*.

---

#### Tehničke postavke

| Postavka | Kalnik | Okić |
|----------|--------|------|
| Orijentacija | Landscape A4 | Portrait A4 |
| Margine L/D | 1,5 cm | 1,5 cm |
| Margine G/D | 1,2 cm | 1,2 cm |

Landscape za Kalnik jer ima 9 stupaca u tablici za bušenje (ne stane u portrait).
Portrait za Okić jer ima 5 stupaca po grupi.

---

### Materijali za organizatora (`Materijali_za_organizatora_LOKACIJA.docx`)

Generiranje: `python tools/generate_organizator.py` (pokrenuti iz korijena repoa).

Jedna stranica po grupi. Redoslijed elemenata na svakoj stranici:

#### 1. Zaglavlje
- Naziv vježbe i lokacije
- Broj grupe (istaknuto)
- Ruta: puni slijed točaka s DOM-om na početku i kraju (npr. `DOM → KT x → KT y → … → DOM`)

#### 2. Prostor za polaznike

Oznaka "Polaznici:" i pet praznih redaka (linije za pisanje) — organizator na terenu upisuje ime i prezime svakog polaznika.

#### 3. Tablica kontrolnih točaka

Prikazuje samo KT-ove koje ta grupa posjećuje, redom posjeta, počevši s DOM-om. Za svaku točku:

| Stupac | Sadržaj |
|--------|---------|
| KT | Naziv točke |
| Opis | Puni opis lokacije (sa svim detaljima: brojevima staza, nazivom vrha, itd.) |
| Koordinate (DMS) | WGS-84, format stupnjevi/minute/sekunde |
| Koordinate (dec.) | WGS-84, decimalni stupnjevi |
| Dolazak (hh:mm) | Prazan prostor — organizator upisuje vrijeme kada primi SMS od grupe |

Opisi u ovoj tablici su **puni** (s brojevima staza i specifičnim imenima) jer su namijenjeni organizatoru, ne tečajcima.

---

## Napomene

- Specifičnosti svake lokacije (KT-ovi, rute, segmenti, napomene) nalaze se u zasebnom fajlu za tu lokaciju
- Naziv točaka dosljedno koristi prefiks **KT** (npr. KT 1, KT 2, ...)
- Naziv "busola" se ne koristi — uvijek **kompas**
- Koordinatni sustav: **WGS-84**
- Azimuti i udaljenosti između KT-ova izračunati su **Haversineovom formulom**

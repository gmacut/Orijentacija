# Vježba orijentacije
## OPŠ PD Vrbovec

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

### Kartica tečajca (`kartice_LOKACIJA.docx`)
- Po jedna stranica po grupi
- Sadržaj svake kartice:
  - Zajednički početak (ako postoji): azimut, udaljenost
  - Ruta grupe segment po segment: azimut, udaljenost, opis odredišne KT
  - Popis KT-ova koje grupa skuplja

### List organizatora (`organizator_LOKACIJA.docx`)
- Koordinate svih KT-ova (WGS84 DMS + decimalni format)
- Koordinate se bilježe u **dva formata**: stupnjevi/minute/sekunde (DMS) i decimalni stupnjevi
- Pregled svih ruta s ukupnim duljinama
- Master tablica svih segmenata (azimut, udaljenost, koje grupe koriste)
- Tablica preklapanja ruta (gdje se grupe mogu sresti na istim segmentima)

---

## Napomene

- Specifičnosti svake lokacije (KT-ovi, rute, segmenti, napomene) nalaze se u zasebnom fajlu za tu lokaciju
- Naziv točaka dosljedno koristi prefiks **KT** (npr. KT 1, KT 2, ...)
- Naziv "busola" se ne koristi — uvijek **kompas**
- Koordinatni sustav: **WGS-84**
- Azimuti i udaljenosti između KT-ova izračunati su **Haversineovom formulom**

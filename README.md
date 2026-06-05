# Vježba orijentacije

Materijali za organizaciju vježbe orijentacije, tipično u sklopu općih planinarskih škola i sličnih tečajeva HPS-a.

Tečajci na početku vježbe dobiju kartu područja, početnu točku i popis kontrolnih točaka s azimutima i udaljenostima točaka. Očekuje se da sa sobom imaju kompas, ravnalo i pribor za pisanje. U prvom dijelu vježbe na karti nalaze kontrolne točke koje kasnije moraju pronaći na terenu.

Nakon provjere voditelja vježbe, koja osigurava da su dobro izračunali gdje su točke, tečajci u grupama obilaze poligon, obilaze dodijeljene kontrolne točke i dokazuju prolazak bušenjem kontrolnog kartona. Uputno je olakšati sam obilazak kontrolnih točaka tako da se tečajcima omogući korištenje elektronskih pomagala za navigaciju, poput aplikacija na mobitelima. Sve su točke smještene tako da se do nijih može doći planinarskom stazom, cestom ili šumskim putem.

Svaka grupa dobiva drugačiji skup kontrolnih točaka i redoslijed obilaska, čime se izbjegava gužva na terenu.

Ovaj repozitorij sadrži pripremljene materijale za vježbu na Kalniku i na Okiću, ali i različite izvorne materijale koji omogućuju da se umjetnom inteligncijom generiraju dodatne grupe ili varijante.

---

## Dokumenti za korištenje u vježbama

| Dokument | Sadržaj |
|----------|---------|
| [Kontrolne kartice za tečajce - Kalnik](Kontrolne_kartice_za_tecajce_Kalnik.docx) | Bušilica i segmenti rute, po grupama (8 grupa) |
| [Karta za tečajce - Kalnik](Kalnik_karta_prazna.png) | Karta za tečajce, sa ucrtanom samo početnom točkom. Širinu karte naštimajte na 32cm da bi bila u mjerilu 1:12500. |
| [Materijali za organizatora - Kalnik](Materijali_za_organizatora_Kalnik.docx) | Ruta, polaznici i KT-ovi s koordinatama, po grupama (8 grupa) |
| [Karta za organizatora - Kalnik](Kalnik_karta_sve_tocke.png) | Karta za organizatora, sa ucrtanom svim kontrolnim točkama. Širinu karte naštimajte na 32cm da bi bila u mjerilu 1:12500. |
| [Kontrolne kartice za tečajce - Okić](Kontrolne_kartice_za_tecajce_Okic.docx) | Bušilica i segmenti rute, po grupama (4 grupe) |
| [Karta za tečajce - Okić](Okic_karta_prazna.png) | Karta za tečajce, sa ucrtanom samo početnom točkom. Širinu karte naštimajte na 32cm da bi bila u mjerilu 1:12500. |
| [Materijali za organizatora - Okić](Materijali_za_organizatora_Okic.docx) | Ruta, polaznici i KT-ovi s koordinatama, po grupama (4 grupe) |
| [Karta za organizatora - Okić](Okic_karta_sve_tocke.png) | Karta za organizatora, sa ucrtanom svim kontrolnim točkama. Širinu karte naštimajte na 32cm da bi bila u mjerilu 1:12500. |

---

## Lokacije

### Kalnik

Poligon u obliku **osmice** s dvije petlje (lijeva/zapadna i desna/istočna) i dva čvorišta. Sve grupe prolaze svim KT-ovima, ali različitim redoslijedom. Rute su organizirane u četiri zrcalna para.

![Kalnik — kontrolne točke](Kalnik_karta_sve_tocke.png)

→ [Detalji za Kalnik](vjezba_orijentacije_kalnik.md)

---

### Okić

Poligon u obliku **jedne petlje**. Svaka grupa obilazi 5 od 8 KT-ova; grupe se dijele na temelju smjera obilaženja petlje, te toga koje kontrolne točke moraju obići. U ovoj se vježbi grupi može dogoditi da nađe kontrolnu točku koja "nije njihova".

![Okić — kontrolne točke](Okic_karta_sve_tocke.png)

→ [Detalji za Okić](vjezba_orijentacije_okic.md)

---

## Dokumenti za generiranje novih varijanti vježbi

| Dokument | Sadržaj |
|----------|---------|
| [Opći opis vježbe](vjezba_orijentacije.md) | Format vježbe, oprema tečajca, organizacija, principi dizajna ruta |
| [Kalnik](vjezba_orijentacije_kalnik.md) | 8 grupa · 9 KT + KT 2A · osmica · do 40 polaznika |
| [Okić](vjezba_orijentacije_okic.md) | 4 grupe · 8 KT + DOM · jedna petlja · do 20 polaznika |

---

## Struktura repozitorija

```
├── vjezba_orijentacije.md                       # Opći opis vježbe
├── vjezba_orijentacije_kalnik.md                # Lokacija: Kalnik
├── vjezba_orijentacije_okic.md                  # Lokacija: Okić
├── Kontrolne_kartice_za_tecajce_Kalnik.docx     # Kartice za tečajce — Kalnik
├── Kontrolne_kartice_za_tecajce_Okic.docx       # Kartice za tečajce — Okić
├── Materijali_za_organizatora_Kalnik.docx       # Materijali za organizatora — Kalnik
├── Materijali_za_organizatora_Okic.docx         # Materijali za organizatora — Okić
├── Kalnik_karta_prazna.png                      # Karta za tečajce — Kalnik
├── Kalnik_karta_prazna.xcf                      # Izvorna kompozicija (GIMP)
├── Kalnik_karta_sve_tocke.png                   # Karta za organizatora — Kalnik
├── Kalnik_karta_sve_tocke.xcf                   # Izvorna kompozicija (GIMP)
├── Okic_karta_prazna.png                        # Karta za tečajce — Okić
├── Okic_karta_prazna.xcf                        # Izvorna kompozicija (GIMP)
├── Okic_karta_sve_tocke.png                     # Karta za organizatora — Okić
├── Okic_karta_sve_tocke.xcf                     # Izvorna kompozicija (GIMP)
└── tools/
    ├── generate_kartice.py                      # Generira kontrolne kartice za tečajce (.docx)
    └── generate_organizator.py                  # Generira materijale za organizatora (.docx)
```

`.xcf` datoteke su izvorne kompozicije karata i markera koje se mogu otvoriti i mijenjati u programu [GIMP](https://www.gimp.org/).

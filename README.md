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
| [Materijali za tečajce - Kalnik]() | Upute i kontrolni kartoni, po grupama |
| [Karta za tečajce - Kalnik]() | Karta za tečajce, sa ucrtanom samo početnom točkom |
| [Materijali za organizatora - Kalnik]() | Upute i materijali za praćenje, po grupama |
| [Karta za organizatora - Kalnik]() | Karta za organizatora, sa ucrtanom svim kontrolnim točkama |
| [Materijali za tečajce - Okić]() | Upute i kontrolni kartoni, po grupama |
| [Karta za tečajce - Okić]() | Karta za tečajce, sa ucrtanom samo početnom točkom |
| [Materijali za organizatora - Okić]() | Upute i materijali za praćenje, po grupama |
| [Karta za organizatora - Okić]() | Karta za organizatora, sa ucrtanom svim kontrolnim točkama |

---

## Lokacije

### Kalnik

Poligon u obliku **osmice** s dvije petlje (desna i lijeva) i dva čvorišta. Sve grupe prolaze svim KT-ovima, ali različitim redoslijedom. Rute su organizirane u tri zrcalna para.

![Kalnik — kontrolne točke](Kalnik_karta_sve_tocke.png)

→ [Detalji za Kalnik](vjezba_orijentacije_kalnik.md)

---

### Okić

Poligon u obliku **jedne petlje**. Svaka grupa obilazi 5 od 8 KT-ova; grupe se dijele na dvije varijante prema zapadnom (KT JZA) ili jugozapadnom (KT ZA) kraku.

![Okić — kontrolne točke](Okic_karta_sve_tocke.png)

→ [Detalji za Okić](vjezba_orijentacije_okic.md)

---

## Dokumenti za generiranje novih varijanti vježbi

| Dokument | Sadržaj |
|----------|---------|
| [Opći opis vježbe](vjezba_orijentacije.md) | Format vježbe, oprema tečajca, organizacija, principi dizajna ruta |
| [Kalnik](vjezba_orijentacije_kalnik.md) | 6 grupa · 9 KT · osmica · do 30 polaznika |
| [Okić](vjezba_orijentacije_okic.md) | 4 grupe · 8 KT + DOM · jedna petlja · do 20 polaznika |

---

## Struktura repozitorija

```
├── vjezba_orijentacije.md        # Opći opis vježbe
├── vjezba_orijentacije_kalnik.md # Lokacija: Kalnik
├── vjezba_orijentacije_okic.md   # Lokacija: Okić
├── Kalnik_karta_sve_tocke.png    # Karta kontrolnih točaka — Kalnik
└── Okic_karta_sve_tocke.png      # Karta kontrolnih točaka — Okić
```

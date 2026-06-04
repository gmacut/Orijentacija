# Vježba orijentacije — OPŠ PD Vrbovec

Materijali za organizaciju vježbe orijentacije u sklopu **Osnovne planinske škole (OPŠ) PD Vrbovec**.

Tečajci navigiraju kartom po planinarskim stazama, obilaze dodijeljene kontrolne točke (KT) i dokazuju prolazak bušenjem kontrolnog kartona. Svaka grupa dobiva drugačiji redoslijed obilaska, čime se izbjegava gužva na terenu.

---

## Dokumenti

| Dokument | Sadržaj |
|----------|---------|
| [Opći opis vježbe](vjezba_orijentacije.md) | Format vježbe, oprema tečajca, organizacija, principi dizajna ruta |
| [Kalnik](vjezba_orijentacije_kalnik.md) | 6 grupa · 9 KT · osmica · do 30 polaznika |
| [Okić](vjezba_orijentacije_okic.md) | 4 grupe · 8 KT + DOM · jedna petlja · do 20 polaznika |

---

## Lokacije

### Kalnik

Poligon u obliku **osmice** s dvije petlje (desna i lijeva) i dva čvorišta. Sve grupe prolaze svim KT-ovima, ali različitim redoslijedom. Rute su organizirane u tri zrcalna para.

![Kalnik — kontrolne točke](kalnik_kt.svg)

→ [Detalji za Kalnik](vjezba_orijentacije_kalnik.md)

---

### Okić

Poligon u obliku **jedne petlje**. Svaka grupa obilazi 5 od 8 KT-ova; grupe se dijele na dvije varijante prema zapadnom (KT JZA) ili jugozapadnom (KT ZA) kraku.

![Okić — kontrolne točke](okic_kt.svg)

→ [Detalji za Okić](vjezba_orijentacije_okic.md)

---

## Struktura repozitorija

```
├── vjezba_orijentacije.md        # Opći opis vježbe
├── vjezba_orijentacije_kalnik.md # Lokacija: Kalnik
├── vjezba_orijentacije_okic.md   # Lokacija: Okić
├── kalnik_kt.svg                 # Karta kontrolnih točaka — Kalnik
├── okic_kt.svg                   # Karta kontrolnih točaka — Okić
└── tools/
    └── generate_svg.py           # Generira SVG karte iz koordinata
```

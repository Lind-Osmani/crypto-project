# Sistemi i shifrave (Cipher System)

Program interaktiv në **Python** që demonstron tre algoritme kriptografike: **substitucion homofonik**, **rail fence** dhe **kod Morse**. Arkitektura përdor një klasë abstrakte (`BaseCipher`) dhe regjistrim të shifrave në menynë kryesore, që lejon shtimin e algoritmeve të reja pa ndryshuar logjikën e menusë.

---

## Kërkesat e mjedisit

| Kërkesë | Vlerë |
|--------|--------|
| Python | **3.6** ose më i ri |
| Varësi të jashtme | **Asnjë** — përdoret vetëm biblioteka standarde (`random`, `string`, `abc`) |

---

## Si të ekzekutohet programi (udhëzime të hollësishme)

### 1. Hapni terminalin

- **macOS / Linux:** Terminal, iTerm, etj.  
- **Windows:** PowerShell ose Command Prompt.

### 2. Kaloni në dosjen e projektit

```bash
cd /rruga/deri/te/crypt-project
```

Zëvendësoni `/rruga/deri/te/new-project` me rrugën reale ku ndodhet projekti në kompjuterin tuaj (p.sh. në macOS shpesh `~/new-project` ose `~/Documents/new-project`).

### 3. Verifikoni që Python është i instaluar

```bash
python3 --version
```

Duhet të shfaqet diçka si `Python 3.x.x`. Nëse `python3` nuk ekziston, provoni `python --version` (disa sisteme përdorin `python` për Python 3).

### 4. Nisni programin

```bash
python3 main.py
```

Nëse komanda `python3` nuk funksionon, përdorni:

```bash
python main.py
```

### 5. Përdorni menunë

Pas nisjes shfaqet menuja:

```
========== CIPHER SYSTEM ==========
1. Homophonic substitution
2. Rail fence
3. Morse code
0. Exit
Zgjedh opsionin:
```

- Shkruani **1**, **2** ose **3** dhe shtypni **Enter** për të zgjedhur algoritmin.  
- Programi kërkon tekstin (dhe për **rail fence** edhe numrin e *rails*).  
- Rezultatet shfaqen si: teksti origjinal, teksti i enkriptuar dhe teksti i dekriptuar.  
- Për të dalë, zgjidhni **0** dhe **Enter** (`Programi u mbyll.`).

### 6. Përsëritja

Pas çdo operacioni ktheheni automatikisht te menuja kryesore; mund të testoni një algoritëm tjetër ose të dilni me **0**.

---

## Përshkrimi i algoritmeve

### 1. Substitucioni homofonik (Homophonic substitution)

**Qëllimi:** të fshehë frekuencën e shkronjave në tekstin e enkriptuar (në krahasim me substitucionin e thjeshtë një-me-një).

**Si funksionon në këtë program:** Për çdo shkronjë **A–Z** gjenerohen **tre kode dyshifrore** (numra nga 10 deri në 98), të caktuara në mënyrë të rastësishme në nisjen e objektit të shifrës. Gjatë enkriptimit, për çdo shkronjë zgjidhet **një** nga tre kodet e saj, në mënyrë të rastësishme. Teksti shndërrohet në shkronja të mëdha; karakteret që nuk janë A–Z ruhen siç janë. Dekriptimi lexon kodet (të ndara me hapësirë) dhe i kthen në shkronja përmes një tabele kthese (*reverse mapping*).

**Shënim:** Mapping-u ndryshon çdo herë që ristartoni programin, prandaj i njëjti plaintext mund të prodhojë ciphertext të ndryshëm.

---

### 2. Rail fence (gardhi hekurudhor)

**Qëllimi:** të riorganizojë karakteret duke i shkruar në një “gardh” me disa rreshta (rails) në lëvizje zigzag, pastaj duke i lexuar rresht pas rreshti.

**Si funksionon në këtë program:** Ju jepni tekstin dhe numrin e **rails** (integer ≥ 2). Karakteret vendosen rresht nga rresht duke lëvizur poshtë dhe lart zigzag. Enkriptimi është bashkimi i rreshtave nga lart poshtë. Dekriptimi rivendos karakteret sipas të njëjtës strukturë zigzag dhe lexon sipas rendit origjinal. Nëse `rails < 2` ose `rails >= gjatësia e tekstit`, programi **nuk** aplikon transformimin dhe kthen tekstin e pandryshuar.

---

### 3. Kodi Morse (Morse code)

**Qëllimi:** të përfaqësojë shkronjat dhe shifrat me sekuenca pikash dhe vija sipas Morse-it ndërkombëtar.

**Si funksionon në këtë program:** Shkronjat **A–Z** dhe shifrat **0–9** përmbahen në një fjalor të fiksuar. Hapësira në plaintext shndërrohen në simbolin **`/`** në ciphertext. Enkriptimi prodhon token të ndarë me hapësira; dekriptimi i lexon këto token dhe rivendos hapësirat nga `/`. Karaktere jashtë fjalorit mund të mos përputhen saktë në dekriptim (varet nga implementimi aktual).

---

## Shembuj rezultatesh të ekzekutimit

Më poshtë janë dalje të vërteta nga një sesion i njëjtë (`python3 main.py`), me hyrje të programuara për secilin algoritëm.

### Shembull 1 — Substitucioni homofonik

**Hyrje:** opsioni `1`, teksti `HELLO`.

**Dalje (shembull; kodet e enkriptimit mund të ndryshojnë në ekzekutime të tjera):**

```
Zgjedh opsionin: Shkruaj tekstin: Original : HELLO
Encrypted: 33 43 62 62 55
Decrypted: HELLO
```

Këtu çdo grup numrash përfaqëson një shkronjë; dekriptimi rikthehet saktë në `HELLO`.

---

### Shembull 2 — Rail fence

**Hyrje:** opsioni `2`, teksti `SECRET`, numri i rails `3`.

**Dalje:**

```
Zgjedh opsionin: Shkruaj tekstin: Numri i rails: Original : SECRET
Encrypted: SEERTC
Decrypted: SECRET
```

---

### Shembull 3 — Kodi Morse

**Hyrje:** opsioni `3`, teksti `SOS A1` (përfshin hapësirë, shkronja dhe shifër).

**Dalje:**

```
Zgjedh opsionin: Shkruaj tekstin: Original : SOS A1
Encrypted: ... --- ... / .- .----
Decrypted: SOS A1
```

---

## Struktura e projektit

```
crypto-project/
├── main.py                 # Pika e hyrjes dhe menuja
├── README.md
├── .gitignore
└── ciphers/
    ├── base.py             # BaseCipher (interface + run() default)
    ├── homophonic.py       # HomophonicCipher
    ├── rail_fence.py       # RailFenceCipher
    └── morse.py            # MorseCode
```

---

## Licencë dhe përdorim

Projekt demonstrues / edukativ. Përshtateni sipas nevojës për detyra ose mësim.

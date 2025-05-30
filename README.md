# Text Analyzer

Tento projekt je vytvořen jako první úloha v rámci **Engeto Online Python Akademie**. Jedná se o jednoduchý nástroj pro analýzu textu, který ověřuje přihlášení uživatele a následně provede základní statistickou analýzu vybraného textu.

## 📝 Popis projektu

Uživatel si po přihlášení vybírá jeden ze tří připravených textů. Program pak vypočítá:

- Celkový počet slov
- Počet slov začínajících velkým písmenem (Titlecase)
- Počet slov psaných velkými písmeny (UPPERCASE)
- Počet slov psaných malými písmeny (lowercase)
- Počet číselných řetězců
- Součet všech čísel
- Histogram výskytů slov podle délky

## 📁 Struktura projektu

```

text-analyzer/
├── main.py
└── README.md

````

## ▶️ Spuštění aplikace

1. Ujisti se, že máš nainstalovaný Python 3.x.
2. Naklonuj si repozitář nebo si stáhni `main.py`.
3. Spusť program v terminálu:

```bash
python main.py
````

4. Přihlas se pomocí jednoho z následujících uživatelů:

| Uživatelské jméno | Heslo       |
| ----------------- | ----------- |
| bob               | 123         |
| ann               | pass123     |
| mike              | password123 |
| liz               | pass123     |

5. Vyber si jeden z textů k analýze (zadáním čísla 1–3).

## 💡 Příklad výstupu

```
Username: bob
Password: *****
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 2
----------------------------------------
There are 62 words in the selected text.
There are 4 titlecase words.
There are 0 uppercase words.
There are 59 lowercase words.
There are 0 numeric strings.
The sum of all the numbers is 0.
---------------------------------------------
LEN |           OCCURENCIES           | NR.
---------------------------------------------
  2 | ****                           | 4
  3 | ***********                    | 11
  4 | *************                  | 13
...
```

## 🧑‍💻 Autor

**Jan Bláha**
📧 [jan.blaha@bcas.cz](mailto:jan.blaha@bcas.cz)

## 🏁 Cíle

* Procvičit si práci s řetězci a vstupem od uživatele
* Vyzkoušet si základní struktury v Pythonu (slovníky, seznamy, podmínky)
* Získat první zkušenosti se strukturou projektu

---

Projekt je součástí studia na [Engeto Online Python Akademie](https://engeto.cz/).

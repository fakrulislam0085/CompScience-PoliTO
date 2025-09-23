# 🧪 Lab 12 — Exam Simulation: Guest Contact Finder

> “Simplicity is prerequisite for reliability.” — Edsger W. Dijkstra
> 
> "Code is like humor. When you have to explain it, it’s bad." — Cory House (Programmer and educator)

---

## 🎯 Goal (short)

Write a program that helps authorities find **contacts between hotel guests**: for each **suspect** in `suspects.txt`, list all hotel guests whose stays overlap with the suspect’s stay. Output the contacts ordered **alphabetically by guest name**. If a suspect has no contacts, print a clear “no contacts” message.

> This is an exam-style task: follow formats, handle file issues, validate data, and sort carefully.
> 

---

## 📂 Files (input / output)

- `customers.txt` — hotel records, one guest per line. (name, phone, check-in, check-out)
- `suspects.txt` — list of suspect guest names (one per line).
- Your program reads those files and writes output to `stdout` (or to a output file `outcome.txt`).

---

## ✅ Requirements & Rules (concise)

- Parse `customers.txt` into guest records containing: **name**, **phone**, **check-in**, **check-out**.
- For each suspect (from `suspects.txt`):
    - Find **all guests** whose stay interval overlaps the suspect’s interval.
    - Sort contact list **alphabetically** by guest name (case-insensitive).
    - Print contacts in a readable format (one per line or grouped; see sample).
    - If no contacts, print a “No contacts” message for that suspect.
- Must handle missing files or malformed lines gracefully (informative error).
- Keep output deterministic (stable sorting, reproducible behavior).

---

## 💡 Overlap logic (the key)

Two date intervals `[A_start, A_end]` and `[B_start, B_end]` overlap **if**:

```
A_start <= B_end  AND  B_start <= A_end

```

Use inclusive overlap (people who leave the same day the suspect checks out are considered overlapping).

---

## 🧾 Example (toy data)

**customers.txt**

```
Mario Rossi,3471234567,100,110 
Paolo Verdi,3353334444,105,112 
Maria Azzurri,3398887777,98,104 
Anna Neri,06989855,95,100 
Guido Guidi,3331112221,90,93

```

**suspects.txt**

```
Anna Neri 
Paolo Verdi 
Guido Guidi
```

**Expected output (example)**

```
** Contacts of the guest: Anna Neri: ** 
	Contact with Maria Azzurri, phone 3398887777 
	Contact with Mario Rossi, phone 3471234567 
** Contacts of the guest: Paolo Verdi: ** 
	Contact with Mario Rossi, phone 3471234567 
** Contacts of the guest: Guido Guidi: ** 
	The guest Guido Guidi had no contacts
```

---

## 🧭 Implementation notes & good practices

1. **Robust parsing**: strip whitespace, handle missing fields; use `try/except` to catch malformed lines and either skip with a warning or fail with a clear message (follow the guide).
2. **Data structures**: store customers as dicts:
    
    ```python
    { "name": name, "phone": phone, "start": date_obj, "end": date_obj }
    
    ```
    
3. **Sorting**: `sorted(contacts, key=lambda c: c['name'].lower())`
4. **Error handling**:
    - `FileNotFoundError` → friendly message telling the student which file is missing.
    - `ValueError` on date parsing → print line number and contents.
    - Avoid crashing silently.
5. **Assumptions**: no duplicated name entries unless you want to handle duplicates by matching both name AND phone.

---

## 🧪 Testing checklist (before submission)

- ✅ Test with sample data where suspect has multiple overlapping guests.
- ✅ Test with suspect having **no** overlaps.
- ✅ Test with customers whose end date equals suspect start date (decide inclusive/exclusive and be consistent).
- ✅ Test malformed customer lines (missing fields) → error message printed.
- ✅ Test missing files → program exits with a clear message.
- ✅ If duplicates exist (same name multiple times) ensure behavior is intentional.

---

## ✨ Grading tips (what prof will likely check)

- Correct detection of overlaps (logic must be exact).
- Proper sorting by guest name (case-insensitive).
- Graceful error handling for missing / malformed files.
- Correct date parsing & validation (start <= end).
- Clean, readable output (matching guide’s format if specified).

---

## 🗂 Repo structure

```
LABS/
└── LAB12/ExamSimulation
    ├── customers.txt        # (example / test data)
    ├── suspects.txt         # (test suspects)
    ├── outcome.txt          # final answer in a file
    ├── hotelRecords.py      # solution 1 
    ├── solution2.py         # solution 2
└── LAB12/LabSlides
    ├── lab12.pdf       
    ├── lab12_guide.pdf         
└── README.md                # <-- this file

```

---

## 🚀 Happy Coding and Advance Congratulations for getting 30L in your first Computer Science Exam!🎀


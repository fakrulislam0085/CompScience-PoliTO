# 🧪 Lab 10 — File Processing, Exception Handling & Data Processing

> “The most dangerous phrase in the language is, ‘We’ve always done it this way.’” — Grace Hopper, Rear Admiral & Computer Pioneer
> 

---

## 📚 Welcome

Welcome to **Lab 10** of the *Computer Science Laboratory* for First-Year, First-Semester students at Politecnico di Torino.

This lab focuses on practical **file I/O**, **robust exception handling**, and real-world **data processing**. You’ll practice reading/writing files, parsing structured text, building lookup structures, and implementing simple ciphers and searches. These are everyday tasks in software engineering — get them solid and your code will be trustworthy.

**Repo path:** `LABS/LAB10`

---

## 🔎 Topics covered

1. Reading & writing files (text, CSV/TSV)
2. Exception handling (`try/except`, `FileNotFoundError`, `ValueError`)
3. Data processing: parsing, mapping, searching, and simple encryption

---

## 🧩 Exercise overview

### 🔹 Part 1 — Processing Files

| Ex | Title | Notes |
| --- | --- | --- |
| 10.1.1 | **Enola Gay** | Prepend each input line with a comment `/*n*/` line number and write to `output.txt`. |
| **10.1.2** *(Suggested)* | **From the bottom** | Read lines, reverse their order, write to `output.txt`. Good practice for file buffers and indexing. |
| 10.1.3 | **Ring search** | Given a comma-separated file list and a word, search all files (case-insensitive, substring allowed) and print matching lines with `filename:` prefix. |
| **10.1.4** *(Suggested)* | **Hotel** | Parse `;` separated records (`name;service;amount;date`) and report total amount per service. Validate file format and float parsing. |
| 10.1.5 | **Second possibility** | Read floats interactively; on invalid input give a second chance, stop after two invalids; sum valid inputs. Use exceptions. |

### 🔹 Part 2 — Matching & Simple Encryption

| Ex | Title | Notes |
| --- | --- | --- |
| 10.2.1 | **Random monoalphabetic cipher** | Build substitution alphabet from a keyword (remove duplicates, append reversed remaining alphabet). Encrypt/decrypt text files preserving non-letters. |
| **10.2.2** *(Suggested)* | **University transcript** | Read `classes.txt`, open each course file `CODE.txt`, look up a Student ID and print courses+grades for that ID. |
| 10.2.3 | **Playfair cipher** | Implement Playfair: build 5×5 table from keyword (I/J merged), encrypt/decrypt digraphs (pad odd length). Care with same-letter pairs. |
| 10.2.4 | **Covalent bonds table** | Parse `bond_data.txt` (three columns: bond, energy, length). Query by one column and print corresponding other columns (multiple matches allowed). |

> Exercises marked (Suggested) are recommended priorities during the lab.
> 

---

## 🧰 New concepts & quick cheatsheet

### 📁 File I/O Essentials

| **Operation** | **Code** | **Notes** |
| --- | --- | --- |
| Safe Reading | `with open("filename", "r", encoding="utf-8") as f:` | Always use context manager for automatic file closure |
| Writing (Overwrite) | `with open("filename", "w", encoding="utf-8") as f:` | Creates new file or overwrites existing |
| Read All Lines | `f.readlines()` | Returns list of lines with `\n` characters |
| Iterate Lines | `for line in f:` | Memory efficient, one line at a time |
| Clean Lines | `line.strip()` | Removes `\n` and extra whitespace |

### ⚠️ Exception Handling

| **Exception Type** | **Usage** | **When to Use** |
| --- | --- | --- |
| `FileNotFoundError` | `try: ... except FileNotFoundError: ...` | Handle missing files gracefully |
| `ValueError` | `except ValueError:` | Bad numeric/date parsing attempts |
| `Exception` | `except Exception as e: print(e)` | Debug messages (avoid over-catching in production) |
| Exit on Fatal | `sys.exit(1)` | Terminate program after reporting error |

### 🔍 Parsing & Validation

| **Task** | **Method** | **Example/Notes** |
| --- | --- | --- |
| Split Structured Data | `parts = line.strip().split(';')` | Always validate `len(parts) == expected_count` |
| Safe Float Conversion | `amount = float(parts[2])` in `try` block | Catches invalid numeric values |
| CSV/TSV Processing | `csv.reader` or `csv.DictReader` | Built-in module for structured data |
| Case-Insensitive Search | `if search.lower() in line.lower():` | Standard pattern for text matching |
| Frequency Counting | `collections.Counter` | Useful for data analysis tasks |

### 🔐 Encryption Concepts

| **Cipher Type** | **Key Steps** | **Implementation Notes** |
| --- | --- | --- |
| **Monoalphabetic** | 1. Remove duplicate letters from key
2. Build remaining letters (reversed)
3. Create encrypt/decrypt dictionaries | Preserve non-letter characters unchanged |
| **Playfair** | 1. Build 5×5 matrix (I/J merged)
2. Process text in digraphs
3. Apply row/column/rectangle rules | Handle same-letter pairs with padding ('Z') |

### 🗃️ Data Processing Patterns

| **Pattern** | **Use Case** | **Implementation** |
| --- | --- | --- |
| **File List Processing** | Search across multiple files | `files = [fn.strip() for fn in input_str.split(',')]` |
| **Tabular Data Query** | Bond data, course records | Read lines → split by whitespace → map to tuples |
| **Lookup Structure** | Student transcripts, dictionaries | Build maps for fast key-based access |
| **Multi-file Processing** | Course files, batch operations | Iterate file list, handle each with try/except |

---

## 🧪 Testing checklist (suggested)

- Missing file → program should print an error and exit cleanly.
- Malformed line (hotel, bond) → report line number and content; either skip or terminate (follow guide).
- Case-insensitive searches return all matching lines from all listed files.
- Cipher encrypt + decrypt roundtrip should yield original plaintext (for letters only).
- Playfair: test with even & odd length messages, repeated letters, and padding rules.
- Covalent bonds: query by energy or length and verify multiple matches are returned.

---

## 💡 Tips & pitfalls

- Always validate `len(parts)` after `split()` when parsing structured text.
- When splitting file names input by user, strip spaces: `files = [fn.strip() for fn in input_str.split(',')]`.
- Preserve non-letter characters in monoalphabetic cipher (do not translate digits/punctuation).
- For Playfair, treat 'I' and 'J' as the same character (map both to the same cell).
- Use helper functions (`parse_hotel_line`, `encrypt_line`, `read_course_file`) — small functions make debugging easier.

---

## 🧾 Discussion (in-lab)

A. **What happens if you try to read/write a file that doesn't exist?**

- Reading: `FileNotFoundError` is raised.
- Writing with mode `'w'` will create the file. Use `'r'` for reading-only. Handle with `try/except`.

B. **Reporting vs handling an exception**

- *Reporting* = print/log the problem for the user or grader.
- *Handling* = take corrective action (retry, use default, skip, terminate gracefully). Both are important: report to be informative; handle to avoid crashes.

C. **Sequential access vs random access**

- Sequential: read bytes/lines in order (stream). Good for streaming and low memory.
- Random: jump to positions (seek), read arbitrary parts — useful for binary files or large datasets where you need specific records.

---

## 📂 Repo structure (place solutions & data here)

```
LABS/
└── LAB10/
    ├── 10.1.x  ....
    ├── 10.2.x
    ├── LabSlides
    └── README.md             # <-- this file

```

# 🧪 Lab 11 — Sets, Dictionaries & Table Searches

> “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”
> 
> 
> — *Martin Fowler (software architect & author)*
> 

---

## 📚 Welcome

Welcome to **Lab 11** of the *Computer Science Laboratory* at Politecnico di Torino.

This lab teaches three powerful tools you’ll use again and again: **sets**, **dictionaries**, and **table (2D list) searches**. You’ll turn text into frequency tables, build sparse-vector arithmetic with dictionaries, implement the Sieve of Eratosthenes, and solve path-finding problems on mazes using dictionaries keyed by coordinates.

This README gives you the concepts, short recipes, suggested exercises, and tips to complete the lab quickly and cleanly.

---

## 📘 What you’ll learn (high level)

- How to count and rank words in files (maps/dicts)
- How to use `set()` for membership and set algebra (union/intersection/difference)
- How dictionaries model sparse structures efficiently (sparse vectors)
- How to implement the Sieve of Eratosthenes using sets
- How to parse tab-separated and CSV data into dictionaries
- How to convert a 2D ASCII maze into adjacency dictionaries and compute paths to the exit

---

## 🧩 Exercises (overview)

### 🔹 Part 1 — Complex data structures

| Ex | Title | Notes |
| --- | --- | --- |
| **11.1.1** *(Suggested)* | **Counting words** | Count occurrence of each word in a text file; output word → frequency (use dict). |
| **11.1.2** | **Most frequent words** | Extend 11.1.1: show top-5 frequent words excluding articles/prepositions. |
| **11.1.3** *(Suggested)* | **Two strings** | Given two strings, show: intersection, symmetric difference, and letters missing from both (use `set`). |
| **11.1.4** *(Suggested)* | **Censor** | Read `bad_words.txt` → censor any occurrence (or sub-word) in `raw_text.txt` and write `censored_text.txt`. |
| **11.1.5** *(Suggested)* | **Sparse vectors** | Represent sparse vectors as dicts `{index: value}` and implement `sparse_array_sum(a,b)` returning a new sparse dict. |
| 11.1.6 | **Sieve of Eratosthenes** | Implement sieve using a `set()` of integers to produce primes < n. |

### 🔹 Part 2 — Complex operations

| Ex | Title | Notes |
| --- | --- | --- |
| **11.2.1** *(Suggested)* | **Per-capita income** | Read `rawdata_2004.txt` (tab `\t`) into `dict[country] = income`; interactive lookup until `'quit'`. Try `rawdata_2021.csv`. |
| 11.2.2 | **Genetic code** | Translate mRNA input into amino acid sequence using a `genetic_code` dictionary built from a CSV. |
| **11.2.3** *(Suggested)* | **Labyrinth (corridors dict)** | Read `maze.txt`, create `corridors` dict mapping `(r,c)` → `set(adjacent_positions)`. |
| 11.2.4 | **Ariadne's thread** | From `corridors`, build `paths` dict with direction letters (`N,E,S,W`) to nearest exit; print maze with directions. |

> Exercises marked (Suggested) are the recommended ones to complete during the lab session.
> 

---

## 🧰 New concepts & short cheatsheet

### Sets & set operations

- `s = set(iterable)` — build a set
- `A & B` — intersection
- `A | B` — union
- `A - B` — difference
- `A ^ B` — symmetric difference
- Good for membership (`x in s`) and uniqueness.

### Dictionaries (maps)

- `d = {}`; `d[key] = value`
- `d.get(key, default)` — safe retrieval
- `for k, v in d.items():` iterate pairs
- `sorted(d.items(), key=lambda kv: kv[1], reverse=True)` — sort by value

### File parsing

- Plain text: `open("file.txt")`, `.read()` or iterate lines
- Tab-separated: use `.split('\t')` or `csv` module with `delimiter='\t'`
- CSV: `import csv` → `csv.reader(...)` or `csv.DictReader(...)`

### Sparse vectors (dict representation)

- Represent vector `v` by `{i: v_i for v_i != 0}`
- To add: iterate over keys union and sum `a.get(i,0) + b.get(i,0)` — store only nonzero results.

### Sieve of Eratosthenes (key idea)

- Start with set `S = {2,3,...,n}`.
- Repeatedly take smallest element `p` in `S` (starting at 2) and remove `multiples = {p*k for k in range(2, ...)}` until `p*p > n`.

### Maze → corridors dictionary

- Scan file lines; for every `' '` (space) at coords `(r,c)`, collect adjacent corridor coordinates among four neighbors.
- `corridors[(r,c)] = set(adjacent_positions)`.

### Ariadne’s thread algorithm (sketch)

- `paths = {pos: '?' for pos in corridors}`
- For edge positions (row == 0 or col == 0 or row == max_row or col == max_col) assign direction to exit (`N/E/S/W`)
- Iteratively fill any `paths[pos] == '?'` that has neighbor with known `paths[neighbor] != '?'`. Repeat until no change.

---

## ✅ Testing & grading hints

- **Word counting**: test with uppercase/lowercase variants and punctuation-free assumption (lab says only alpha & spaces).
- **Sieve**: test `n=30` → primes `[2,3,5,7,11,13,17,19,23,29]`.
- **Sparse sum**: test with disjoint keys and overlapping keys (zeros must be removed).
- **Maze + Ariadne**: test with a small 5×5 maze and visually check output. Edge positions must be considered exits.

---

## 💡 Tips & pitfalls

- Always `.strip()` lines before splitting to avoid empty tokens.
- When reading CSV or TSV, prefer the `csv` module for robustness.
- Use `collections.Counter` for fast frequency counting in large texts.
- For big n in the sieve, avoid building huge lists — use sets and remove multiples carefully.
- For `corridors`, be strict about row/column bounds — printing indices helps debug.

---

## 🌱 Final advice (for your juniors)

- Break tasks into **tiny functions** (parse, process, output) — easier to test.
- Use `set()` whenever you need uniqueness or fast membership checks.
- Use dictionaries to model real-world sparse data — they’re fast and expressive.
- Comment assumptions in your solutions (e.g., input format). The professor reads those and it helps your grade.

---

## 📂 Repo structure

Put your solutions and files under:

```
LABS/
└── LAB11/
    ├── 11.1.x  ....
    ├── 11.2.x
    ├── LabSlides
    └── README.md             # <-- this file

```

---

### Code, Eat and Sleep! ⌨️🥷

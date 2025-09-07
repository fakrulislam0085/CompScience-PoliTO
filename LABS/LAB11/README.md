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

🔗 Sets & set operations
Operation	Meaning	Example
s = set(iterable)	Build a set (unique items)	s = set("hello") # {'h','e','l','o'}
A & B	Intersection (common elements)	{'a','b'} & {'b','c'} -> {'b'}
A | B	Union (all elements)	{'a'} | {'b'} -> {'a','b'}
A - B	Difference (in A not in B)	{'a','b'} - {'b'} -> {'a'}
A ^ B	Symmetric diff (in A or B but not both)	{'a','b'} ^ {'b','c'} -> {'a','c'}
Membership	Fast test for presence	'x' in s is O(1) on average

Tip: Use sets for uniqueness, fast membership tests, and simple set algebra.

🗺️ Dictionaries (maps)
Pattern	Purpose	Example
Create	d = {}	
Assign	d[key] = value	d['Italy'] = 35000
Safe lookup	d.get(key, default)	d.get('USA', 0)
Iterate	for k, v in d.items():	
Sort by value	sorted(d.items(), key=lambda kv: kv[1], reverse=True)	Top frequencies

Mini example

counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
# top-5
top5 = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:5]

📄 File parsing (quick recipes)
File type	Read method	Note
Plain text	with open("file.txt") as f: lines = f.read() or iterate for line in f:	.strip() to clean whitespace
Tab-separated	line.split('\t') or csv.reader(..., delimiter='\t')	Use csv for robustness
CSV	import csv → csv.DictReader(...)	Handles quoted fields automatically

Tip: Always .strip() before .split() and handle empty lines.

🔢 Sparse vectors (dict representation)

Idea: Store only non-zero entries: {index: value}.

Function sketch

def sparse_array_sum(a, b):
    result = {}
    keys = set(a) | set(b)
    for k in keys:
        s = a.get(k, 0) + b.get(k, 0)
        if s != 0:
            result[k] = s
    return result


Why: Memory & time efficient when most entries are zero.

🧠 Sieve of Eratosthenes (core idea + tiny pseudocode)

Core idea: start with S = {2..n}, repeatedly remove multiples of the smallest remaining number.

Pseudocode

S = set(2..n-1)
p = 2
while p*p < n:
    remove multiples of p from S (starting at p*p)
    p = next element in S after p
return sorted(S)


Note: Removing from a set is fine for moderate n; for very large n use a boolean array (memory & speed benefits).

🧭 Maze → corridors dictionary

Goal: convert ASCII maze into adjacency dictionary.

Rule: for every corridor cell (r,c) (a space ' '), set

corridors[(r,c)] = { (nr,nc) for each neighbor that is also a corridor }


Neighbors = up/down/left/right: [(−1,0),(1,0),(0,−1),(0,1)]

Mini code

for r, line in enumerate(lines):
    for c, ch in enumerate(line.rstrip('\n')):
        if ch == ' ':
            adj = set()
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if inside_bounds and lines[nr][nc] == ' ':
                    adj.add((nr,nc))
            corridors[(r,c)] = adj

🧵 Ariadne’s thread (algorithm sketch)

paths = {pos: '?' for pos in corridors}

For edge cells (exits) set paths[edge] = direction (N/E/S/W) toward outside.

Repeat:

For each pos with paths[pos] == '?', if any neighbor n has paths[n] != '?', set paths[pos] = direction_to(n).

Stop when no changes occur.

The paths dict will contain the direction to move from each corridor cell toward the nearest exit (or ? if unreachable).

Note: This is a BFS-like wave propagation; it produces shortest-path directions (in number of steps).

✅ Final quick tips

Use set() when uniqueness or membership speed matters.

Use dict for sparse structures and counting.

For parsing text files, prefer csv when columns are structured.

When implementing algorithms (sieve, BFS-like propagation), sketch the logic in plain english first, then code.

Add small tests and assert invariants (e.g., end >= start for intervals, len(parts) >= expected for parsed lines).

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


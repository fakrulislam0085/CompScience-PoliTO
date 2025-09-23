# Lab 01 — Course Overview, Setup & Python Built-ins Cheat Sheet

> Short course overview + quick setup so you (and your classmates) can start coding immediately.
---
> "Simplicity is the soul of Python." — Guido van Rossum (Creator of Python)
> 

---

## 1) Repo overview — what we do in these labs (quick roadmap)

This repository collects all labs for the **Computer Science** course (1st year, 1st semester, Course Code: 07JCJLM).

Below is a short roadmap of topics you’ll practice — one lab at a time — so you know how the pieces fit together.

| Lab | Content |
| --- | --- |
| **Lab01 (this file)** | Course overview, setup instructions, Python built-in functions cheat sheet. |
| **Lab02** | Python basics: variables, arithmetic, string slicing, formatting, alignment, emoji, basic I/O. |
| **Lab03** | Decisions & Boolean logic: comparisons, logical operators, De Morgan, small condition-based programs. |
| **Lab04** | Loops & simulations:`for/while`, partial sums, patterns, Nim game, simple physics simulations. |
| **Lab05** | File I/O & randomness: reading/writing files, pseudo-random generators, simulations (Drunkard's walk, Lotka-Volterra). |
| **Lab06** | Functions & modular code: geometry functions, bank balance, Roman numeral conversion, wire resistance. |
| **Lab07** | Lists & list algorithms: list operations, set membership, Bulgarian solitaire, parking simulation, smoothing filters. |
| **Lab08** | Tables & 2D lists: table creation, magic squares, neighbor averaging, tic-tac-toe, Hooke's-law spring simulation. |
| **Lab09** | Recap + applications: lists & tables recap, spiral matrix, theater seating, concatenated-words game, flood map. |
| **Lab10** | File processing & encryption: advanced file parsing, monoalphabetic & Playfair ciphers, tabular queries. |
| **Lab11** | Sets, dictionaries & path-finding: word counting, sparse vectors, Sieve of Eratosthenes, maze corridors, Ariadne's thread. |
| **Lab12** | Exam-style project: guest-contact finder across check-in/out intervals, robust file handling and output formatting. |

> Each lab folder contains: LabSlides (labX.pdf, labX_guide.pdf), solutions, README.md describing the lab.
> 

---

## 2) Quick setup — install Python + editors (Windows / macOS / Linux)

Below are short, reliable steps. The official lab PDF also contains an installation guide — follow that if platform specifics differ.

### A. Install Visual Studio Code (VS Code)

1. Download: https://code.visualstudio.com/ and install.
2. Open VS Code → Extensions → install **Python** (Microsoft). This provides syntax, linting, debugger.
3. Select interpreter: `Ctrl+Shift+P` → `Python: Select Interpreter` → choose the `.venv` interpreter (if created).
4. Run a file: open `main.py` → press `F5` or click the green run button.

> Helpful settings: enable formatOnSave and add python.linting.enabled: true in Settings if you like auto-checks.
> 

### B. Replit (online quick test)

1. Visit https://replit.com → Sign up / Log in → New REPL → choose **Python**.
2. Copy-paste code and run in the browser. Great for quick testing or sharing code with classmates.

---

## 3) 🐍 Python Built-in Functions — Cheat Sheet

> Compact, practical reference. Use this as your immediate cheat-sheet while coding exercises.
> 

---

### 🔹 Type & Info

| Function | Usage | Example |
| --- | --- | --- |
| `type()` | Get type of object | `type(5)` → `<class 'int'>` |
| `id()` | Get unique id of object | `id("abc")` |
| `dir()` | List attributes/methods | `dir([])` |
| `help()` | Get documentation | `help(str)` |

---

### 🔹 Input & Output

| Function | Usage | Example |
| --- | --- | --- |
| `print()` | Display output | `print("Hello")` |
| `input()` | Take user input | `name = input()` |

---

### 🔹 Numbers & Math

| Function | Usage | Example |
| --- | --- | --- |
| `abs()` | Absolute value | `abs(-7)` → `7` |
| `pow(x, y)` | Power | `pow(2, 3)` → `8` |
| `round()` | Round number | `round(3.1416, 2)` → `3.14` |
| `min()`, `max()` | Smallest / largest | `max([1, 2, 3])` → `3` |
| `sum()` | Sum of iterables | `sum([1,2,3])` → `6` |
| `divmod()` | Quotient & remainder | `divmod(7, 3)` → `(2,1)` |

---

### 🔹 Sequences (List, Tuple, String)

| Function | Usage | Example |
| --- | --- | --- |
| `len()` | Length | `len("hello")` → `5` |
| `sorted()` | Return sorted list | `sorted([3,1,2])` → `[1,2,3]` |
| `reversed()` | Reverse iterator | `list(reversed([1,2,3]))` → `[3,2,1]` |
| `enumerate()` | Index + value | `list(enumerate(['a','b']))` → `[(0,'a'), (1,'b')]` |
| `zip()` | Pair elements | `list(zip([1,2],[3,4]))` → `[(1,3),(2,4)]` |
| `all()` | True if all are True | `all([True,1,3])` → `True` |
| `any()` | True if any True | `any([0, False, 5])` → `True` |

---

### 🔹 Conversions

| Function | Usage | Example |
| --- | --- | --- |
| `int()`, `float()`, `str()` | Type casting | `int("7")` → `7` |
| `list()`, `tuple()`, `set()` | Convert between types | `list("abc")` → `['a','b','c']` |
| `dict()` | Create dictionary | `dict(a=1, b=2)` → `{'a':1, 'b':2}` |
| `bin()`, `oct()`, `hex()` | Number base | `bin(10)` → `'0b1010'` |

---

### 🔹 Iterators & Functional

| Function | Usage | Example |
| --- | --- | --- |
| `map()` | Apply function to iterable | `list(map(str, [1,2,3]))` → `['1','2','3']` |
| `filter()` | Filter items | `list(filter(lambda x: x>2, [1,2,3,4]))` → `[3,4]` |
| `reduce()`* (from `functools`) | Reduce iterable | `reduce(lambda x,y: x+y, [1,2,3])` → `6` |
| `range()` | Sequence generator | `list(range(1,5))` → `[1,2,3,4]` |

---

### 🔹 Object & Utility

| Function | Usage | Example |
| --- | --- | --- |
| `isinstance()` | Check type | `isinstance(5, int)` → `True` |
| `callable()` | Is callable? | `callable(print)` → `True` |
| `hash()` | Hash value | `hash("hello")` |
| `eval()` | Evaluate string as Python | `eval("2+3")` → `5` |
| `exec()` | Execute Python code | `exec("x=5; print(x)")` |
| `globals()` / `locals()` | Namespace dict | `globals()` |

---

### 🔠 Python String Methods (Character Checks)

| Method | Returns `True` if… | Example |
| --- | --- | --- |
| `s.isalpha()` | all characters are **letters** | `"abc".isalpha()` → `True` |
| `s.isdigit()` | all characters are **digits** | `"123".isdigit()` → `True` |
| `s.isalnum()` | all characters are **letters or digits** | `"abc123".isalnum()` → `True` |
| `s.isspace()` | all characters are **whitespace** (`' '`, `\t`, `\n`) | `"   ".isspace()` → `True` |
| `s.islower()` | all cased chars are **lowercase** | `"hello".islower()` → `True` |
| `s.isupper()` | all cased chars are **uppercase** | `"HELLO".isupper()` → `True` |
| `s.istitle()` | string is **Title Case** | `"Hello World".istitle()` → `True` |
| `s.isnumeric()` | numeric chars only (includes some unicode numbers) | `"²".isnumeric()` → `True` |
| `s.isdecimal()` | only decimal digits (0–9) | `"123".isdecimal()` → `True` |

---

### 🛠 Other Handy String Methods

| Method | What it does | Example |
| --- | --- | --- |
| `s.lower()` | make lowercase | `"HeLLo".lower()` → `"hello"` |
| `s.upper()` | make uppercase | `"HeLLo".upper()` → `"HELLO"` |
| `s.title()` | title case | `"hello world".title()` → `"Hello World"` |
| `s.capitalize()` | capitalize first letter | `"python".capitalize()` → `"Python"` |
| `s.strip()` | remove whitespace (or chars) from both ends | `"  hi  ".strip()` → `"hi"` |
| `s.lstrip()` / `s.rstrip()` | remove left/right spaces | `"   hi".lstrip()` → `"hi"` |
| `s.startswith(x)` | check prefix | `"python".startswith("py")` → `True` |
| `s.endswith(x)` | check suffix | `"python".endswith("on")` → `True` |
| `s.find(x)` | index of first occurrence (or `-1`) | `"hello".find("l")` → `2` |
| `s.index(x)` | like `find()` but raises error if not found | `"hello".index("l")` → `2` |
| `s.count(x)` | count occurrences | `"banana".count("a")` → `3` |
| `s.replace(a, b)` | replace substring | `"hello".replace("l", "x")` → `"hexxo"` |
| `s.split()` | split into list | `"a b c".split()` → `['a','b','c']` |
| `s.join(list)` | join list into string | `".".join(['a','b','c'])` → `"a.b.c"` |

---

## 4) Short tips & good practices

- Use **virtualenv** for each project to isolate dependencies.
- Prefer `with open(...) as f:` for safe file handling.
- Avoid `eval`/`exec` unless strongly needed.
- Write small functions and test them separately.
- Use **meaningful variable names** and comment assumptions (helps graders and teammates).

---

## Tips for Python Beginners

Getting started with Python programming? Here are some helpful tips to make your coding journey smoother:

- **Use meaningful variable names**: Choose descriptive names that explain what the variable stores (e.g., `student_count` instead of `sc`)
- **Practice consistent indentation**: Python relies on indentation for code blocks. Use 4 spaces for each level of indentation
- **Comment your code**: Add comments to explain complex logic or why you made certain decisions
- **Use list comprehensions** for cleaner code: `[x*2 for x in range(10)]` is more readable than a for-loop for simple operations
- **Learn to debug effectively**: Use `print()` statements or the `pdb` module to trace issues in your code
- **Write small, focused functions**: Each function should do one thing well
- **Use virtual environments**: Keep project dependencies isolated with `venv` or `conda`
- **Read error messages carefully**: Python provides helpful error messages - the solution is often in the error text
- **Practice regularly**: Consistent practice is key to learning any programming language


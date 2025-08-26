# Computer Science Laboratory #8

> “Simple is better than complex.” — The Zen of Python (Tim Peters, Python developer)
> 

---

## 📝 Welcome Note

Welcome to **Lab 08** of the *Computer Science Laboratory* course for First-Year, First-Semester students at Politecnico di Torino.

This lab focuses on **lists and tables**. You’ll explore similarities and differences between them, how indexes work, and how to avoid common pitfalls like out-of-range errors. Through hands-on exercises, you’ll practice creating, manipulating, and combining both **1D and 2D data structures**, setting the foundation for more advanced algorithms.

📂 **Lab structure**: `LABS/LAB08`

---

## 🧠 What You’ll Learn in This Lab

The lab is divided into **two parts**:

### 🔹 Part 1 – Processing Lists and Tables

- Understanding out-of-range errors
- Shifting elements in a list
- Detecting and highlighting dice roll sequences
- Constructing and modifying tables with patterns
- Merging lists (normal + sorted)

### 🔹 Part 2 – Algorithms with Lists and Tables

- Calculating neighbor averages in a table
- Checking if a table is a **magic square**
- Building a **tic-tac-toe** game
- Simulating a spring with Hooke’s Law

---

## 🧰 New Concepts You Need to Know

### 🔑 Core Concepts

| Concept | What It Means |
| --- | --- |
| **Out-of-range error** | Happens when you try to access an index beyond the valid range of a list/table. Always check with `len()`. |
| **Tables (2D lists)** | Represented as “lists of lists” in Python. Each row is itself a list. |
| **Indexes in strings, lists, tables** | Strings: `s[i]` → character; Lists: `list[i]` → element; Tables: `table[row][col]` → element |

### 🔑 Python Tools

| Function / Concept | Usage |
| --- | --- |
| `list.append(x)` | Adds element at the end of list |
| `list.pop(i)` | Removes and returns element at index `i` |
| `list.insert(i, x)` | Inserts `x` at index `i` |
| `len(list)` | Returns number of elements |
| `zip(a, b)` | Iterates pairs from two lists |
| `randint(a, b)` | Generates random integer between `a` and `b` |

### 🔑 List Comprehensions (Detailed)

List comprehensions give a concise way to create lists:

### ✅ 1D Lists

```python
# Squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, ..., 81]

```

### ✅ 2D Lists (Tables)

```python
# Create 3x3 table filled with zeros
table = [[0 for col in range(3)] for row in range(3)]
print(table)
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

```

👉 **Tip:** Outer loop = rows, inner loop = columns. This is the standard way to build grids.

---

## 🧩 Exercise Overview

### 🌀 Part 1: Processing Lists and Tables

| Exercise | Title | Description |
| --- | --- | --- |
| [08.1.1] | Out-of-range | Write a program that triggers an out-of-range error and observe the behavior |
| **[08.1.2]** *(Suggested)* | Buffer Shift | Implement `shiftList()` to rotate elements (last becomes first) |
| [08.1.3] | Throwing Dices | Generate 20 dice rolls, highlight the longest sequence of identical values |
| **[08.1.4]** *(Suggested)* | Table Patterns | Create and manipulate an `m × n` table with different filling rules and sum calculation |
| [08.1.5] | Merging Lists | Merge two lists, alternating elements |
| [08.1.6] | Merging Sorted Lists | Merge two **sorted** lists into a new sorted one (without using `.sort()` or `sorted()`) |

---

### 🚀 Part 2: Algorithms with Lists and Tables

| Exercise | Title | Description |
| --- | --- | --- |
| **[08.2.1]** *(Suggested)* | Neighbor Average | Compute average of neighbors (8 directions) in a table |
| **[08.2.2]** *(Suggested)* | Magic Square | Check if a 4×4 matrix is a magic square |
| [08.2.3] | Tic-Tac-Toe | Implement two-player tic-tac-toe game |
| [08.2.4] | Spring Simulation | Simulate a spring oscillating with Hooke’s Law (F = -kx) |

---

## 💎 Tips for Writing Clean Code

- Always check index ranges: `if 0 <= i < len(list): ...`
- Use **list comprehensions** for clean initialization of lists/tables.
- Separate **logic from display**: write helper functions like `printTable()`.
- Test with **edge cases**: empty list, single row table, very large table.
- Document assumptions (e.g., “lists must be sorted” in merge functions).

---

## 🌱 Final Advice for Juniors

1. **Think visually**: tables are just lists of lists — rows and columns are indexes!
2. Always handle **boundary cases** (edges/corners in neighbor problems).
3. Games and simulations (tic-tac-toe, spring) may look complex, but they’re just **loops + conditions**.
4. Write modular code: break down problems into **small functions**.
5. Debug by printing intermediate tables — it’s the best way to *see* what’s going on.

---

📂 **Repo Structure**:

```
LABS/
│── LAB07/
│── LAB08/   ← (You are here)

```

---

✨ *Lists and tables are the building blocks of data structures. Master them now, and you’ll unlock the power to model everything from simple games to scientific simulations.*

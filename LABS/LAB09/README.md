# 🧪 Lab 09: Lists, Tables & Applications

> “The only way to learn a new programming language is by writing programs in it.” — Dennis Ritchie (creator of C)
> 

---

## 📝 Welcome Note

Welcome to **Lab 09** of the *Computer Science Laboratory* course for First-Year, First-Semester students at Politecnico di Torino.

This lab is a **recap of key programming ideas** you’ve been building since the beginning:

- Conditionals for **making decisions** (Lab03)
- Loops for **repetition** (Lab04)
- Lists and tables for **storing and processing data** (Lab08)

You’ll revisit these fundamentals in slightly more complex contexts — bar charts, list transformations, seating simulations, and even flooding terrains 🌊. Think of this lab as a **bridge** between your basics and more advanced problem-solving.

---

## 🧠 What You’ll Learn in This Lab

### 🔹 Core Topics

1. **Using conditional constructs to make decisions** (review from Lab03)
2. **Using loops for repeated execution of instructions** (review from Lab04)
3. **Definition and processing of lists and tables** (review from Lab08)

### 🔹 Discussion Questions

- **A.** How do you use conditional constructs to make complex decisions?
- **B.** How should general vs. specific conditions be handled in conditionals?
- **C.** In the context of loops, what is an *off-by-one error*?
- **D.** What search algorithm is used to find an element in an unordered set?
- **E.** Which construct is best suited for iterating through a 2D table?

---

## 🧰 New Concepts & Tools

| Concept | Explanation |
| --- | --- |
| Conditional chaining | Build layered decisions (e.g., `if … elif … else`) |
| Off-by-one error | Loop goes one step too far (classic bug when indexing lists) |
| Linear search | Used for searching in unordered lists |
| List transformations | Swapping, shifting, replacing, removing elements |
| Bar chart printing | Scale values relative to max and visualize with `*` |
| Nested lists (tables) | Represent seating charts or matrices |
| Sentinel values | Special values (like `0` or `-1`) to stop input loops |

---

## 🧩 Exercise Overview

### 🌀 Part 1: Recap Exercises

| Exercise | Title | Description |
| --- | --- | --- |
| **09.1.1** *(Suggested)* | List Functions | Implement swap, shift, replace, neighbor check, remove middle, second-largest, check sorted, duplicates… all in list-processing functions |
| **09.1.2**  | Hidden Rules | Initialize lists with sequences (arithmetic, squares, alternating, cyclic, etc.) by discovering the generation rule |
| 09.1.3 | Bar Chart | Read values and display bars (`*`) scaled to max value |
| 09.1.4 | Bar Chart with Negatives | Improve chart to handle positive + negative values |
| 09.1.5 | Captioned Chart | Add labels to each bar, align nicely |
| 09.1.6 | Integer List Parser | Parse colon-separated list and filter: without min/max, only even numbers, only 2-digit numbers |

---

### 🚀 Part 2: Applications

| Exercise | Title | Description |
| --- | --- | --- |
| 09.2.1 *(Suggested)* | Theater Seating | Manage seat booking by seat number or price; mark sold seats |
| 09.2.2 | Concatenated Words Game | Word-chain game where next word must start with last 2 letters of previous |
| 09.2.3 | Best Customer | Track daily sales and return customer with highest purchase |
| 09.2.4 | Spiral Matrix | Build `N x N` spiral of numbers from 1 to `N²` |
| 09.2.5 | Pet Shop Discount | Apply discount only to non-pet items if >= 5 purchased |
| 09.2.6 | Flood Map | Show terrain flood levels with `*` for flooded and space for safe |

---

## 💎 Tips for Writing Clean Code

- Double-check **loop ranges** to avoid off-by-one bugs.
- Use **helper functions** (`is_sorted`, `swap`, `sum_without_min`) to keep code modular.
- For visualization problems (bar charts, spiral matrices, flood maps) — **sketch on paper first**.
- Handle **edge cases**: empty list, single element, max/min duplicates.
- Document assumptions (e.g., “list length ≥ 2” for swapping).

---

## 🌱 Final Advice for Juniors

This lab revisits all your core skills. Think of it as:

- **Conditionals = brain** (decision making)
- **Loops = heartbeat** (repetition)
- **Lists/Tables = memory** (storing data)

If you master these three, you’ll have 80% of the toolkit you need for serious programming. Practice each exercise like you’re sharpening your sword 🗡️ — it may feel repetitive now, but when the *real battles* (projects, exams, coding interviews) come, you’ll be grateful.

---

✅ **Repo Path:** `LABS/LAB09`

---

Code, Code and Code. That's the Future! 🚀

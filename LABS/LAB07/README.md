# Computer Science Laboratory #7

> "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live." — John Woods (Programmer)
> 

---

## 📝 Welcome Note

Welcome to **Lab 07** of the *Computer Science Laboratory* course for First-Year, First-Semester students at Politecnico di Torino.

This lab focuses on **lists, algorithms, and simulations**. You’ll learn how to manipulate data structures effectively, simulate processes, and build a deeper understanding of how iteration and randomness shape computational models.

📂 **Lab structure**: `LABS/LAB07`

---

## 🧠 What You’ll Learn in This Lab

This lab is split into **two parts**:

### 🔹 Part 1 – Elaboration of Lists

- Alternating sums
- Index-based operations
- Removing elements without built-in shortcuts
- Detecting local maxima
- Comparing sets inside lists
- Sorting and random list generation
- Summations with conditions

### 🔹 Part 2 – Algorithms that Use Lists

- Noise filtering (data smoothing)
- Parking space simulation
- Bulgarian solitaire simulation

---

## 🧰 New Concepts You Need to Know

Here are the most important **new concepts** introduced in Lab 07:

| Concept | What It Means |
| --- | --- |
| `from random import randint` | Imports only the `randint` function from the `random` module |
| `randint(a, b)` | Generates a random integer in range `[a, b]` inclusive |
| `random()` | Generates a float between 0.0 and 1.0 |
| `uniform(a, b)` | Generates a random float between `a` and `b` |
| `choice(list)` | Picks one random element from a list |
| `list.sort()` | Sorts the list in-place |
| `sorted(list)` | Returns a new sorted list |
| `list.append(x)` | Adds an element to the end of the list |
| `list.pop(i)` | Removes and returns element at index `i` |
| `list.remove(x)` | Removes the first occurrence of element `x` |
| `list.index(x)` | Returns index of first occurrence of element `x` |
| `list.count(x)` | Returns the number of occurrences of `x` in the list |
| `[::-1]` | Reverses a list quickly |
| `set(a) == set(b)` | Checks if two lists contain the same unique elements |

---

## 🧩 Exercise Overview

### 🌀 Part 1: Elaboration of Lists

| Exercise | Title | Description |
| --- | --- | --- |
| **[1.1]** *(Suggested)* | Alternating Sum | Compute alternating sum of integers (e.g., `1 - 4 + 9 - 16 + ...`) |
| [1.2] | List of Random Numbers | Generate 10 random numbers and display subsets (even index, even value, reverse, first/last) |
| **[1.3]** *(Suggested)* | Remove Min | Implement `remove_min(v)` without using `min()` or `remove()` |
| [1.4] | Local Highs | Find and print positions of local maxima |
| **[1.5]** *(Suggested)* | Same Elements | Implement `same_set(a, b)` ignoring duplicates and order |
| [1.6] | Ordered List | Generate 20 random numbers, sort them, print both versions |
| [1.7] | Sum Without Min | Implement `sum_without_smallest(v)` |

---

### 🚀 Part 2: Algorithms that Use Lists

| Exercise | Title | Description |
| --- | --- | --- |
| **[2.1]** *(Suggested)* | Measurement Noise | Replace each element with average of neighbors (smoothing) |
| [2.2] | Distances | Simulate parking space filling rule (middle of longest free row) |
| **[2.3]** *(Suggested)* | Bulgarian Solitaire | Simulate solitaire with random initial piles until final config |

---

## 💎 Tips for Writing Clean Code

- Always **separate concerns**: input, processing, output.
- Test with **edge cases**: empty list, single element, large values.
- Use **list comprehensions** when clean and readable.
- Remember: `random.randint()` includes both ends, unlike `range()`.
- Use `set()` for comparing list uniqueness.

---

## 🌱 Final Advice for Juniors

1. Don’t just generate random numbers — **understand how randomness drives algorithms**.
2. **Debug step by step**: print intermediate lists, check before/after operations.
3. Simulations like Bulgarian solitaire may look complex, but they’re just **loops + lists + logic**.
4. Be patient with edge cases (like empty lists or repeated elements).
5. Practice writing functions (`def`) for each sub-task; modular code = happy code.

---

📂 **Repo Structure**:

```
LABS/
│── LAB05/
│── LAB06/
│── LAB07/   ← (You are here)
```

---

✨ *Good code is not just about solving problems — it’s about solving them with clarity, simplicity, and a touch of elegance.*


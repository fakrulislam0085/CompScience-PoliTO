# 🧪 Lab 02: Python Basics & String Manipulation

Welcome to **Lab 02** of the *Computer Science* course for First-Year, First-Semester students at Politecnico di Torino. This lab is all about building **foundational Python skills** — from arithmetic to string tricks, wrapped in real-world logic and fun formatting challenges.
>"First, solve the problem. Then, write the code." — John Johnson (Pioneering computer scientist and writer)
---

## 📚 Topics Covered

This lab explores the following core Python concepts:

### ✅ Part 1: Arithmetic & Logic

- Constants and variable naming
- Basic arithmetic operators (`+`, `-`, `*`, `/`, `**`)
- Absolute value, min & max
- Squaring numbers
- Scientific notation & formatting

### ✅ Part 2: Strings & Formatting

- String slicing and manipulation
- Unicode and emoji handling
- Output formatting (alignment)
- String transformations (e.g., phone number formatting)

---

## 📝 Exercises Breakdown

### 🔹 Part 1: Arithmetic Operations

| Exercise | Description |
| --- | --- |
| **02.1.1 – Two Numbers** *(Suggested)* | Work with two constant integers and calculate: sum, difference, product, average, absolute difference, min, max. Use `abs()`, `min()`, `max()`. |
| **02.1.2 – Resistances** | Input 3 resistor values and compute total resistance based on Ohm’s law. |
| **02.1.3 – Digits** | Store a five-digit integer as a constant and print each digit on a new line. |
| **02.1.4 – Hybrid Car** | Compare total cost of a hybrid vs gasoline car over 5 years based on input factors. |
| **02.1.5 – Electric Force** *(Suggested)* | Use Coulomb’s law to compute the electric force between two charges: |

---

### 🔹 Part 2: String Manipulation

| Exercise | Description |
| --- | --- |
| **02.2.1 – Characters** *(Suggested)* | Slice a string to show the first 3 + last 3 characters (e.g. `Mississippi` → `Mis...ppi`). Handle short strings gracefully. |
| **02.2.2 – Telephone Number** *(Suggested)* | Convert a 10-digit string like `"4155551212"` to `" (415) 555-1212"`. |
| **02.2.3 – Alignment** | Format outputs (e.g., sum, difference, etc.) so values align vertically. Use `:<`, `:>`, or `:^`. |
| **02.2.4 – Emoji** | Display emoji data: Unicode code, name, character, and ranking. Use `ord()` and `unicodedata.name()`. |
| **02.2.5 – Enrolments** | Compare two student IDs and sort them based on the numerical part only (ignore the letter). Use `ord()`, slicing, and `int()`. |

---

## 🧠 Concept Primer – What You Should Know First

Before tackling the exercises, review these Python concepts:

### 🔢 Absolute Value: `abs()`

Returns the positive version of a number.

```python
abs(-9)  # 9

```

### 🔼 Minimum & Maximum: `min()`, `max()`

Find the smallest or largest value.

```python
min(3, 5, 1)  # 1
max(3, 5, 1)  # 5
```

### ➗ Modulo Operator: `%`

Returns the remainder of a division.

```python
10 % 3  # 1

```

### 🐫 Naming Conventions: `camelCase` vs `snake_case`

| Style | Example | Notes |
| --- | --- | --- |
| `camelCase` | `totalCost` | More common in Java |
| `snake_case` | `total_cost` | ✅ Preferred in Python |

### 🔁 Using `main()` Function

Improves structure, readability, and prevents code from auto-running on import.

```python

def main():
    print("Hello PoliTO!")

if __name__ == "__main__":
    main()

```

### ✖️ Squaring in Python

```python

x = 5
x_squared = x ** 2  # 25

```

### 🎯 Alignment Formatting

```python

value = 42
print(f"{value:<10}")  # Left-align
print(f"{value:>10}")  # Right-align 
print(f"{value:10}")   # Right-align
print(f"{value:^10}")  # Center-align

```

### 🔬 Scientific Numbers with `'e'`

Used for very large or small numbers.

```python

num = 0.000045
print(f"{num:.2e}")  # Output: 4.50e-05

```

### ➕ `import math`

Brings advanced mathematical functions like:

```python
import math
math.sqrt(25)  # 5.0
math.pi        # 3.14159...
```

---

## 🚀 Final Tips

- Read each exercise carefully before starting.
- Comment your code! It's for you and for the grader.
- Format your output — clean output = clean thinking.
- If you're stuck, break the problem down into smaller parts.

---

🎉 **Now go crush Lab 02 like the coding king/queen you are.**

Happy coding! 💻🧠

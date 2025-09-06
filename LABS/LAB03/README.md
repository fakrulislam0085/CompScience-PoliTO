# 🧪 Lab 03: Comparisons, Decisions & Clean Python Thinking

Welcome to **Lab 03** of the *Computer Science* course for First-Year, First-Semester students at Politecnico di Torino. This lab goes deeper into **logical reasoning**, **decision making**, and **Python control structures** — preparing you for real-world programming scenarios where clean decisions matter.

---

## 📚 Topics Covered

This lab builds on earlier concepts and introduces powerful logic tools:

### ✅ Part 1: Comparisons & Boolean Expressions

* Equality, inequality, relational operators
* String analysis with methods like `.isupper()`, `.isdigit()`
* Boolean logic (`and`, `or`, `not`)
* De Morgan's Law
* Using `index()` and `count()` with strings
* Tuple-based assignments

### ✅ Part 2: Decisions & Control Flow

* Nested and chained conditions
* `if`/`elif`/`else` logic
* Input validation
* Writing and reading scientific notation (e.g., `1.23e-7`)
* Dictionary unpacking with `**`
* `try`/`except` for error control
* Real-world case studies (e.g., leap years, tax brackets, shopping vouchers)

---

## 📝 Exercises Breakdown

### 🔹 Part 1: Boolean Operators & Logic

| Exercise                                  | Description                                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------- |
| **03.1.1 – Equality Tests** *(Suggested)* | Compare values of different types and predict Python’s behavior.            |
| **03.1.2 – String Analysis**              | Check if a string has only letters, digits, capital letters, etc.           |
| **03.1.3 – DNA Substring**                | Use `.index()` and `.count()` to find short sequences inside DNA strings.   |
| **03.1.4 – Pseudocode Debugging**         | Analyze a buggy pseudocode and explain what’s wrong.                        |
| **03.1.5 – Boolean Expressions**          | Evaluate several compound Boolean expressions with different values of `x`. |
| **03.1.6 – De Morgan’s Law**              | Rewrite expressions using De Morgan’s Law and print equivalences.           |

### 🔹 Part 2: Decisions

| Exercise                                         | Description                                                                      |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| **03.2.1 – Number Sequence Check** *(Suggested)* | Check if 3 numbers are strictly increasing, decreasing, or neither.              |
| **03.2.2 – Grade to Number**                     | Convert a letter grade (with optional +/-) to a numeric GPA.                     |
| **03.2.3 – Season Detector**                     | Given a month and day, output the current season.                                |
| **03.2.4 – Leap Year** *(Suggested)*             | Determine if a given year (post-1582) is a leap year using Boolean operators.    |
| **03.2.5 – Number to Grade**                     | Given a GPA (0.0–4.0), return the closest letter grade (with + or -).            |
| **03.2.6 – Tax Brackets**                        | Calculate taxes based on income and marital status.                              |
| **03.2.7 – Unit Converter**                      | Convert between compatible metric/imperial units using validation.               |
| **03.2.8 – Supermarket Vouchers**                | Calculate discounts based on the amount of groceries bought.                     |
| **03.2.9 – Electromagnetic Spectrum**            | Identify wave type based on scientific-notation wavelength input.                |
| **03.2.10 – Halley’s Comet**                     | Simulate jump velocity and calculate escape mass based on gravitational physics. |

---

## 🔍 Concepts Primer – Review Before You Code

### ✍️ Input Validation

Always ensure your inputs are clean. Use `try/except` to catch invalid data early.

```python
try:
    val = float(input("Enter a number: "))
except ValueError:
    print("That wasn't a valid number.")
```

### 🔗 Comparison Chaining

Python allows this neat syntax:

```python
if 0 < x < 100:
    print("x is between 0 and 100")
```

### 🧠 Boolean Logic & De Morgan

Know these:

```python
not (A and B) == (not A or not B)
not (A or B) == (not A and not B)
```

### 🎯 `index()` & `count()`

* `index()` gives the first position where something appears.
* `count()` tells how many times it appears.

```python
word = "banana"
print(word.index("n"))  # 2
print(word.count("a"))  # 3
```

### 🧱 Alignment Formatting

Use `:<`, `:>`, `:^` to cleanly align outputs:

```python
print(f"{'Label':<20}{42:>5}")
```

### 🧪 Scientific Notation in Code

```python
wavelength = 1.23e-7  # = 0.000000123
```

### 💼 Dictionary Unpacking

```python
def show_info(**kwargs):
    for key, val in kwargs.items():
        print(key, val)
```

### 🎭 `isupper()`/`islower()` vs `upper()`/`lower()`    

* `isupper()` checks if ALL letters are uppercase.
* `upper()` transforms string to uppercase.

* `islower()` checks if ALL letters are lowercase.
* `lower()` transforms string to lowercase.

```python
s = "ABC"
s.isupper()  # True
s.upper()    # 'ABC'
```

---

## 📁 Project Structure

All of the files of this lab are organized in this structure:

```
/LABS
  └── /LAB03
      ├── 03.1.1_equality_tests.py
      ├── 03.1.2_string_analysis.py
      ├── ...
      └── 03.2.10_halley_escape_velocity.py
```

Each exercise lives in its own `.py` file. Great for clarity, testing, and future reuse.

---

## 💡 Advice to Juniors

* **Test often.** Run your code after writing small chunks.
* **Read error messages!** They're your best debugging buddies.
* **Name variables clearly.** Avoid `x`, `y`, `z` unless they truly make sense.
* **Use comments wisely.** Focus on tricky logic, not obvious code.
* **Master `if` logic.** It’s the heart of this lab — and of most real-world programs.
* **Handle exceptions.** Get used to guarding your code against bad inputs.
* **Enjoy the challenge.** This lab gets deep — but it also shows how powerful and readable Python can be.

---

🎓 **You’re not just writing code — you’re building the logic muscle.**

Go crush it, clean coder. 💥

Happy coding! 🧠💻


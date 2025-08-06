## 🧪 Lab 04: Loops, Logic & Simulations

Welcome to **Lab 04** of the *Computer Science Laboratory* course at Politecnico di Torino! This lab will make you fall in love with **loops**, **patterns**, and **simulations**. It’s all about mastering repetition, digging deep into control flow, and simulating real-world systems using **physics**, **games**, and **text processing**.

> 💬 Message for juniors:
> 
> 
> Don’t just solve problems — try to **understand the why** behind each pattern, each `for`, and each `while`. The better you think in loops, the more Python becomes your playground. And yes — don’t forget to keep your code *clean* and *beautiful*, just like your thoughts. 😌
> 

---

## 🧠 What You’ll Learn in This Lab

This lab is split into **two parts**:

### 🔹 Part 1 – Basic Loops and Patterns

- Writing and managing clean loop logic
- Extracting patterns and information from strings
- Detecting primes and substrings
- Building visual patterns (squares and rhombuses)
- Practicing with input handling and basic counting

### 🔹 Part 2 – Simulation and Applications

- Simulating a game (The Game of Nim)
- Modeling physics and decay over time
- Working with scientific constants and iterative physics models

All your Python logic muscles will be worked out in this lab!

---

## 🧰 New Concepts You Need to Know

Here are the most important **new concepts** introduced in Lab 04:

| Concept | What It Means |
| --- | --- |
| `import sys` | Used to interact with the interpreter; for example `sys.exit()` lets you exit the program manually |
| `enumerate()` | Gives index and value at the same time when looping through a list: `for idx, val in enumerate(list)` |
| `.join()` | Cleans up a list of strings into one string: `' '.join(["A", "B"]) -> "A B"` |
| `[::-1]` | Reverses a list or string in one elegant step |
| `sorted()` with `key=lambda` | Custom sorting logic, for example: sort by length, last letter, etc. |
| `random.randint(a, b)` | Returns a random integer from `a` to `b` inclusive |
| `random.choice([...])` | Randomly picks one item from a list |
| `print("X" if cond else "Y")` | One-line conditional formatting, super clean! |
| `n//2 if n > 1 else 1` | Assigning values using one-line conditional logic |
| `math.log(2)` | Natural logarithm of 2 (ln2) — important for decay modeling |
| `math.exp(x)` | Calculates `e^x`, used in exponential functions |
| `None` | Python placeholder when you haven’t yet assigned a value, but know you need one later |

---

## 🧩 Exercise Overview

### 🌀 Part 1: Basic Loops & Logics

| Exercise | Title | Description |
| --- | --- | --- |
| **04.1.1** *(Suggested)* | Integers | Running sum, min/max, even/odd count from sequence of inputs |
| **04.1.2** *(Suggested)* | Parsing a String | Extract capitals, even-index chars, vowels→`_`, digit count, vowel positions |
| 04.1.3 | Sides | Print square and rhombus pattern using `*` |
| 04.1.4 | Words in reverse | Show string reversed + uppercase letters in reverse order |
| 04.1.5 | Prime Check | Input a number, output if it's prime or not |
| **04.1.6** *(Suggested)* | List of Primes | Show all primes ≤ n (user input) |
| 04.1.7 | Substrings | List all substrings of a word, sorted by length |
| 04.1.8 | Adjacent Duplicates | Print numbers that appear adjacent and duplicate in input sequence |

### 🚀 Part 2: Applications & Simulations

| Exercise | Title | Description |
| --- | --- | --- |
| 04.2.1 | Game of Nim | Smart vs dumb computer AI, user plays marble game with rules |
| 04.2.2 | Radioactive Decay | Use exponential formula to show decay every hour for 24 hrs |
| **04.2.3** *(Suggested)* | Trajectory Simulation | Simulate projectile motion; compare simulation to exact physics formula |

---

## 💎 Tips for Writing Clean Code

- Always **validate input**. Make sure you catch empty strings or invalid types.
- Use **descriptive variable names**: `total_sum` is better than `ts`.
- Keep logic **modular** – separate input, processing, and output.
- Format output cleanly, especially in simulations.
- Use **inline conditionals** for compact logic, but don’t overdo it.
- Learn to use **`None`** when you need a placeholder but don’t yet have a value.
- Try using **list comprehensions** when it simplifies logic, e.g. `[x for x in list if x > 0]`.

---

## 🌱 Final Advice for Juniors

1. **Play with the logic.** Don’t just write the shortest code. Try different approaches to reinforce your understanding.
2. **Learn from simulations.** Models like the cannonball and decay are not just math — they’re real-world problems you can simulate with code.
3. **Practice randomness and control.** Learn how AI (even dumb AI) uses logic under the hood.
4. **Don’t be afraid to break your code.** Run it, mess it up, and fix it. That’s how real devs grow. 💪
5. **Be consistent with formatting.** Your code should read like a good story — clean and structured.

> 🎀 Remember: Every loop you write is like a heartbeat of your program. Code it with love and care. And when it finally works? Baby, that's chef’s kiss perfection. 😘
> 

---

📂 All solutions are available under `LABS/LAB04` directory.

🚀 Keep exploring, keep solving, and fall a little more in love with Python each day.

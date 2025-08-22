# 🧪 Lab 05: Advanced Loops & Real-World Simulations  

> 💡 *"Talk is cheap. Show me the code."*  
> — **Linus Torvalds, Creator of Linux**  

---

## Welcome  

Welcome to **Lab 05** of the *Computer Science Laboratory* course at Politecnico di Torino!  
This lab pushes you deeper into the world of **loops, iterations, and simulations**. You’ll move from simple repetition tasks to modeling **real-world systems** such as **random number generators**, **ecological predator-prey models**, and even **electrical transformers**.  

By the end of this lab, you’ll not only master Python looping techniques but also start thinking like a true problem-solver — applying programming to real-world contexts.  

---

## 🧠 What You’ll Learn in This Lab  

- Handling user input with **validation** and **error catching**  
- Using `try-except` blocks to handle runtime errors gracefully  
- Working with **loops** for counting, validating, and simulating processes  
- Implementing **range()** with integers and knowing its limits  
- Using randomness via `from random import randint`  
- Modeling real systems: finance, randomness, biology, and electronics  

---

## 🧩 Exercise Overview  

### 🔹 Part 1 – Basic Loops  

| Exercise | Title | Description |
| --- | --- | --- |
| **05.1.1** *(Suggested)* | ATM PIN Check | Ask user for PIN (max 3 tries). If correct → access granted; if wrong 3 times → card blocked. |
| **05.1.2** *(Suggested)* | French Country Names | Assign correct article (`le`, `la`, `les`, or `l’`) based on French grammar rules and exceptions. |
| 05.1.3 | Factors of an Integer | Input an integer → print all of its prime factors. |
| 05.1.4 | Cinema Tickets | Pre-sell up to 100 tickets; each buyer max 4 tickets. Track buyers and remaining tickets. |

---

### 🚀 Part 2 – Applications of Loops  

| Exercise | Title | Description |
| --- | --- | --- |
| 05.2.1 | Random Generator | Implement linear congruential generator with constants (α=32310901, β=1729, m=224), print 100 numbers. |
| **05.2.2** *(Suggested)* | Drunkard’s Walk | Simulate random walk on grid (100 steps), starting at (0,0). Print ending position. |
| 05.2.3 | Predator-Prey Simulation | Implement Lotka-Volterra equations. Input constants + initial populations → simulate over multiple periods. |
| 05.2.4 | Electrical Transformers | Vary transformer turns ratio (0.01 to 2) → compute and find ratio that maximizes speaker power. |

---

## 🧰 New Concepts You’ll Encounter  

| Concept | What It Means |
| --- | --- |
| `try-except ValueError` | Handle invalid user inputs (e.g., entering text when number expected). |
| `except Exception as e` | General way to catch exceptions and inspect error messages. |
| `FileNotFoundError`, `FileExistsError` | Specific exceptions for missing or duplicate files. |
| `range()` integers only | Python’s `range()` only works with integers, not floats. |
| `exit(0)` | Immediately terminates program with status code 0 (success). |
| `from random import randint` | Import and use `randint(a,b)` to generate random numbers. |
| Underscores in big numbers | Python supports `1_000_000` for readability. |
| `isalpha()` | Checks if string contains only letters. |
| `isupper()` / `islower()` | Checks if string is uppercase / lowercase. |
| `isspace()` | Checks if string is only whitespace. |
| `ispunct()` | (Not built-in, but often custom-checked) → punctuation detection. |

---

## 📖 Discussion Questions  

- Why do we need **exception handling** (`try-except`) instead of just trusting user input?  
- In the **Drunkard’s Walk**, why doesn’t the drunkard stay close to (0,0) on average?  
- For the **Predator-Prey simulation**, what do the constants *A, B, C, D* represent in real ecosystems?  
- Why is using a **transformer** in audio devices better than connecting a speaker directly?  

---

## 📂 Lab Structure  

All solutions are available under:  
`LABS/LAB05`  

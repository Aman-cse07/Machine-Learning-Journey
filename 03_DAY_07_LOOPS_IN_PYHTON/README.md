# 🐍 Python Learning Journey - Day 03

# 🔍 Find the Largest of Three Numbers Using Nested `if` Statements

Welcome to **Day 03** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Nested `if` Statements** in Python by finding the **largest of three numbers**. Nested `if` statements are useful when one condition depends on the result of another condition.

---

# 📚 Topics Covered

- ✅ What is a Nested `if` Statement?
- ✅ Multiple Variable Assignment
- ✅ Comparison Operators
- ✅ Finding the Largest of Three Numbers
- ✅ Program Explanation
- ✅ Practice Program

---

# 📖 What is a Nested `if` Statement?

A **Nested `if` Statement** is an `if` statement placed inside another `if` statement.

It is used when one condition should be checked only after another condition is satisfied.

### Syntax

```python
if condition1:
    if condition2:
        # Code
    else:
        # Code
else:
    # Code
```

---

# 📖 Multiple Variable Assignment

Python allows assigning multiple variables in a single line.

### Example

```python
a, b, c = 10, 20, 30
```

This is equivalent to:

```python
a = 10
b = 20
c = 30
```

---

# 💻 Practice Program

```python
a, b, c = 10, 20, 30

if a > b:
    if a > c:
        print("a is the largest number")
else:
    if b > c:
        print("b is the largest number")
    else:
        print("c is the largest number")
```

---

# 📌 Program Explanation

### Step 1: Assign Values

```python
a, b, c = 10, 20, 30
```

Assigns:

- `a = 10`
- `b = 20`
- `c = 30`

---

### Step 2: Compare `a` and `b`

```python
if a > b:
```

Checks whether **a** is greater than **b**.

Since:

```text
10 > 20
```

is **False**, the program moves to the `else` block.

---

### Step 3: Compare `b` and `c`

```python
if b > c:
```

Checks:

```text
20 > 30
```

This is also **False**.

---

### Step 4: Execute the Final `else`

```python
print("c is the largest number")
```

Since neither `a` nor `b` is the largest, the program concludes that **c** is the largest number.

---

# 📤 Output

```text
c is the largest number
```

---

# 📊 Flow of Execution

```text
Start
   │
   ▼
Assign values to a, b, c
   │
   ▼
Is a > b ?
   │
 ┌─┴───────────┐
 │             │
Yes           No
 │             │
 ▼             ▼
Is a > c ?   Is b > c ?
 │             │
 ┌─┴───┐      ┌─┴───┐
 │     │      │     │
Yes   No     Yes    No
 │     │      │      │
 ▼     ▼      ▼      ▼
Print  -   Print   Print
 a         b         c
Largest   Largest  Largest
```

---

# ⚠️ Note

This program works correctly for the given values, but it does **not handle all cases**, especially when numbers are equal.

A more reliable approach is:

```python
if a >= b and a >= c:
    print("a is the largest number")
elif b >= a and b >= c:
    print("b is the largest number")
else:
    print("c is the largest number")
```

This version correctly handles equal values as well.

---

# 🌍 Real-World Applications

Finding the largest value is useful in:

- 📊 Finding the highest marks
- 🏆 Determining the winner
- 💰 Finding the highest salary
- 🌡️ Finding the maximum temperature
- 📈 Data analysis

---

# ⚡ Key Points

- A nested `if` is an `if` statement inside another `if`.
- Python supports assigning multiple variables in one line.
- Comparison operators return either `True` or `False`.
- Nested `if` statements help solve decision-making problems involving multiple conditions.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-03/
│   ├── largest_of_three.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Understand Nested `if` statements.
- Compare multiple values.
- Find the largest among three numbers.
- Write decision-making programs using conditional statements.

---

# 🚀 Challenge

Try modifying the program to:

- 🔹 Take the three numbers from the user using `input()`.
- 🔹 Find the **smallest** number.
- 🔹 Handle cases where two or all three numbers are equal.
- 🔹 Display both the largest and smallest numbers.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/controlflow.html
- **Python `if` Statements:** https://docs.python.org/3/reference/compound_stmts.html#if

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

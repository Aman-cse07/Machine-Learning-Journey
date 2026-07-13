# 🐍 Python Learning Journey - Day 03

# ➕ Arithmetic Operators in Python

Welcome to **Day 03** of my Python Learning Journey! 🚀

In this lesson, we explore **Arithmetic Operators** in Python. These operators are used to perform mathematical calculations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.

---

# 📚 Topics Covered

- ✅ Arithmetic Operators
- ✅ Addition Operator (`+`)
- ✅ Subtraction Operator (`-`)
- ✅ Multiplication Operator (`*`)
- ✅ Division Operator (`/`)
- ✅ Modulus Operator (`%`)
- ✅ Exponent Operator (`**`)
- ✅ Floor Division Operator (`//`)
- ✅ Practice Program

---

# 📖 What are Arithmetic Operators?

Arithmetic operators are symbols used to perform mathematical operations on numbers.

Python supports the following arithmetic operators:

| Operator | Name | Example |
|----------|------|---------|
| `+` | Addition | `a + b` |
| `-` | Subtraction | `a - b` |
| `*` | Multiplication | `a * b` |
| `/` | Division | `a / b` |
| `%` | Modulus (Remainder) | `a % b` |
| `**` | Exponent (Power) | `2 ** 3` |
| `//` | Floor Division | `a // b` |

---

# 💻 Practice Program

```python
a = 5
b = 6

sum = a + b
sub = a - b
multi = a * b
div = a / b
modulus = a % b
exponent = 2 ** 3
floor_division = a // b

print("Sum of a + b is :-", sum)
print("Sub of a - b is :-", sub)
print("Multi of a * b is :-", multi)
print("Div of a / b is :-", div)
print("Modulus of a % b is :-", modulus)
print("Exponent of 2 ** 3 is :-", exponent)
print("Floor Division of a // b is :-", floor_division)
```

---

# 📤 Output

```text
Sum of a + b is :- 11
Sub of a - b is :- -1
Multi of a * b is :- 30
Div of a / b is :- 0.8333333333333334
Modulus of a % b is :- 5
Exponent of 2 ** 3 is :- 8
Floor Division of a // b is :- 0
```

---

# 📌 Explanation

## ➕ Addition (`+`)

Adds two numbers.

```python
sum = a + b
```

Output:

```text
11
```

---

## ➖ Subtraction (`-`)

Subtracts one number from another.

```python
sub = a - b
```

Output:

```text
-1
```

---

## ✖️ Multiplication (`*`)

Multiplies two numbers.

```python
multi = a * b
```

Output:

```text
30
```

---

## ➗ Division (`/`)

Divides one number by another.

```python
div = a / b
```

Output:

```text
0.8333333333333334
```

> **Note:** The `/` operator always returns a **float** value.

---

## 🧮 Modulus (`%`)

Returns the remainder after division.

```python
modulus = a % b
```

Output:

```text
5
```

Since:

```
5 ÷ 6 = 0 remainder 5
```

---

## 🔥 Exponent (`**`)

Raises a number to the power of another number.

```python
exponent = 2 ** 3
```

Output:

```text
8
```

Explanation:

```
2 × 2 × 2 = 8
```

---

## 📐 Floor Division (`//`)

Returns only the integer part of the division result.

```python
floor_division = a // b
```

Output:

```text
0
```

Explanation:

```
5 ÷ 6 = 0.833...

Removing the decimal part gives:

0
```

---

# ⚖️ Operator Precedence

Python follows the **PEMDAS/BODMAS** rule while evaluating expressions.

Priority order:

1. Parentheses `()`
2. Exponent `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`

Example:

```python
print(5 + 2 * 3)
```

Output:

```text
11
```

---

# ⚡ Key Points

- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division (returns float)
- `%` → Remainder
- `**` → Power
- `//` → Integer Quotient (Floor Division)

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-03/
│   ├── arithmetic_operators.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Perform basic mathematical calculations in Python.
- Understand all arithmetic operators.
- Use arithmetic operators in real-world programs.
- Understand the difference between `/` and `//`.
- Calculate powers using `**`.
- Find remainders using `%`.

---

# 🚀 What's Next?

In the next lesson, we'll learn:

- Assignment Operators (`=`, `+=`, `-=`, `*=`, `/=`, etc.)
- Comparison Operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical Operators (`and`, `or`, `not`)

Stay tuned! 🎉

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** it and follow my Python Learning Journey!

# 🐍 Python Learning Journey - Day 05

# ⚡ Assignment, Comparison & Logical Operators in Python

Welcome to **Day 05** of my Python Learning Journey! 🚀

In this lesson, we will learn about three important categories of operators in Python:

- Assignment Operators
- Comparison Operators
- Logical Operators

These operators are widely used in decision-making, loops, conditions, and real-world programming.

---

# 📚 Topics Covered

- ✅ Assignment Operators
- ✅ Comparison Operators
- ✅ Logical Operators
- ✅ Truth Tables
- ✅ Practice Program

---

# 📖 What are Operators?

Operators are special symbols used to perform operations on variables and values.

Python provides several types of operators. In this lesson, we'll focus on:

- Assignment Operators
- Comparison Operators
- Logical Operators

---

# 📝 Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Assign value | `a = 5` |
| `+=` | Add and assign | `a += 3` |
| `-=` | Subtract and assign | `a -= 3` |
| `*=` | Multiply and assign | `a *= 2` |
| `/=` | Divide and assign | `a /= 2` |
| `%=` | Modulus and assign | `a %= 2` |
| `**=` | Exponent and assign | `a **= 2` |
| `//=` | Floor division and assign | `a //= 2` |

---

## 💻 Example

```python
a = 4 - 2
print(a)

b = 6

b += 3
print(b)

b -= 3
print(b)
```

### Output

```text
2
9
6
```

### Explanation

```python
b += 3
```

Equivalent to:

```python
b = b + 3
```

Similarly,

```python
b -= 3
```

Equivalent to:

```python
b = b - 3
```

---

# 🔍 Comparison Operators

Comparison operators compare two values and always return either **True** or **False**.

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | Equal to | `5 == 5` |
| `!=` | Not Equal to | `5 != 4` |
| `>` | Greater Than | `8 > 5` |
| `<` | Less Than | `4 < 8` |
| `>=` | Greater Than or Equal To | `5 >= 5` |
| `<=` | Less Than or Equal To | `5 <= 5` |

---

## 💻 Example

```python
d = 5 >= 5
print(d)

dd = 5 <= 5
print(dd)

c = 7 == 7
print(c)

e = 5 != 5
print(e)
```

### Output

```text
True
True
True
False
```

---

# 🧠 Logical Operators

Logical operators are used to combine multiple conditions.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# 🔹 OR Operator

The **`or`** operator returns **True** if at least one condition is True.

## Truth Table

| A | B | A or B |
|---|---|---------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Example

```python
print(True or False)
print(True or True)
print(False or True)
print(False or False)
```

### Output

```text
True
True
True
False
```

---

# 🔹 AND Operator

The **`and`** operator returns **True** only when both conditions are True.

## Truth Table

| A | B | A and B |
|---|---|----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Example

```python
print(True and False)
print(True and True)
print(False and True)
print(False and False)
```

### Output

```text
False
True
False
False
```

---

# 🔹 NOT Operator

The **`not`** operator reverses the Boolean value.

| Expression | Result |
|------------|--------|
| `not(True)` | False |
| `not(False)` | True |

### Example

```python
print(not(True))
print(not(False))
```

### Output

```text
False
True
```

---

# 💻 Complete Practice Program

```python
a = 6
b = 7
c = a + b
print(c)

# Assignment Operators
a = 4 - 2
print(a)

b = 6
b += 3
b -= 3
print(b)

# Comparison Operators
d = 5 >= 5
print(d)

dd = 5 <= 5
print(dd)

c = 7 == 7
print(c)

e = 5 != 5
print(e)

# Logical Operators

# OR
print("True or False is:-", True or False)
print("True or True is:-", True or True)
print("False or True is:-", False or True)
print("False or False is:-", False or False)

# AND
print("True and False is:-", True and False)
print("True and True is:-", True and True)
print("False and True is:-", False and True)
print("False and False is:-", False and False)

# NOT
print(not(True))
print(not(False))
```

---

# ⚡ Key Points

- Assignment operators modify and assign values.
- Comparison operators always return `True` or `False`.
- Logical operators combine multiple conditions.
- `or` returns `True` if at least one condition is true.
- `and` returns `True` only if all conditions are true.
- `not` reverses the Boolean value.

---

# 🌍 Real-World Uses

These operators are used in:

- 🔐 Login Authentication
- 🎓 Student Result Systems
- 🏦 Banking Applications
- 🛒 E-commerce Websites
- 🎮 Game Development
- 🤖 Artificial Intelligence
- 🌐 Web Development

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-05/
│   ├── operators.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Understand Assignment Operators.
- Compare values using Comparison Operators.
- Use Logical Operators in conditions.
- Read and understand Boolean expressions.
- Apply operators in real-world Python programs.

---

# 🚀 What's Next?

In **Day 06**, we'll learn about:

- User Input using `input()`
- Type Casting
- Taking Multiple Inputs
- Small Practice Programs

Stay tuned! 🎉

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

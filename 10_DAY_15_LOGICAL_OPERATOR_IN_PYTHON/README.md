# 🐍 Python Learning Journey - Logical Operators

# 🧠 Logical Operators in Python

Logical operators are used to **combine multiple conditions** and produce a Boolean result (`True` or `False`).

Python provides three logical operators:

- `and`
- `or`
- `not`

Logical operators are very important in **conditional statements**, loops, validation, authentication, and decision-making programs.

---

# 📚 Topics Covered

- ✅ What are Logical Operators?
- ✅ `and` Operator
- ✅ `or` Operator
- ✅ `not` Operator
- ✅ Truth Tables
- ✅ Logical Operators with Conditions
- ✅ Logical Operators with `if-else`
- ✅ Practical Examples
- ✅ Common Mistakes
- ✅ Practice Questions

---

# 📖 What are Logical Operators?

Logical operators are used to combine or modify Boolean expressions.

A Boolean expression can have only two possible values:

```text
True
False
```

For example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

We can combine multiple conditions using logical operators.

---

# 🔹 1. `and` Operator

The `and` operator returns `True` **only when both conditions are True**.

### Syntax

```python
condition1 and condition2
```

### Example

```python
age = 20
has_id = True

print(age >= 18 and has_id)
```

Output:

```text
True
```

Both conditions are true:

```text
age >= 18  → True
has_id     → True
```

Therefore:

```text
True and True → True
```

---

# 📊 Truth Table of `and`

| Condition A | Condition B | A `and` B |
|-------------|-------------|-----------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### Example

```python
print(True and True)
print(True and False)
print(False and True)
print(False and False)
```

Output:

```text
True
False
False
False
```

### ⭐ Remember

> **`and` requires ALL conditions to be True.**

---

# 🔹 2. `or` Operator

The `or` operator returns `True` when **at least one condition is True**.

### Syntax

```python
condition1 or condition2
```

### Example

```python
age = 16
has_permission = True

print(age >= 18 or has_permission)
```

Output:

```text
True
```

Here:

```text
age >= 18      → False
has_permission → True
```

Therefore:

```text
False or True → True
```

---

# 📊 Truth Table of `or`

| Condition A | Condition B | A `or` B |
|-------------|-------------|----------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### Example

```python
print(True or True)
print(True or False)
print(False or True)
print(False or False)
```

Output:

```text
True
True
True
False
```

### ⭐ Remember

> **`or` needs at least ONE condition to be True.**

---

# 🔹 3. `not` Operator

The `not` operator **reverses the Boolean value**.

### Syntax

```python
not condition
```

### Example

```python
print(not True)
print(not False)
```

Output:

```text
False
True
```

---

# 📊 Truth Table of `not`

| Condition | `not` Condition |
|-----------|-----------------|
| True | False |
| False | True |

### ⭐ Remember

> **`not` simply reverses True ↔ False.**

---

# 🔥 Comparison of Logical Operators

| Operator | Meaning | Result |
|----------|---------|--------|
| `and` | All conditions must be True | True only when all are True |
| `or` | At least one condition must be True | False only when all are False |
| `not` | Reverses the result | True becomes False |

---

# 💻 Logical Operators with Comparison Operators

Logical operators are commonly combined with comparison operators.

Example:

```python
age = 20
marks = 85

print(age >= 18 and marks >= 40)
```

Output:

```text
True
```

Here:

```text
age >= 18   → True
marks >= 40 → True
```

Therefore:

```text
True and True → True
```

---

# 🧠 Using `and` with `if`

```python
age = 20
marks = 75

if age >= 18 and marks >= 40:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Eligible
```

Both conditions must be satisfied.

---

# 🧠 Using `or` with `if`

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's a weekend")
else:
    print("It's a working day")
```

Output:

```text
It's a weekend
```

Only one condition needs to be true.

---

# 🧠 Using `not` with `if`

```python
is_logged_in = False

if not is_logged_in:
    print("Please login first")
else:
    print("Welcome!")
```

Output:

```text
Please login first
```

Because:

```text
not False → True
```

---

# 🎓 Student Eligibility Example

Logical operators are useful for checking multiple conditions.

```python
age = 20
marks = 70

if age >= 18 and marks >= 60:
    print("Student is eligible")
else:
    print("Student is not eligible")
```

Output:

```text
Student is eligible
```

---

# 🔐 Login Example

```python
username = "Aman"
password = "1234"

if username == "Aman" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
```

Output:

```text
Login Successful
```

---

# 🎟️ Voting Eligibility Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
```

Output:

```text
You are eligible to vote
```

---

# 🛒 Shopping Example

Suppose a customer gets free delivery if they spend ₹500 or have a premium membership.

```python
amount = 300
premium_member = True

if amount >= 500 or premium_member:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")
```

Output:

```text
Free Delivery
```

---

# ⚡ Multiple Logical Operators

Python allows us to combine multiple logical operators.

Example:

```python
age = 20
marks = 85
attendance = 80

if age >= 18 and marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Eligible
```

All three conditions must be true.

---

# 🧩 Using Parentheses

Parentheses can be used to make complex conditions easier to understand.

```python
age = 20
marks = 85

if (age >= 18 and marks >= 60) or marks == 100:
    print("Eligible")
else:
    print("Not Eligible")
```

Output:

```text
Eligible
```

---

# ⚠️ Common Mistakes

### ❌ Mistake 1: Using `&` instead of `and`

```python
if age >= 18 & marks >= 40:
```

For logical conditions, use:

```python
if age >= 18 and marks >= 40:
```

`&` is a **bitwise AND operator**, not the normal logical `and` operator.

---

### ❌ Mistake 2: Confusing `=` and `==`

Assignment:

```python
age = 18
```

Comparison:

```python
age == 18
```

Use `==` when comparing values.

---

# 📌 Operator Precedence

When multiple operators are used, Python follows an order of evaluation.

For logical operators, the order is:

```text
not
and
or
```

Example:

```python
print(True or False and False)
```

Python evaluates `and` first:

```text
False and False → False
True or False   → True
```

Output:

```text
True
```

For complicated expressions, using parentheses is recommended:

```python
print(True or (False and False))
```

---

# 📋 Quick Revision Table

| Operator | Example | Result |
|----------|---------|--------|
| `and` | `True and True` | `True` |
| `and` | `True and False` | `False` |
| `or` | `True or False` | `True` |
| `or` | `False or False` | `False` |
| `not` | `not True` | `False` |
| `not` | `not False` | `True` |

---

# 🌍 Real-World Applications

Logical operators are widely used in:

- 🔐 Login Authentication
- 🎓 Student Eligibility
- 🏦 Banking Systems
- 🛒 E-Commerce Websites
- 🎮 Game Development
- 🌐 Web Applications
- 🤖 Artificial Intelligence
- 📊 Data Validation
- 🔒 Security Systems

---

# 💻 Complete Practice Program

```python
# AND Operator

print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)


# OR Operator

print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)


# NOT Operator

print("not True:", not True)
print("not False:", not False)
```

### Output

```text
True and True: True
True and False: False
False and True: False
False and False: False

True or True: True
True or False: True
False or True: True
False or False: False

not True: False
not False: True
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Understand logical operators in Python.
- Use `and`, `or`, and `not`.
- Create and understand truth tables.
- Combine comparison and logical operators.
- Use logical operators with `if-else`.
- Build real-world decision-making programs.

---

# 🚀 Practice Questions

### Question 1

Check whether a person is eligible to vote.

```text
Age >= 18
```

---

### Question 2

Check whether a student passed both subjects.

```text
Maths >= 40 AND Science >= 40
```

---

### Question 3

Check whether a person can enter a club.

```text
Age >= 18 OR Has_Permission == True
```

---

### Question 4

Check whether a user is **not logged in**.

---

### Question 5

Create a program that checks whether a student is eligible for an exam based on:

```text
Attendance >= 75
AND
Marks >= 40
```

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-10/
│   ├── logical_operators.py
│   └── README.md
│
└── Projects/
```

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- **Python Operators:** https://docs.python.org/3/tutorial/introduction.html

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

# 🐍 Python Learning Journey - Day 03

# 🎓 Grade Calculator Using `if-elif-else` in Python

Welcome to **Day 03** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Conditional Statements** in Python using the **`if`**, **`elif`**, and **`else`** keywords. Conditional statements help a program make decisions based on user input or specific conditions.

---

# 📚 Topics Covered

- ✅ What are Conditional Statements?
- ✅ The `if` Statement
- ✅ The `elif` Statement
- ✅ The `else` Statement
- ✅ User Input with `input()`
- ✅ Type Casting using `int()`
- ✅ Grade Calculator Program

---

# 📖 What are Conditional Statements?

Conditional statements allow a program to execute different blocks of code depending on whether a condition is **True** or **False**.

They are used to make decisions in a program.

For example:

- Checking exam results
- Login authentication
- ATM transactions
- Voting eligibility
- Grade calculation

---

# 🧩 Syntax of `if-elif-else`

```python
if condition:
    # Code executes if condition is True

elif another_condition:
    # Code executes if this condition is True

else:
    # Code executes if none of the above conditions are True
```

---

# 💻 Grade Calculator Program

```python
marks = int(input("Enter your marks: "))

if 0 <= marks <= 40:
    print("The grade is D")
elif 40 < marks <= 60:
    print("The grade is C")
elif 60 < marks <= 80:
    print("The grade is B")
elif 80 < marks <= 100:
    print("The grade is A")
else:
    print("Invalid marks")
```

---

# 📌 Program Explanation

### Step 1: Take Input from the User

```python
marks = int(input("Enter your marks: "))
```

- `input()` takes input from the user.
- `int()` converts the input from a string to an integer.

Example:

```text
Enter your marks: 75
```

---

### Step 2: Check Marks Between 0 and 40

```python
if 0 <= marks <= 40:
```

If the marks are between **0 and 40**, the program prints:

```text
The grade is D
```

---

### Step 3: Check Marks Between 41 and 60

```python
elif 40 < marks <= 60:
```

If the marks are greater than **40** and less than or equal to **60**, the output is:

```text
The grade is C
```

---

### Step 4: Check Marks Between 61 and 80

```python
elif 60 < marks <= 80:
```

If the marks are greater than **60** and less than or equal to **80**, the output is:

```text
The grade is B
```

---

### Step 5: Check Marks Between 81 and 100

```python
elif 80 < marks <= 100:
```

If the marks are greater than **80** and less than or equal to **100**, the output is:

```text
The grade is A
```

---

### Step 6: Invalid Marks

```python
else:
    print("Invalid marks")
```

If the user enters:

- Negative marks
- Marks greater than 100

The program prints:

```text
Invalid marks
```

---

# 📤 Sample Outputs

### Example 1

```text
Enter your marks: 35
The grade is D
```

---

### Example 2

```text
Enter your marks: 55
The grade is C
```

---

### Example 3

```text
Enter your marks: 72
The grade is B
```

---

### Example 4

```text
Enter your marks: 92
The grade is A
```

---

### Example 5

```text
Enter your marks: 120
Invalid marks
```

---

# 📊 Grade Table

| Marks Range | Grade |
|-------------|-------|
| 0 – 40 | D |
| 41 – 60 | C |
| 61 – 80 | B |
| 81 – 100 | A |
| Below 0 or Above 100 | Invalid |

---

# 🎯 Why Use `if-elif-else`?

Conditional statements are commonly used in:

- 🎓 Student Result Systems
- 🏦 Banking Applications
- 🛒 Shopping Websites
- 🎮 Games
- 🔐 Login Systems
- 🚦 Traffic Signal Control
- 📊 Data Validation

---

# ⚡ Key Points

- `if` checks the first condition.
- `elif` checks additional conditions if the previous ones are false.
- `else` runs when none of the conditions are true.
- `input()` reads data from the user.
- `int()` converts input to an integer.
- Only **one block** of the `if-elif-else` chain executes.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-03/
│   ├── grade_calculator.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Understand conditional statements.
- Use `if`, `elif`, and `else`.
- Take input from the user.
- Convert input using `int()`.
- Build simple decision-making programs.

---

# 🚀 Challenge

Modify the program to display:

| Grade | Marks |
|--------|-------|
| A+ | 91 – 100 |
| A | 81 – 90 |
| B | 61 – 80 |
| C | 41 – 60 |
| D | 0 – 40 |

Can you also display **"Pass"** or **"Fail"** based on the grade?

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/controlflow.html
- **Python `if` Statement:** https://docs.python.org/3/reference/compound_stmts.html#if

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** it and follow my Python Learning Journey!

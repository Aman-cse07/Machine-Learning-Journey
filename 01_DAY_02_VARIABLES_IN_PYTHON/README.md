# 🐍 Python Learning Journey - Day 02

Welcome to **Day 02** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Variables** in Python. Variables are one of the most fundamental concepts in programming because they allow us to store and manipulate data.

---

# 📚 Topics Covered

- ✅ What are Variables?
- ✅ Rules for Naming Variables
- ✅ Creating Variables
- ✅ Variable Assignment
- ✅ Different Data Types
- ✅ The `type()` Function
- ✅ Boolean Values
- ✅ None Data Type
- ✅ Practice Program

---

# 📖 What is a Variable?

A **variable** is a named memory location used to store data. It acts as a container that holds values, which can be used and modified throughout the program.

Think of a variable as a **labeled box** where you can keep information such as your name, age, marks, etc.

---

# 🧠 Syntax

```python
variable_name = value
```

Example:

```python
name = "Aman Kumar"
age = 23
marks = 89.45
```

---

# 📝 Rules for Naming Variables

- ✅ Variable names can contain letters, numbers, and underscores (`_`).
- ✅ Variable names must start with a letter or an underscore.
- ❌ Variable names cannot start with a number.
- ❌ Variable names cannot contain spaces.
- ❌ Python keywords cannot be used as variable names.
- ✅ Variable names are **case-sensitive**.

Example:

```python
student_name = "Aman"
Student_Name = "Rahul"

print(student_name)
print(Student_Name)
```

These are treated as **different variables**.

---

# 🔤 Variable Assignment

Python automatically determines the data type based on the assigned value.

Example:

```python
name = "Aman Kumar"
age = 23
marks = 89.45
```

---

# 📊 Common Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `str` | String (Text) | `"Aman"` |
| `int` | Integer | `23` |
| `float` | Decimal Number | `89.45` |
| `bool` | Boolean | `True`, `False` |
| `NoneType` | Represents no value | `None` |

---

# 🔍 The `type()` Function

The `type()` function is used to find the data type of a variable.

Example:

```python
name = "Aman"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

# 💻 Practice Program

```python
name = "Aman Kumar"
age = 23
roll_no = 23707
marks = 89.45

print(name)
print(age)
print(roll_no)

print(type(name))
print(type(age))
print(type(roll_no))

print("My name is :-", name)
print("My age is :-", age)
print("My roll no. is :-", roll_no)

print(type(marks))

age2 = 25
old = True
a = None

print(type(age2))
print(type(old))
print(type(a))
```

---

# 📤 Output

```text
Aman Kumar
23
23707

<class 'str'>
<class 'int'>
<class 'int'>

My name is :- Aman Kumar
My age is :- 23
My roll no. is :- 23707

<class 'float'>
<class 'int'>
<class 'bool'>
<class 'NoneType'>
```

---

# 📌 Explanation

### String Variable

```python
name = "Aman Kumar"
```

Stores text data.

---

### Integer Variables

```python
age = 23
roll_no = 23707
```

Stores whole numbers.

---

### Float Variable

```python
marks = 89.45
```

Stores decimal numbers.

---

### Boolean Variable

```python
old = True
```

Stores either **True** or **False**.

---

### None Variable

```python
a = None
```

Represents the absence of any value.

---

### Printing Variables

```python
print(name)
```

Displays the value stored in the variable.

---

### Printing with Text

```python
print("My name is :-", name)
```

Prints both the text and the variable value.

Output:

```text
My name is :- Aman Kumar
```

---

### Finding Data Types

```python
print(type(name))
```

Output:

```text
<class 'str'>
```

Similarly,

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

---

# ⚡ Key Points

- Variables store data.
- Python does not require declaring a data type.
- Variable names should be meaningful.
- Use the `type()` function to check the data type.
- Python is dynamically typed, meaning the data type is assigned automatically.

---

# 📂 Folder Structure

```
Python-Learning-Journey/
│
├── Day-02/
│   ├── variables.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing Day 02, you will be able to:

- Create variables in Python.
- Understand different data types.
- Print variable values.
- Use the `type()` function.
- Work with String, Integer, Float, Boolean, and None data types.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/introduction.html
- **Python Data Types:** https://docs.python.org/3/library/stdtypes.html

---

# 🚀 What's Next?

In **Day 03**, we'll learn about:

- Input from User (`input()`)
- Type Conversion
- Taking Multiple Inputs
- Practice Programs

Stay tuned! 🎉

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

# 🐍 Python Learning Journey - Day 04

# 🔧 Functions in Python

Welcome to **Day 04** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Functions** in Python. Functions help us organize our code into reusable blocks, making programs cleaner, easier to understand, and easier to maintain.

---

# 📚 Topics Covered

- ✅ What is a Function?
- ✅ Creating a Function
- ✅ Calling a Function
- ✅ Function with `print()`
- ✅ Function with `return`
- ✅ Practice Program

---

# 📖 What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, we can write it once inside a function and call it whenever needed.

### Benefits of Functions

- ♻️ Reusable Code
- 📖 Better Readability
- 🛠️ Easy to Maintain
- 🚀 Reduces Code Duplication
- 📂 Makes Programs Modular

---

# 🧩 Syntax of a Function

```python
def function_name():
    # Function body
    print("Hello World")

function_name()
```

### Explanation

- `def` → Keyword used to define a function.
- `function_name` → Name of the function.
- `()` → Parentheses used for parameters (if any).
- `:` → Indicates the start of the function body.
- Indentation is mandatory in Python.
- Call the function using its name followed by `()`.

---

# 💻 Practice Program

```python
def Bpmce():
    print("BPMCE, MADHEPURA")

Bpmce()

def self():
    print("Aman Kumar 23157128040 CSE (AI & ML)")

self()

def self1():
    return "Aman Kumar 23707 CSE (AI & ML)"

print(self1())
```

---

# 📌 Program Explanation

## Function 1

```python
def Bpmce():
    print("BPMCE, MADHEPURA")
```

This function prints the name of the college.

Calling the function:

```python
Bpmce()
```

### Output

```text
BPMCE, MADHEPURA
```

---

## Function 2

```python
def self():
    print("Aman Kumar 23157128040 CSE (AI & ML)")
```

This function prints personal information.

Calling the function:

```python
self()
```

### Output

```text
Aman Kumar 23157128040 CSE (AI & ML)
```

---

## Function 3

```python
def self1():
    return "Aman Kumar 23707 CSE (AI & ML)"
```

This function **returns** a string instead of printing it.

Calling the function:

```python
print(self1())
```

### Output

```text
Aman Kumar 23707 CSE (AI & ML)
```

---

# 🖨️ `print()` vs `return`

## Using `print()`

```python
def greet():
    print("Hello")
```

- Displays the output directly.
- Does not return a value.

---

## Using `return`

```python
def greet():
    return "Hello"

print(greet())
```

- Returns a value to the caller.
- The returned value can be stored in a variable or used in expressions.

---

# 📤 Complete Output

```text
BPMCE, MADHEPURA
Aman Kumar 23157128040 CSE (AI & ML)
Aman Kumar 23707 CSE (AI & ML)
```

---

# 🌍 Real-World Applications of Functions

Functions are used in almost every Python application, including:

- 🌐 Web Development
- 🤖 Artificial Intelligence
- 📊 Data Analysis
- 🎮 Game Development
- 🔒 Cybersecurity
- 📱 Desktop Applications
- ⚙️ Automation Scripts

---

# ⚡ Key Points

- Functions are defined using the `def` keyword.
- A function executes only when it is called.
- Functions help avoid repeating code.
- `print()` displays output directly.
- `return` sends a value back to the caller.
- Function names should be meaningful and follow Python naming conventions.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-04/
│   ├── functions.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create your own functions.
- Call functions in Python.
- Understand the difference between `print()` and `return`.
- Write reusable and organized code using functions.

---

# 🚀 Challenge

Try creating the following functions:

### Challenge 1

Create a function that prints your college name.

```python
def college():
    pass
```

---

### Challenge 2

Create a function that returns your favorite programming language.

Example Output:

```text
Python
```

---

### Challenge 3

Create a function that returns the sum of two numbers.

Example:

```python
def add(a, b):
    return a + b
```

Output:

```text
30
```

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- **Python Functions:** https://docs.python.org/3/library/functions.html

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

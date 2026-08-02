# 🐍 Python Learning Journey - Day 05

# 🔤 Strings in Python

Welcome to **Day 05** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Strings** in Python. Strings are one of the most commonly used data types and are used to store and manipulate text.

---

# 📚 Topics Covered

- ✅ What is a String?
- ✅ Creating Strings
- ✅ Types of Quotes
- ✅ String Indexing
- ✅ Negative Indexing
- ✅ String Slicing
- ✅ String Immutability
- ✅ Common String Operations
- ✅ String Methods
- ✅ Practice Examples

---

# 📖 What is a String?

A **String** is a sequence of characters enclosed within **single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`)**.

Strings can contain:

- Letters
- Numbers
- Symbols
- Spaces
- Special Characters

Example:

```python
name = "Aman Kumar"
```

---

# ✍️ Creating Strings

## Using Single Quotes

```python
name = 'Aman'
```

---

## Using Double Quotes

```python
name = "Aman"
```

---

## Using Triple Quotes

```python
paragraph = """
Python is an easy programming language.
It is beginner-friendly.
"""
```

Triple quotes are mainly used for **multiline strings**.

---

# 🔢 String Indexing

Each character in a string has an index.

Example:

```python
name = "Python"
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |

Example:

```python
print(name[0])
print(name[3])
```

Output:

```text
P
h
```

---

# 🔄 Negative Indexing

Python also supports negative indexing.

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index | -6 | -5 | -4 | -3 | -2 | -1 |

Example:

```python
print(name[-1])
```

Output:

```text
n
```

---

# ✂️ String Slicing

String slicing extracts a portion of a string.

### Syntax

```python
string[start:end]
```

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

Another example:

```python
print(name[2:6])
```

Output:

```text
thon
```

---

# 🧊 String Immutability

Strings in Python are **immutable**, meaning they cannot be changed after creation.

Example:

```python
name = "Python"

# This will generate an error
name[0] = "J"
```

Instead, create a new string.

```python
name = "Jython"
```

---

# ➕ String Concatenation

Strings can be joined using the `+` operator.

Example:

```python
first = "Hello"
second = "World"

print(first + " " + second)
```

Output:

```text
Hello World
```

---

# ✖️ String Repetition

Use the `*` operator to repeat a string.

Example:

```python
print("Python " * 3)
```

Output:

```text
Python Python Python
```

---

# 🔍 Membership Operators

Check whether a character or word exists in a string.

Example:

```python
text = "Python"

print("P" in text)
print("Java" in text)
```

Output:

```text
True
False
```

---

# 🛠 Common String Methods

| Method | Description |
|---------|-------------|
| `upper()` | Converts to uppercase |
| `lower()` | Converts to lowercase |
| `title()` | Converts to title case |
| `capitalize()` | Capitalizes first letter |
| `strip()` | Removes spaces from both ends |
| `replace()` | Replaces text |
| `find()` | Finds substring |
| `count()` | Counts occurrences |
| `split()` | Splits string into a list |
| `join()` | Joins list into a string |
| `startswith()` | Checks starting text |
| `endswith()` | Checks ending text |

---

# 💻 Practice Examples

## Convert to Uppercase

```python
text = "python"

print(text.upper())
```

Output:

```text
PYTHON
```

---

## Convert to Lowercase

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

---

## Replace Text

```python
text = "Hello Python"

print(text.replace("Python", "World"))
```

Output:

```text
Hello World
```

---

## Count Characters

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## Find Text

```python
text = "Python Programming"

print(text.find("Program"))
```

Output:

```text
7
```

---

## Split String

```python
text = "Apple Mango Banana"

print(text.split())
```

Output:

```text
['Apple', 'Mango', 'Banana']
```

---

## Join Strings

```python
fruits = ["Apple", "Banana", "Mango"]

print(", ".join(fruits))
```

Output:

```text
Apple, Banana, Mango
```

---

# ⚡ Key Points

- Strings are enclosed within quotes.
- Strings are immutable.
- Indexing starts from **0**.
- Negative indexing starts from **-1**.
- Slicing extracts a portion of a string.
- Python provides many built-in string methods.

---

# 🌍 Real-World Applications

Strings are used in:

- 🌐 Web Development
- 🤖 Artificial Intelligence
- 📧 Email Processing
- 🔐 Password Validation
- 📄 Text Processing
- 💬 Chat Applications
- 📊 Data Analysis

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-05/
│   ├── strings.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create strings in Python.
- Access characters using indexing.
- Extract text using slicing.
- Concatenate and repeat strings.
- Use common string methods.
- Understand string immutability.

---

# 🚀 Challenge

Try solving these problems:

1. Print the first and last character of a string.
2. Reverse a string using slicing.
3. Count the number of vowels in a string.
4. Check whether a word is a palindrome.
5. Replace all spaces with underscores.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
- **Python String Methods:** https://docs.python.org/3/library/stdtypes.html#string-methods

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

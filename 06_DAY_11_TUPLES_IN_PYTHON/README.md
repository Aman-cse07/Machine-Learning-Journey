# 🐍 Python Learning Journey - Day 06

# 📦 Tuples in Python

Welcome to **Day 06** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Tuples** in Python. Tuples are used to store multiple items in a single variable. They are similar to lists, but unlike lists, **tuples are immutable**, meaning their elements cannot be changed after creation.

---

# 📚 Topics Covered

- ✅ What is a Tuple?
- ✅ Creating Tuples
- ✅ Tuple Characteristics
- ✅ Accessing Tuple Elements
- ✅ Tuple Indexing
- ✅ Negative Indexing
- ✅ Tuple Slicing
- ✅ Tuple Packing
- ✅ Tuple Unpacking
- ✅ Tuple Methods
- ✅ Built-in Functions
- ✅ Nested Tuples
- ✅ Tuple Operations
- ✅ Practice Examples

---

# 📖 What is a Tuple?

A **Tuple** is an ordered collection of items enclosed in **parentheses `()`**.

Unlike lists, tuples **cannot be modified** after they are created.

### Example

```python
student = ("Aman", 23, "CSE")
```

---

# ⭐ Characteristics of Tuples

- Ordered
- Immutable (Cannot be modified)
- Allows duplicate values
- Supports indexing
- Supports slicing
- Can store multiple data types

---

# ✍️ Creating Tuples

## Empty Tuple

```python
empty_tuple = ()
```

---

## Tuple with Integers

```python
numbers = (10, 20, 30)
```

---

## Tuple with Strings

```python
fruits = ("Apple", "Banana", "Mango")
```

---

## Mixed Data Types

```python
data = ("Aman", 23, 89.5, True)
```

---

## Single Element Tuple

```python
number = (10,)
```

> **Note:** The comma is mandatory for a single-element tuple.

Incorrect:

```python
number = (10)
```

This is treated as an integer, not a tuple.

---

# 🔢 Tuple Indexing

Example

```python
fruits = ("Apple", "Banana", "Mango")
```

| Index | Value |
|------:|-------|
| 0 | Apple |
| 1 | Banana |
| 2 | Mango |

Example

```python
print(fruits[0])
print(fruits[2])
```

Output

```text
Apple
Mango
```

---

# 🔄 Negative Indexing

| Index | Value |
|------:|-------|
| -1 | Mango |
| -2 | Banana |
| -3 | Apple |

Example

```python
print(fruits[-1])
```

Output

```text
Mango
```

---

# ✂️ Tuple Slicing

Syntax

```python
tuple_name[start:end]
```

Example

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output

```text
(20, 30, 40)
```

---

# 📥 Accessing Tuple Elements

```python
student = ("Aman", 23, "CSE")

print(student[0])
print(student[2])
```

Output

```text
Aman
CSE
```

---

# ❌ Tuple Immutability

Tuples cannot be changed.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

Output

```text
TypeError
```

---

# 📦 Tuple Packing

Packing means storing multiple values into one tuple.

```python
student = ("Aman", 23, "CSE")
```

---

# 📤 Tuple Unpacking

```python
name, age, course = ("Aman", 23, "CSE")

print(name)
print(age)
print(course)
```

Output

```text
Aman
23
CSE
```

---

# ➕ Tuple Operations

## Concatenation

```python
tuple1 = (1, 2)
tuple2 = (3, 4)

print(tuple1 + tuple2)
```

Output

```text
(1, 2, 3, 4)
```

---

## Repetition

```python
numbers = (1, 2)

print(numbers * 3)
```

Output

```text
(1, 2, 1, 2, 1, 2)
```

---

# 🔍 Membership Operators

```python
fruits = ("Apple", "Banana", "Mango")

print("Apple" in fruits)
print("Orange" in fruits)
```

Output

```text
True
False
```

---

# 🛠 Tuple Methods

Python tuples have only **two built-in methods**.

| Method | Description |
|---------|-------------|
| `count()` | Counts occurrences of an element |
| `index()` | Returns the index of an element |

---

# 🔹 `count()`

Returns how many times a value appears.

```python
numbers = (1, 2, 3, 2, 2, 5)

print(numbers.count(2))
```

Output

```text
3
```

---

# 🔹 `index()`

Returns the first index of a value.

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

Output

```text
2
```

---

# 🔧 Built-in Functions Used with Tuples

## `len()`

Returns the number of elements.

```python
numbers = (10, 20, 30)

print(len(numbers))
```

Output

```text
3
```

---

## `max()`

Returns the largest value.

```python
numbers = (10, 50, 30)

print(max(numbers))
```

Output

```text
50
```

---

## `min()`

Returns the smallest value.

```python
numbers = (10, 50, 30)

print(min(numbers))
```

Output

```text
10
```

---

## `sum()`

Returns the sum of all numeric elements.

```python
numbers = (10, 20, 30)

print(sum(numbers))
```

Output

```text
60
```

---

## `sorted()`

Returns a sorted list.

```python
numbers = (40, 10, 30)

print(sorted(numbers))
```

Output

```text
[10, 30, 40]
```

---

## `tuple()`

Converts an iterable into a tuple.

```python
numbers = tuple([1, 2, 3])

print(numbers)
```

Output

```text
(1, 2, 3)
```

---

# 🧩 Nested Tuples

```python
matrix = (
    (1, 2),
    (3, 4)
)

print(matrix[1][0])
```

Output

```text
3
```

---

# 🌍 Real-World Applications

Tuples are commonly used in:

- 📍 Storing coordinates (x, y)
- 📅 Date and time values
- 📊 Database records
- 🌐 API responses
- 🎮 Game development
- 📈 Data analysis

---

# ⚖️ Difference Between List and Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[]` | `()` |
| Mutable | ✅ Yes | ❌ No |
| Ordered | ✅ Yes | ✅ Yes |
| Duplicate Values | ✅ Yes | ✅ Yes |
| Faster | ❌ | ✅ |
| Methods | Many | Only `count()` and `index()` |

---

# ⚡ Key Points

- Tuples are immutable.
- Tuples use parentheses `()`.
- Tuples support indexing and slicing.
- Duplicate values are allowed.
- Only two tuple methods are available:
  - `count()`
  - `index()`
- Built-in functions like `len()`, `max()`, `min()`, and `sum()` work with tuples.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-06/
│   ├── tuples.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create tuples.
- Access tuple elements.
- Understand tuple immutability.
- Perform tuple packing and unpacking.
- Use tuple methods.
- Apply built-in functions with tuples.
- Differentiate between lists and tuples.

---

# 🚀 Practice Questions

1. Create a tuple of five numbers and print the third element.
2. Count how many times a value appears in a tuple.
3. Find the index of a given element.
4. Find the maximum and minimum values in a tuple.
5. Calculate the sum of all elements in a tuple.
6. Convert a list into a tuple.
7. Create a nested tuple and access an inner element.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
- **Built-in Functions:** https://docs.python.org/3/library/functions.html

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

# 🐍 Python Learning Journey - Day 10

# 📋 Lists in Python

Welcome to **Day 06** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Lists** in Python. Lists are one of the most powerful and commonly used data structures in Python. They allow us to store multiple values in a single variable and are widely used in real-world applications.

---

# 📚 Topics Covered

- ✅ What is a List?
- ✅ Creating Lists
- ✅ Characteristics of Lists
- ✅ List Indexing
- ✅ Negative Indexing
- ✅ List Slicing
- ✅ Accessing List Elements
- ✅ Updating List Elements
- ✅ Adding Elements
- ✅ Removing Elements
- ✅ List Methods
- ✅ Nested Lists
- ✅ List Operations
- ✅ Practice Examples

---

# 📖 What is a List?

A **List** is an ordered and mutable (changeable) collection of items.

Lists can store different types of data in a single collection, such as integers, strings, floats, and even other lists.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]
```

---

# ✍️ Creating a List

### Empty List

```python
my_list = []
```

---

### List of Integers

```python
numbers = [10, 20, 30, 40]
```

---

### List of Strings

```python
names = ["Aman", "Rahul", "Priya"]
```

---

### Mixed Data Types

```python
data = ["Aman", 21, 89.5, True]
```

---

### Nested List

```python
matrix = [[1, 2], [3, 4]]
```

---

# ⭐ Characteristics of Lists

- Ordered
- Mutable (can be modified)
- Allows duplicate values
- Can store multiple data types
- Supports indexing and slicing

---

# 🔢 List Indexing

Lists use **zero-based indexing**.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]
```

| Index | Value |
|------:|-------|
| 0 | Apple |
| 1 | Banana |
| 2 | Mango |

Example:

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

Negative indexing starts from the end.

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

# ✂️ List Slicing

Syntax

```python
list_name[start:end]
```

Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output

```text
[20, 30, 40]
```

---

# 📥 Accessing Elements

```python
colors = ["Red", "Green", "Blue"]

print(colors[1])
```

Output

```text
Green
```

---

# ✏️ Updating Elements

Lists are mutable.

Example

```python
colors = ["Red", "Green", "Blue"]

colors[1] = "Yellow"

print(colors)
```

Output

```text
['Red', 'Yellow', 'Blue']
```

---

# ➕ Adding Elements

## append()

Adds an element at the end.

```python
fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)
```

Output

```text
['Apple', 'Banana', 'Mango']
```

---

## insert()

Adds an element at a specific position.

```python
fruits.insert(1, "Orange")
```

Output

```text
['Apple', 'Orange', 'Banana', 'Mango']
```

---

## extend()

Adds multiple elements.

```python
fruits.extend(["Grapes", "Papaya"])
```

Output

```text
['Apple', 'Orange', 'Banana', 'Mango', 'Grapes', 'Papaya']
```

---

# ❌ Removing Elements

## remove()

Removes a specific value.

```python
fruits.remove("Banana")
```

---

## pop()

Removes an element using its index.

```python
fruits.pop(0)
```

---

## del

Deletes an element or the entire list.

```python
del fruits[1]
```

---

## clear()

Removes all elements.

```python
fruits.clear()
```

Output

```text
[]
```

---

# 🛠 Common List Methods

| Method | Description |
|---------|-------------|
| `append()` | Adds an item to the end |
| `insert()` | Inserts an item at a given position |
| `extend()` | Adds multiple items |
| `remove()` | Removes the specified item |
| `pop()` | Removes and returns an item |
| `clear()` | Removes all items |
| `index()` | Returns the index of an item |
| `count()` | Counts occurrences of an item |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `copy()` | Returns a copy of the list |

---

# 🔍 Finding Elements

## index()

```python
numbers = [10, 20, 30]

print(numbers.index(20))
```

Output

```text
1
```

---

## count()

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

Output

```text
3
```

---

# 📊 Sorting Lists

```python
numbers = [50, 20, 80, 10]

numbers.sort()

print(numbers)
```

Output

```text
[10, 20, 50, 80]
```

---

# 🔄 Reverse a List

```python
numbers.reverse()

print(numbers)
```

Output

```text
[80, 50, 20, 10]
```

---

# 📑 Copying a List

```python
list1 = [1, 2, 3]

list2 = list1.copy()

print(list2)
```

Output

```text
[1, 2, 3]
```

---

# 🔗 List Concatenation

```python
list1 = [1, 2]
list2 = [3, 4]

print(list1 + list2)
```

Output

```text
[1, 2, 3, 4]
```

---

# 🔁 Repeating a List

```python
numbers = [1, 2]

print(numbers * 3)
```

Output

```text
[1, 2, 1, 2, 1, 2]
```

---

# 🧩 Nested Lists

```python
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])
```

Output

```text
2
```

---

# 🌍 Real-World Applications

Lists are used in:

- 👨‍🎓 Student Management Systems
- 🛒 Shopping Cart Applications
- 🎮 Games
- 📊 Data Analysis
- 🤖 Machine Learning
- 🌐 Web Development
- 📱 Mobile Applications

---

# ⚡ Key Points

- Lists are ordered collections.
- Lists are mutable.
- Lists allow duplicate values.
- Lists support indexing and slicing.
- Lists can store different data types.
- Python provides many built-in list methods.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-6/
│   ├── lists.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create lists.
- Access list elements.
- Modify list values.
- Add and remove elements.
- Use common list methods.
- Work with nested lists.
- Perform list operations.

---

# 🚀 Challenge

Try solving these problems:

1. Find the largest number in a list.
2. Find the smallest number in a list.
3. Reverse a list without using `reverse()`.
4. Count even and odd numbers in a list.
5. Remove duplicate elements from a list.
6. Merge two lists.
7. Sort a list in descending order.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/datastructures.html
- **Python List Methods:** https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

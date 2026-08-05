# 🐍 Python Learning Journey - Day 08

# 🔷 Sets in Python

Welcome to **Day 08** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Sets** in Python. Sets are one of Python's built-in data structures used to store **unique and unordered** elements. They are commonly used for removing duplicates and performing mathematical set operations like union and intersection.

---

# 📚 Topics Covered

- ✅ What is a Set?
- ✅ Characteristics of Sets
- ✅ Creating Sets
- ✅ Empty Set
- ✅ Accessing Set Elements
- ✅ Adding Elements
- ✅ Updating Sets
- ✅ Removing Elements
- ✅ Set Methods
- ✅ Built-in Functions
- ✅ Set Operations
- ✅ Frozen Sets
- ✅ Real-World Applications

---

# 📖 What is a Set?

A **Set** is an unordered collection of **unique** elements.

Unlike lists and tuples, sets do not allow duplicate values and do not support indexing.

### Example

```python
fruits = {"Apple", "Banana", "Mango"}
```

---

# ⭐ Characteristics of Sets

- Stores only unique values
- Unordered collection
- Mutable (elements can be added or removed)
- Does not support indexing
- Does not allow duplicate values
- Can store different data types
- Faster searching compared to lists

---

# ✍️ Creating Sets

## Empty Set

```python
empty_set = set()
```

> **Note:** `{}` creates an empty dictionary, **not** an empty set.

---

## Set of Integers

```python
numbers = {10, 20, 30, 40}
```

---

## Set of Strings

```python
fruits = {"Apple", "Banana", "Mango"}
```

---

## Mixed Data Types

```python
data = {"Aman", 23, 89.5, True}
```

---

## Creating a Set from a List

```python
numbers = set([1, 2, 3, 4])
```

Output

```text
{1, 2, 3, 4}
```

---

# 🔍 Duplicate Values

Sets automatically remove duplicate elements.

```python
numbers = {10, 20, 20, 30, 40, 40}

print(numbers)
```

Output

```text
{10, 20, 30, 40}
```

---

# 📥 Accessing Set Elements

Sets do **not** support indexing.

❌ Incorrect

```python
numbers = {10, 20, 30}

print(numbers[0])
```

Output

```text
TypeError
```

---

✅ Correct Way

```python
for item in numbers:
    print(item)
```

---

# ➕ Adding Elements

## `add()`

Adds one element.

```python
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)
```

Output

```text
{'Apple', 'Banana', 'Mango'}
```

---

## `update()`

Adds multiple elements.

```python
fruits.update(["Orange", "Grapes"])

print(fruits)
```

---

# ❌ Removing Elements

## `remove()`

Removes a specific element.

```python
fruits.remove("Apple")
```

> Raises an error if the element is not present.

---

## `discard()`

Removes an element safely.

```python
fruits.discard("Apple")
```

> Does **not** raise an error if the element is missing.

---

## `pop()`

Removes a random element.

```python
fruits.pop()
```

---

## `clear()`

Removes all elements.

```python
fruits.clear()
```

---

# 🔄 Looping Through a Set

```python
fruits = {"Apple", "Banana", "Mango"}

for fruit in fruits:
    print(fruit)
```

---

# 🛠 Set Methods

## 1️⃣ `add()`

Adds one element.

```python
numbers.add(50)
```

---

## 2️⃣ `update()`

Adds multiple elements.

```python
numbers.update([60, 70])
```

---

## 3️⃣ `remove()`

Removes an element.

```python
numbers.remove(20)
```

---

## 4️⃣ `discard()`

Removes an element without raising an error.

```python
numbers.discard(100)
```

---

## 5️⃣ `pop()`

Removes and returns a random element.

```python
numbers.pop()
```

---

## 6️⃣ `clear()`

Removes all elements.

```python
numbers.clear()
```

---

## 7️⃣ `copy()`

Returns a shallow copy of the set.

```python
new_numbers = numbers.copy()
```

---

# ➕ Set Operations

## Union

Returns all unique elements from both sets.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
```

Output

```text
{1, 2, 3, 4, 5}
```

---

## Intersection

Returns common elements.

```python
print(A.intersection(B))
```

Output

```text
{3}
```

---

## Difference

Returns elements present in the first set only.

```python
print(A.difference(B))
```

Output

```text
{1, 2}
```

---

## Symmetric Difference

Returns elements present in either set but not both.

```python
print(A.symmetric_difference(B))
```

Output

```text
{1, 2, 4, 5}
```

---

# 🔁 Update Operations

## `intersection_update()`

Keeps only common elements.

```python
A.intersection_update(B)
```

---

## `difference_update()`

Removes common elements.

```python
A.difference_update(B)
```

---

## `symmetric_difference_update()`

Updates with the symmetric difference.

```python
A.symmetric_difference_update(B)
```

---

# 🔍 Set Relationship Methods

## `issubset()`

Checks whether one set is a subset of another.

```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
```

Output

```text
True
```

---

## `issuperset()`

Checks whether one set is a superset of another.

```python
print(B.issuperset(A))
```

Output

```text
True
```

---

## `isdisjoint()`

Checks whether two sets have no common elements.

```python
A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
```

Output

```text
True
```

---

# ❄️ Frozen Set

A **Frozen Set** is an immutable version of a set.

```python
numbers = frozenset([1, 2, 3, 4])

print(numbers)
```

Output

```text
frozenset({1, 2, 3, 4})
```

---

# 🔧 Built-in Functions

## `len()`

Returns the number of elements.

```python
numbers = {10, 20, 30}

print(len(numbers))
```

Output

```text
3
```

---

## `max()`

Returns the largest element.

```python
print(max(numbers))
```

---

## `min()`

Returns the smallest element.

```python
print(min(numbers))
```

---

## `sum()`

Returns the sum of all elements.

```python
print(sum(numbers))
```

---

## `sorted()`

Returns a sorted list.

```python
print(sorted(numbers))
```

Output

```text
[10, 20, 30]
```

---

## `type()`

Returns the data type.

```python
print(type(numbers))
```

Output

```text
<class 'set'>
```

---

# ⚖️ Difference Between List, Tuple, Dictionary & Set

| Feature | List | Tuple | Dictionary | Set |
|---------|------|--------|------------|-----|
| Syntax | `[]` | `()` | `{key:value}` | `{}` |
| Ordered | ✅ | ✅ | ✅ (Python 3.7+) | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicate Values | ✅ | ✅ | Keys ❌ | ❌ |
| Indexing | ✅ | ✅ | By Key | ❌ |

---

# 🌍 Real-World Applications

Sets are commonly used in:

- 📊 Removing duplicate values
- 🎓 Student registration systems
- 🌐 Database operations
- 🤖 Machine Learning
- 📈 Data Analysis
- 🔍 Search algorithms
- 🔐 Permission management

---

# ⚡ Key Points

- Sets store **unique elements**.
- Sets are **unordered**.
- Sets do not support indexing.
- Duplicate values are automatically removed.
- Set operations include **union**, **intersection**, **difference**, and **symmetric difference**.
- Frozen sets are immutable.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-08/
│   ├── sets.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create and use sets.
- Add and remove elements.
- Perform mathematical set operations.
- Use built-in set methods.
- Understand frozen sets.
- Compare sets with lists, tuples, and dictionaries.

---

# 🚀 Practice Questions

1. Create a set of five numbers.
2. Remove duplicate values from a list using a set.
3. Find the union of two sets.
4. Find the intersection of two sets.
5. Find the difference between two sets.
6. Check if one set is a subset of another.
7. Create a frozen set.
8. Count the number of elements in a set.
9. Find the maximum and minimum values in a set.
10. Sort a set using `sorted()`.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/datastructures.html#sets
- **Set Methods:** https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

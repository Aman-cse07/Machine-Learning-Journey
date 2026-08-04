# 🐍 Python Learning Journey - Day 07

# 📖 Dictionaries in Python

Welcome to **Day 07** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Dictionaries** in Python. Dictionaries are one of the most powerful built-in data structures used to store data in **key-value pairs**. They are fast, flexible, and widely used in real-world applications.

---

# 📚 Topics Covered

- ✅ What is a Dictionary?
- ✅ Characteristics of Dictionaries
- ✅ Creating Dictionaries
- ✅ Accessing Values
- ✅ Adding & Updating Items
- ✅ Removing Items
- ✅ Dictionary Methods
- ✅ Built-in Functions
- ✅ Looping Through Dictionaries
- ✅ Nested Dictionaries
- ✅ Dictionary Comprehension
- ✅ Real-World Applications

---

# 📖 What is a Dictionary?

A **Dictionary** is an unordered (insertion-ordered in Python 3.7+), mutable collection of **key-value pairs**.

Each key in a dictionary must be **unique**, while values can be duplicated.

### Example

```python
student = {
    "name": "Aman",
    "age": 23,
    "course": "CSE (AI & ML)"
}
```

---

# ⭐ Characteristics of Dictionaries

- Stores data as **key : value** pairs
- Mutable (Can be modified)
- Keys must be unique
- Values can be duplicated
- Supports nested dictionaries
- Fast searching using keys

---

# ✍️ Creating Dictionaries

## Empty Dictionary

```python
student = {}
```

---

## Dictionary with Values

```python
student = {
    "name": "Aman",
    "age": 23,
    "course": "CSE"
}
```

---

## Using dict()

```python
student = dict(
    name="Aman",
    age=23,
    course="CSE"
)
```

---

# 📥 Accessing Dictionary Values

Using Key

```python
student = {
    "name": "Aman",
    "age": 23
}

print(student["name"])
```

Output

```text
Aman
```

---

Using `get()`

```python
print(student.get("age"))
```

Output

```text
23
```

---

# ➕ Adding Items

```python
student = {
    "name": "Aman"
}

student["city"] = "Madhepura"

print(student)
```

Output

```text
{'name': 'Aman', 'city': 'Madhepura'}
```

---

# ✏️ Updating Items

```python
student["age"] = 24
```

Output

```text
{'name': 'Aman', 'city': 'Madhepura', 'age': 24}
```

---

# ❌ Removing Items

## pop()

```python
student.pop("age")
```

Removes the specified key.

---

## popitem()

```python
student.popitem()
```

Removes the last inserted key-value pair.

---

## del

```python
del student["city"]
```

Deletes a key.

---

## clear()

```python
student.clear()
```

Removes all items.

---

# 🔄 Looping Through Dictionary

## Keys

```python
for key in student:
    print(key)
```

---

## Values

```python
for value in student.values():
    print(value)
```

---

## Key and Value

```python
for key, value in student.items():
    print(key, value)
```

---

# 🛠 Dictionary Methods

## 1️⃣ `clear()`

Removes all items.

```python
student.clear()
```

---

## 2️⃣ `copy()`

Returns a copy of the dictionary.

```python
new_student = student.copy()
```

---

## 3️⃣ `fromkeys()`

Creates a new dictionary from given keys.

```python
keys = ("a", "b", "c")

d = dict.fromkeys(keys, 0)

print(d)
```

Output

```text
{'a': 0, 'b': 0, 'c': 0}
```

---

## 4️⃣ `get()`

Returns the value of a key.

```python
student.get("name")
```

---

## 5️⃣ `items()`

Returns all key-value pairs.

```python
student.items()
```

---

## 6️⃣ `keys()`

Returns all keys.

```python
student.keys()
```

---

## 7️⃣ `values()`

Returns all values.

```python
student.values()
```

---

## 8️⃣ `pop()`

Removes a specified key.

```python
student.pop("age")
```

---

## 9️⃣ `popitem()`

Removes the last inserted item.

```python
student.popitem()
```

---

## 🔟 `setdefault()`

Returns the value of a key. If the key doesn't exist, it inserts the key with the specified default value.

```python
student.setdefault("city", "Madhepura")
```

---

## 1️⃣1️⃣ `update()`

Updates the dictionary.

```python
student.update({"age":24})
```

---

# 🔧 Built-in Functions

## `len()`

Returns the number of key-value pairs.

```python
print(len(student))
```

---

## `type()`

Returns the data type.

```python
print(type(student))
```

Output

```text
<class 'dict'>
```

---

## `sorted()`

Returns sorted keys.

```python
print(sorted(student))
```

---

## `max()`

Returns the maximum key.

```python
data = {
    10:"A",
    20:"B",
    30:"C"
}

print(max(data))
```

Output

```text
30
```

---

## `min()`

Returns the minimum key.

```python
print(min(data))
```

Output

```text
10
```

---

# 🧩 Nested Dictionary

```python
students = {
    "student1":{
        "name":"Aman",
        "age":23
    },
    "student2":{
        "name":"Rahul",
        "age":22
    }
}

print(students["student1"]["name"])
```

Output

```text
Aman
```

---

# ⚡ Dictionary Comprehension

```python
square = {
    x:x*x
    for x in range(1,6)
}

print(square)
```

Output

```text
{1:1, 2:4, 3:9, 4:16, 5:25}
```

---

# 🌍 Real-World Applications

Dictionaries are used in:

- 👨‍🎓 Student Management Systems
- 🛒 E-Commerce Websites
- 🔐 Login Systems
- 🌐 APIs (JSON Data)
- 🤖 Artificial Intelligence
- 📊 Data Analysis
- 🎮 Game Development

---

# ⚖️ Difference Between List, Tuple & Dictionary

| Feature | List | Tuple | Dictionary |
|----------|------|--------|------------|
| Syntax | `[]` | `()` | `{}` |
| Mutable | ✅ Yes | ❌ No | ✅ Yes |
| Ordered | ✅ Yes | ✅ Yes | ✅ Yes (Python 3.7+) |
| Duplicate Values | ✅ Yes | ✅ Yes | Values Yes, Keys No |
| Indexing | ✅ Yes | ✅ Yes | ❌ Uses Keys |

---

# ⚡ Key Points

- Dictionary stores **key-value pairs**.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- Fast lookup using keys.
- Supports nested dictionaries and comprehensions.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-07/
│   ├── dictionary.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create dictionaries.
- Access values using keys.
- Add, update, and delete items.
- Use all important dictionary methods.
- Use built-in functions with dictionaries.
- Create nested dictionaries.
- Write dictionary comprehensions.

---

# 🚀 Practice Questions

1. Create a student dictionary with name, age, and marks.
2. Add a new key called `city`.
3. Update the student's marks.
4. Delete the `age` key.
5. Print all keys and values.
6. Count the number of items in a dictionary.
7. Create a nested dictionary.
8. Create a dictionary using comprehension.
9. Find the maximum and minimum key.
10. Copy one dictionary into another.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- **Dictionary Methods:** https://docs.python.org/3/library/stdtypes.html#dict

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

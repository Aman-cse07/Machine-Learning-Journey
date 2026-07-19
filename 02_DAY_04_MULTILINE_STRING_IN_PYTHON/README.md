# 🐍 Python Learning Journey - Day 04

# 📝 Multiline Strings in Python

Welcome to **Day 04** of my Python Learning Journey! 🚀

In this lesson, we will learn about **Multiline Strings** in Python. Multiline strings allow us to write text that spans multiple lines without using `\n` repeatedly. They are commonly used for storing paragraphs, poems, documentation, SQL queries, HTML code, and more.

---

# 📚 Topics Covered

- ✅ What are Multiline Strings?
- ✅ Triple Single Quotes (`''' '''`)
- ✅ Triple Double Quotes (`""" """`)
- ✅ Printing a Multiline String
- ✅ Practice Program
- ✅ Applications of Multiline Strings

---

# 📖 What are Multiline Strings?

A **multiline string** is a string that spans multiple lines. In Python, multiline strings are created using **triple single quotes (`'''`)** or **triple double quotes (`"""`)**.

Unlike normal strings, you don't need to use the newline character (`\n`) after every line.

---

# ✍️ Syntax

### Using Triple Single Quotes

```python
text = '''
This is
a multiline
string.
'''
```

### Using Triple Double Quotes

```python
text = """
This is
also a multiline
string.
"""
```

Both methods produce the same result.

---

# 💻 Practice Program

```python
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
''')
```

---

# 📤 Output

```text
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
```

---

# 📌 Explanation

### Triple Single Quotes (`''' '''`)

```python
print('''
Hello
Python
''')
```

- Used to create a multiline string.
- Preserves line breaks exactly as written.

---

### Triple Double Quotes (`""" """`)

```python
print("""
Hello
World
""")
```

- Works exactly like triple single quotes.
- Often used for **docstrings** (documentation strings).

---

# 💡 Why Use Multiline Strings?

Multiline strings are useful when working with:

- 📝 Poems
- 📄 Paragraphs
- 📚 Documentation (Docstrings)
- 🌐 HTML Code
- 🗄️ SQL Queries
- 📧 Email Templates
- 📜 Long Messages

---

# ⚠️ Difference Between Normal and Multiline Strings

### Normal String

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

### Multiline String

```python
print("""
Hello
World
""")
```

Output:

```text
Hello
World
```

Multiline strings are easier to read and write when dealing with long text.

---

# ⚡ Key Points

- Multiline strings use **triple quotes**.
- Both `''' '''` and `""" """` work the same way.
- They preserve formatting and line breaks.
- Triple double quotes are commonly used for **docstrings**.
- Ideal for storing long blocks of text.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-04/
│   ├── multiline_string.py
│   └── README.md
│
└── Projects/
```

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Create multiline strings in Python.
- Use both triple single quotes and triple double quotes.
- Print long blocks of text without using `\n`.
- Understand where multiline strings are used in real-world applications.

---

# 📚 Useful Resources

- **Official Python Documentation:** https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
- **Python Tutorial:** https://docs.python.org/3/tutorial/introduction.html

---

# 🚀 What's Next?

In the next lesson, we'll learn about:

- User Input with `input()`
- Type Conversion
- Input from Keyboard
- Practice Programs

Stay tuned! 🎉

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** it and follow my Python Learning Journey!

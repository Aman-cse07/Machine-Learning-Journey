# 🐍 Python Learning Journey - For Loop & Loop Control Statements

# 🔄 For Loop in Python

Welcome to another lesson in my **Python Learning Journey**! 🚀

In this lesson, we will learn about the **`for` loop** in Python and how it is used to iterate over different sequences such as **lists, tuples, strings, and ranges**.

We will also learn about:

- `for` loop with `else`
- `break`
- `continue`
- `pass`

These concepts are very important for writing programs that repeat tasks and make decisions while looping.

---

# 📚 Topics Covered

- ✅ What is a Loop?
- ✅ What is a `for` Loop?
- ✅ Syntax of `for` Loop
- ✅ `for` Loop with `range()`
- ✅ Iterating over a List
- ✅ Iterating over a Tuple
- ✅ Iterating over a String
- ✅ Iterating over a Dictionary
- ✅ `for` Loop with `else`
- ✅ `break` Statement
- ✅ `continue` Statement
- ✅ `pass` Statement
- ✅ Difference between `break`, `continue`, and `pass`
- ✅ Nested `for` Loops
- ✅ Practical Examples
- ✅ Practice Questions

---

# 🔁 What is a Loop?

A **loop** is used to execute a block of code repeatedly.

For example, if we want to print numbers from 1 to 5, instead of writing:

```python
print(1)
print(2)
print(3)
print(4)
print(5)
```

we can use a loop:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

This makes our code shorter and easier to maintain.

---

# 🔄 What is a `for` Loop?

A `for` loop is used to **iterate over a sequence or iterable**.

It can be used with:

- Lists
- Tuples
- Strings
- Dictionaries
- Sets
- Ranges
- Other iterable objects

---

# 📝 Syntax of `for` Loop

```python
for variable in iterable:
    # code to execute
```

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
```

Here:

- `fruit` → loop variable
- `fruits` → iterable
- `print(fruit)` → code executed for each item

---

# 🔢 For Loop with `range()`

The `range()` function is commonly used with `for` loops.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

> `range(5)` starts from `0` and stops before `5`.

---

## Starting and Ending Value

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

## Using a Step

```python
for i in range(1, 11, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

Here:

```text
start = 1
stop = 11
step = 2
```

---

# 📋 Iterating Over a List

A list can contain multiple values, and a `for` loop can visit each value one by one.

```python
fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Banana
Mango
Orange
```

---

## List of Numbers

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
50
```

---

## Finding the Sum of List Elements

```python
numbers = [10, 20, 30, 40]

total = 0

for number in numbers:
    total = total + number

print("Total:", total)
```

Output:

```text
Total: 100
```

---

# 📦 Iterating Over a Tuple

Tuples can also be iterated using a `for` loop.

```python
numbers = (10, 20, 30, 40)

for number in numbers:
    print(number)
```

Output:

```text
10
20
30
40
```

---

## Tuple of Strings

```python
names = ("Aman", "Rahul", "Priya")

for name in names:
    print(name)
```

Output:

```text
Aman
Rahul
Priya
```

---

# 🔤 Iterating Over a String

A string is a sequence of characters.

Therefore, we can use a `for` loop to access each character.

```python
name = "Aman"

for character in name:
    print(character)
```

Output:

```text
A
m
a
n
```

---

# 🔢 Counting Characters in a String

```python
text = "Python"

count = 0

for character in text:
    count = count + 1

print("Number of characters:", count)
```

Output:

```text
Number of characters: 6
```

---

# 🔎 Finding Vowels in a String

```python
text = "Python Programming"

for character in text:
    if character in "aeiouAEIOU":
        print(character)
```

Output:

```text
o
o
a
i
```

---

# 📖 Iterating Over a Dictionary

A dictionary can also be iterated using a `for` loop.

```python
student = {
    "name": "Aman",
    "age": 23,
    "course": "CSE"
}

for key in student:
    print(key)
```

Output:

```text
name
age
course
```

---

## Iterating Over Dictionary Values

```python
for value in student.values():
    print(value)
```

Output:

```text
Aman
23
CSE
```

---

## Iterating Over Keys and Values

The `items()` method returns both keys and values.

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Aman
age : 23
course : CSE
```

---

# 🔷 Iterating Over a Set

Sets can also be iterated using a `for` loop.

```python
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
```

> Sets are unordered, so the order of output should not be relied upon.

---

# 🔁 Nested For Loop

A loop inside another loop is called a **nested loop**.

Example:

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Output:

```text
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
```

Nested loops are commonly used with:

- Matrices
- Patterns
- Tables
- 2D data

---

# 🧮 Multiplication Table Using For Loop

```python
number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)
```

Output:

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# 🔀 For Loop with `else`

Python allows us to use an `else` block with a `for` loop.

The `else` block executes when the loop finishes **normally without encountering a `break` statement**.

### Syntax

```python
for variable in iterable:
    # loop body
else:
    # executes when loop finishes normally
```

---

## Example

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
3
4
Loop completed
```

---

# 🛑 For Loop with `else` and `break`

If the loop encounters `break`, the `else` block is **not executed**.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

The `else` block did not execute because `break` terminated the loop.

---

# 🔍 Practical Example: Searching an Element

```python
numbers = [10, 20, 30, 40, 50]

search = 30

for number in numbers:
    if number == search:
        print("Element found")
        break
else:
    print("Element not found")
```

Output:

```text
Element found
```

This is a very useful pattern for searching.

---

# 🛑 `break` Statement

The `break` statement is used to **immediately terminate a loop**.

When Python encounters `break`, it exits the loop.

### Syntax

```python
break
```

---

## Example

```python
for i in range(1, 10):
    if i == 5:
        break

    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, `break` stops the loop.

---

# 🔍 Search Using `break`

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    if number == 30:
        print("Number found")
        break
```

Output:

```text
Number found
```

---

# ➡️ `continue` Statement

The `continue` statement is used to **skip the current iteration** and move to the next iteration.

### Syntax

```python
continue
```

---

## Example

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

When `i` becomes `3`, Python skips that iteration.

---

# 🔢 Print Only Odd Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue

    print(i)
```

Output:

```text
1
3
5
7
9
```

Here, `continue` skips all even numbers.

---

# ⏭️ `continue` vs `break`

### `break`

Completely stops the loop.

```python
for i in range(1, 6):
    if i == 3:
        break

    print(i)
```

Output:

```text
1
2
```

---

### `continue`

Skips only the current iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue

    print(i)
```

Output:

```text
1
2
4
5
```

---

# ⏸️ `pass` Statement

The `pass` statement is a **null statement**.

It does nothing when executed.

It is useful when you need to write a block of code but don't want to implement it yet.

### Example

```python
for i in range(5):
    pass
```

The loop runs, but `pass` performs no action.

---

# 🧪 Example of `pass` with `if`

```python
age = 20

if age >= 18:
    pass
else:
    print("Not eligible")
```

Since the condition is true, Python executes `pass` and does nothing.

---

# 🏗️ `pass` as a Placeholder

Suppose you are creating a function but haven't written its logic yet.

```python
def calculate_result():
    pass
```

This allows Python to accept the empty function body without producing an indentation error.

Later, you can replace `pass` with the actual code.

---

# ⚖️ Difference Between `break`, `continue`, and `pass`

| Statement | Purpose | Effect on Loop |
|-----------|---------|----------------|
| `break` | Stop the loop | Completely terminates loop |
| `continue` | Skip current iteration | Moves to next iteration |
| `pass` | Do nothing | Loop continues normally |

---

# 🧠 Easy Way to Remember

```text
break    → STOP the loop 🛑
continue → SKIP this iteration ⏭️
pass     → DO NOTHING 🤷
```

---

# 🔥 Complete Example

```python
for i in range(1, 11):

    if i == 3:
        continue

    if i == 8:
        break

    if i == 5:
        pass

    print(i)
```

Output:

```text
1
2
4
5
6
7
```

Explanation:

- `3` → skipped because of `continue`
- `5` → `pass` does nothing, so `5` is printed
- `8` → loop stops because of `break`
- Numbers after `8` are never processed

---

# 📊 Comparison of Loop Control Statements

| Statement | Stops Loop? | Skips Iteration? | Does Nothing? |
|-----------|-------------|------------------|---------------|
| `break` | ✅ Yes | ❌ | ❌ |
| `continue` | ❌ No | ✅ Yes | ❌ |
| `pass` | ❌ No | ❌ | ✅ |

---

# 🌍 Real-World Applications

For loops and loop-control statements are used in:

- 📊 Data Processing
- 🤖 Machine Learning
- 🌐 Web Development
- 📁 File Processing
- 🔍 Searching Data
- 📈 Data Analysis
- 🎮 Game Development
- 🧮 Mathematical Calculations
- 🗃️ Database Operations

---

# 💻 Practical Example: Find Even Numbers

```python
numbers = [10, 15, 20, 25, 30, 35]

for number in numbers:
    if number % 2 != 0:
        continue

    print(number)
```

Output:

```text
10
20
30
```

---

# 💻 Practical Example: Find a Number

```python
numbers = [10, 20, 30, 40, 50]

search = 40

for number in numbers:
    if number == search:
        print("Number found:", number)
        break
else:
    print("Number not found")
```

Output:

```text
Number found: 40
```

---

# 💻 Practical Example: Prime Number Check

```python
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Number is not prime.")
        break
else:
    print("Number is prime.")
```

### How it works

Suppose:

```text
n = 7
```

Python checks:

```text
7 % 2
7 % 3
7 % 4
7 % 5
7 % 6
```

None of them gives `0`, so the loop finishes without `break`.

Therefore:

```text
Number is prime.
```

If:

```text
n = 8
```

Python finds:

```text
8 % 2 == 0
```

So `break` executes and the number is not prime.

---

# 📌 Important Points

- `for` loops are used to iterate over iterable objects.
- Lists, tuples, strings, dictionaries, sets, and ranges can be iterated.
- `break` completely terminates the loop.
- `continue` skips the current iteration.
- `pass` does nothing.
- `for...else` executes `else` when the loop finishes normally.
- If `break` occurs, the `else` block is skipped.
- Indentation is very important in Python.

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

- Understand how `for` loops work.
- Iterate through lists.
- Iterate through tuples.
- Iterate through strings.
- Iterate through dictionaries and sets.
- Use `range()` with loops.
- Use `for...else`.
- Understand and use `break`.
- Understand and use `continue`.
- Understand and use `pass`.
- Build practical programs using loops.

---

# 🚀 Practice Questions

### Basic

1. Print numbers from 1 to 10 using a `for` loop.
2. Print all elements of a list.
3. Print all elements of a tuple.
4. Print each character of a string.
5. Print numbers from 10 to 1.
6. Print all even numbers from 1 to 50.
7. Print all odd numbers from 1 to 50.

### Intermediate

8. Find the sum of all numbers in a list.
9. Find the largest number in a list.
10. Find the smallest number in a list.
11. Count vowels in a string.
12. Search for an element in a list using `for...else`.
13. Print a multiplication table.
14. Reverse a string using a `for` loop.

### Loop Control

15. Print numbers from 1 to 10 but skip `5` using `continue`.
16. Print numbers from 1 to 10 and stop at `7` using `break`.
17. Create a loop using `pass`.
18. Create a program that searches for a number using `for...else`.
19. Check whether a number is prime using `for...else`.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-11/
│   ├── for_loop.py
│   ├── break_continue_pass.py
│   └── README.md
│
└── Projects/
```

---

# 📚 Useful Resources

- **Python Official Documentation:** https://docs.python.org/3/tutorial/controlflow.html
- **Python `for` Statements:** https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
- **Python `break` and `continue`:** https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!

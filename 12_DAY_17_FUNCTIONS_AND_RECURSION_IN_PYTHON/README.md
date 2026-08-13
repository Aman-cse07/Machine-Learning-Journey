# 🐍 Python Learning Journey - Functions and Recursion

# 🔧 Functions and Recursion in Python

Welcome to another lesson in my **Python Learning Journey**! 🚀

In this lesson, we will learn about **Functions** and **Recursion** in Python.

Functions help us divide a large program into smaller, reusable blocks of code. Recursion is a technique where a function **calls itself** to solve a problem.

---

# 📚 Topics Covered

* ✅ What is a Function?
* ✅ Why Use Functions?
* ✅ Creating a Function
* ✅ Calling a Function
* ✅ Function Parameters
* ✅ Function Arguments
* ✅ Default Arguments
* ✅ Keyword Arguments
* ✅ Return Statement
* ✅ Multiple Parameters
* ✅ Variable-Length Arguments
* ✅ `*args`
* ✅ `**kwargs`
* ✅ Local and Global Variables
* ✅ Functions with Conditions and Loops
* ✅ Recursive Functions
* ✅ Base Case
* ✅ Recursive Case
* ✅ Factorial Using Recursion
* ✅ Sum Using Recursion
* ✅ Fibonacci Series Using Recursion
* ✅ Advantages and Disadvantages of Recursion
* ✅ Practice Questions

---

# 📖 What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of writing the same code multiple times, we can define a function once and call it whenever required.

### Example

```python
def greet():
    print("Hello Aman")

greet()
```

Output:

```text
Hello Aman
```

---

# ⭐ Why Do We Use Functions?

Functions help us to:

* Reduce code repetition
* Make code easier to understand
* Make programs more organized
* Reuse code
* Make debugging easier
* Divide large programs into smaller parts

---

# ✍️ Creating a Function

We use the `def` keyword to create a function.

### Syntax

```python
def function_name():
    # function body
```

Example:

```python
def welcome():
    print("Welcome to Python")

welcome()
```

Output:

```text
Welcome to Python
```

---

# 📞 Calling a Function

Defining a function does not execute it.

We need to **call** the function.

```python
def message():
    print("Learning Python")

message()
```

Here:

```python
message()
```

is the function call.

---

# 🔢 Function with Parameters

A parameter allows us to pass data into a function.

```python
def greet(name):
    print("Hello", name)

greet("Aman")
```

Output:

```text
Hello Aman
```

Here:

```text
name → Parameter
"Aman" → Argument
```

---

# 🧮 Function with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

---

# 🔙 Return Statement

The `return` statement sends a value back to the place where the function was called.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### `print()` vs `return`

`print()` displays a value:

```python
def add(a, b):
    print(a + b)
```

`return` sends a value back:

```python
def add(a, b):
    return a + b
```

The returned value can be stored in a variable and used later.

---

# ➕ Function to Add Two Numbers

```python
def sum(a, b):
    add = a + b
    return add

result = sum(4, 5)

print(result)
```

Output:

```text
9
```

---

# 🔢 Function to Find Square

```python
def square(number):
    return number * number

print(square(5))
```

Output:

```text
25
```

---

# 🎯 Default Arguments

A default argument has a default value.

```python
def greet(name="Aman"):
    print("Hello", name)

greet()
greet("Rahul")
```

Output:

```text
Hello Aman
Hello Rahul
```

If no argument is provided, `"Aman"` is used.

---

# 🔑 Keyword Arguments

We can pass arguments using parameter names.

```python
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=23, name="Aman")
```

Output:

```text
Name: Aman
Age: 23
```

The order does not matter when keyword arguments are used.

---

# 📦 Positional Arguments

Arguments passed according to their position are called positional arguments.

```python
def student(name, age):
    print(name)
    print(age)

student("Aman", 23)
```

Output:

```text
Aman
23
```

---

# 🔀 `*args`

`*args` allows a function to accept multiple positional arguments.

```python
def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20, 30))
```

Output:

```text
60
```

---

# 🔑 `**kwargs`

`**kwargs` allows a function to accept multiple keyword arguments.

```python
def student(**details):
    print(details)

student(name="Aman", age=23, course="CSE")
```

Output:

```text
{'name': 'Aman', 'age': 23, 'course': 'CSE'}
```

---

# 🌍 Local Variables

A variable created inside a function is called a **local variable**.

```python
def display():
    name = "Aman"
    print(name)

display()
```

`name` is available inside the function.

---

# 🌎 Global Variables

A variable created outside a function is called a **global variable**.

```python
name = "Aman"

def display():
    print(name)

display()
```

Output:

```text
Aman
```

---

# 🔄 Function with a Loop

Functions can contain loops.

```python
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()
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

# 🧠 Function with Conditional Statements

```python
def check_number(number):

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("Zero")

check_number(10)
```

Output:

```text
Positive number
```

---

# 🔁 What is Recursion?

**Recursion** is a programming technique in which a function calls itself.

A recursive function must have a **base case** to stop the recursion.

### Basic Structure

```python
def function():
    if condition:
        return
    function()
```

A recursive function generally contains two important parts:

1. **Base Case**
2. **Recursive Case**

---

# 🛑 Base Case

The **base case** is the condition that stops the recursive function.

Without a base case, the function would continue calling itself indefinitely.

Example:

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

Output:

```text
5
4
3
2
1
```

When `n` becomes `0`, the function stops.

---

# 🔄 Recursive Case

The part where the function calls itself is called the **recursive case**.

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
```

Here:

```python
countdown(n - 1)
```

is the recursive call.

---

# 🧮 Factorial Using Recursion

The factorial of a number is:

```text
5! = 5 × 4 × 3 × 2 × 1
```

Therefore:

```text
5! = 120
```

### Python Program

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

### How Recursion Works

```text
factorial(5)
5 × factorial(4)

4 × factorial(3)

3 × factorial(2)

2 × factorial(1)

factorial(1) → 1
```

Then the results return back:

```text
2 × 1 = 2
3 × 2 = 6
4 × 6 = 24
5 × 24 = 120
```

---

# ➕ Sum of Natural Numbers Using Recursion

```python
def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

print(sum_numbers(5))
```

Output:

```text
15
```

Because:

```text
5 + 4 + 3 + 2 + 1 = 15
```

---

# 🐚 Fibonacci Series Using Recursion

The Fibonacci sequence is:

```text
0 1 1 2 3 5 8 13 ...
```

Each number is the sum of the previous two numbers.

### Program

```python
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i))
```

Output:

```text
0
1
1
2
3
5
8
13
```

---

# 🔍 Recursive Function to Print Numbers

```python
def print_numbers(n):

    if n == 0:
        return

    print(n)

    print_numbers(n - 1)

print_numbers(5)
```

Output:

```text
5
4
3
2
1
```

---

# 🔄 Recursion vs Loop

| Feature    | Loop                         | Recursion                         |
| ---------- | ---------------------------- | --------------------------------- |
| Repetition | Uses loops                   | Function calls itself             |
| Memory     | Usually less                 | Uses call stack                   |
| Speed      | Usually faster               | Can be slower                     |
| Code       | Often simpler for repetition | Useful for recursive problems     |
| Base Case  | Not required                 | Required                          |
| Common Use | Iteration                    | Trees, graphs, divide-and-conquer |

---

# ⚠️ Advantages of Recursion

* Makes some problems easier to understand
* Useful for tree and graph problems
* Useful in divide-and-conquer algorithms
* Can produce clean and elegant code
* Useful for problems naturally defined recursively

---

# ⚠️ Disadvantages of Recursion

* Uses additional memory because of the call stack
* Can be slower than loops
* Too many recursive calls can cause an error
* Sometimes an iterative solution is simpler

---

# 🚨 Recursion Error

If a recursive function does not have a proper base case, it may continue indefinitely.

Example:

```python
def test():
    print("Hello")
    test()

test()
```

This eventually causes:

```text
RecursionError
```

Therefore, always make sure your recursive function has a proper **base case**.

---

# 🧩 Function vs Recursion

A function does not necessarily call itself.

```python
def greet():
    print("Hello")

greet()
```

A recursive function calls itself.

```python
def countdown(n):

    if n == 0:
        return

    print(n)
    countdown(n - 1)
```

So:

```text
Every recursive function is a function,
but every function is NOT recursive.
```

---

# 💻 Practical Example: Check Even or Odd

```python
def check_number(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_number(10))
```

Output:

```text
Even
```

---

# 💻 Practical Example: Find Maximum

```python
def find_max(a, b, c):

    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(find_max(10, 30, 20))
```

Output:

```text
30
```

---

# 📌 Important Points

* Functions are reusable blocks of code.
* Use `def` to define a function.
* Parameters receive values passed to a function.
* Arguments are the actual values passed to a function.
* `return` sends a value back from a function.
* `*args` accepts multiple positional arguments.
* `**kwargs` accepts multiple keyword arguments.
* Recursion occurs when a function calls itself.
* Every recursive function should have a base case.
* Recursion is especially useful for trees, graphs, and divide-and-conquer problems.

---

# 🎯 Learning Outcome

After completing this lesson, you will be able to:

* Create and call functions.
* Use parameters and arguments.
* Return values from functions.
* Use default and keyword arguments.
* Understand `*args` and `**kwargs`.
* Understand local and global variables.
* Create recursive functions.
* Identify base and recursive cases.
* Solve basic problems using recursion.

---

# 🚀 Practice Questions

## Functions

1. Create a function to add two numbers.
2. Create a function to find the square of a number.
3. Create a function to check whether a number is even or odd.
4. Create a function to find the largest of three numbers.
5. Create a function to calculate the area of a circle.
6. Create a function to calculate simple interest.
7. Create a function to count vowels in a string.
8. Create a function to find the sum of all elements in a list.

## Recursion

9. Find the factorial of a number using recursion.
10. Find the sum of natural numbers using recursion.
11. Print numbers from `n` to `1` using recursion.
12. Print numbers from `1` to `n` using recursion.
13. Find the nth Fibonacci number using recursion.
14. Find the sum of digits of a number using recursion.
15. Reverse a string using recursion.
16. Check whether a number is a palindrome using recursion.

---

# 📂 Folder Structure

```text
Python-Learning-Journey/
│
├── Day-12/
│   ├── functions.py
│   ├── recursion.py
│   └── README.md
│
└── Projects/
```

---

# 📚 Useful Resources

* **Python Official Documentation:** https://docs.python.org/3/tutorial/controlflow.html#defining-functions
* **Python Functions:** https://docs.python.org/3/reference/compound_stmts.html#function-definitions

---

# 👨‍💻 Author

## **Aman Kumar**

**B.Tech CSE (AI & ML)**

**Python Learning Journey 🐍🚀**

---

⭐ If you found this repository helpful, don't forget to **Star** this repository and follow my Python Learning Journey!


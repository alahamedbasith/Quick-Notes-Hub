# Python Core Concepts Summary

This document provides a summary of fundamental Python programming concepts, from basic syntax to more advanced topics like exception handling and object-oriented programming. Each section provides a clear explanation, syntax, and practical code examples.

## Table of Contents

1.  [Python Basics: Syntax and Semantics](#python-basics-syntax-and-semantics)
2.  [Variables in Python](#variables-in-python)
3.  [Basic Data Types](#basic-data-types)
4.  [Operators in Python](#operators-in-python)
5.  [Conditional Statements](#conditional-statements-in-python)
6.  [Loops in Python](#loops-in-python)
7.  [Practical Examples of Lists](#practical-examples-of-list)
8.  [Sets in Python](#sets-in-python)
9.  [Tuples in Python](#tuples-in-python)
10. [Dictionaries in Python](#dictionaries-in-python)
11. [Functions in Python](#functions-in-python)
12. [Lambda Functions](#lambda-functions-in-python)
13. [Map Function](#map-function-in-python)
14. [Filter Function](#python-filter-function)
15. [Modules and Packages](#import-modules-and-packages-in-python)
16. [The Standard Library](#standard-library-overview)
17. [File Operations](#file-operation-in-python)
18. [Working with File Paths](#working-with-file-paths)
19. [Exception Handling](#exception-handling-in-python)

---

## PYTHON BASICS-SYNTAX AND SEMANTICS
----------------------------------------------------------------------------
Python basics cover the fundamental rules and structure of the Python programming language. Understanding syntax (the rules for writing code) and semantics (the meaning of that code) is the first step to writing effective Python programs.

#### SYNTAX: THE GRAMMAR OF PYTHON
- **Indentation**: Python uses 4 spaces for indentation to define code blocks.
- **Comments**: `#` for single-line, `"""` or `'''` for multi-line.
- **Case-Sensitivity**: `myVar` and `myvar` are different.

```python
# This is a comment
if True:
    print("This is an indented block.")  # 4 spaces
```

#### SEMANTICS: THE MEANING OF CODE
- **Expressions**: Combinations of values, variables, and operators that evaluate to a value (e.g., `5 + 3`).
- **Keywords**: Reserved words with special meanings (`if`, `def`, `for`, etc.).

---

## VARIABLES IN PYTHON
----------------------------------------------------------------------------
A variable is a name that points to a value. Python is dynamically-typed, so you don't need to declare the type.

- **Assignment**: `age = 25`
- **Naming Convention**: `snake_case` (e.g., `my_variable_name`).
- **Multiple Assignment**: `x, y = 10, 20`

```python
name = "Alice"
age = 30
is_student = True

# Re-assignment is possible
age = 31 
```

---

## BASIC DATA TYPES
----------------------------------------------------------------------------
- **Numeric**: `int` (100), `float` (3.14), `complex` (2+3j)
- **Text**: `str` ("Hello")
- **Sequence**: `list` ([1, 2, 3]), `tuple` ((1, 2, 3))
- **Mapping**: `dict` ({"key": "value"})
- **Set**: `set` ({1, 2, 3}), `frozenset` (immutable)
- **Boolean**: `bool` (True, False)
- **None**: `NoneType` (None)

---

## OPERATORS IN PYTHON
----------------------------------------------------------------------------
- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`
- **Identity**: `is`, `is not`
- **Membership**: `in`, `not in`

---

## CONDITIONAL STATEMENTS IN PYTHON
----------------------------------------------------------------------------
Execute code based on conditions.

- **`if`**: Executes if the condition is true.
- **`if-else`**: Executes one block if true, another if false.
- **`if-elif-else`**: Chains multiple conditions.

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}") # Grade: B
```

---

## LOOPS IN PYTHON
----------------------------------------------------------------------------
Repeat a block of code.

- **`for` loop**: Iterates over a sequence (list, string, range).
- **`while` loop**: Repeats as long as a condition is true.
- **Control Statements**: `break` (exits loop), `continue` (skips iteration), `pass` (placeholder).

```python
# For loop
for i in range(3):
    print(i)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## PRACTICAL EXAMPLES OF LIST
----------------------------------------------------------------------------
A list is an ordered, mutable (changeable) collection.

- **Creation**: `my_list = [1, "a", 3.5]`
- **Methods**: `append()`, `insert()`, `remove()`, `pop()`, `sort()`
- **List Comprehension**: A concise way to create lists.

```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared) # [1, 4, 9, 16, 25]
```

---

## SETS IN PYTHON
----------------------------------------------------------------------------
An unordered, mutable collection of **unique** elements.

- **Creation**: `my_set = {1, 2, 3}`
- **Use Case**: Removing duplicates from a list.
- **Operations**: Union (`|`), intersection (`&`), difference (`-`).

```python
unique_items = set([1, 2, 2, 3, 1, 4])
print(unique_items) # {1, 2, 3, 4}
```

---

## TUPLES IN PYTHON
----------------------------------------------------------------------------
An ordered, **immutable** (unchangeable) collection.

- **Creation**: `my_tuple = (1, 2, 3)`
- **Use Case**: Storing data that should not be modified (e.g., coordinates, dictionary keys).
- **Unpacking**: `x, y, z = my_tuple`

---

## DICTIONARIES IN PYTHON
----------------------------------------------------------------------------
An unordered, mutable collection of **key-value** pairs.

- **Creation**: `my_dict = {"name": "Alice", "age": 30}`
- **Accessing**: `my_dict["name"]`
- **Methods**: `keys()`, `values()`, `items()`

```python
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

## FUNCTIONS IN PYTHON
----------------------------------------------------------------------------
A reusable block of code.

- **Definition**: `def my_function(parameter):`
- **Return Value**: `return value`
- **Arguments**: `*args` (tuple of positional args), `**kwargs` (dict of keyword args).

```python
def greet(name="World"):
    return f"Hello, {name}!"

print(greet("Alice")) # Hello, Alice!
```

---

## LAMBDA FUNCTIONS IN PYTHON
----------------------------------------------------------------------------
A small, anonymous function defined with `lambda`.

- **Syntax**: `lambda arguments: expression`
- **Use Case**: As an argument for higher-order functions like `sorted()`, `map()`, and `filter()`.

```python
# Sort a list of tuples by the second element
points = [(1, 5), (3, 2), (5, 8)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points) # [(3, 2), (1, 5), (5, 8)]
```

---

## MAP FUNCTION IN PYTHON
----------------------------------------------------------------------------
Applies a function to every item of an iterable.

- **Syntax**: `map(function, iterable)`
- **Returns**: A map object (iterator).

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared) # [1, 4, 9, 16]
```

---

## PYTHON FILTER FUNCTION
----------------------------------------------------------------------------
Constructs an iterator from elements of an iterable for which a function returns `True`.

- **Syntax**: `filter(function, iterable)`
- **Returns**: A filter object (iterator).

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6]
```

---

## IMPORT MODULES AND PACKAGES IN PYTHON
----------------------------------------------------------------------------
- **Module**: A single `.py` file.
- **Package**: A directory of modules with an `__init__.py` file.
- **Importing**: `import math`, `from math import sqrt`, `import numpy as np`.

---

## STANDARD LIBRARY OVERVIEW
----------------------------------------------------------------------------
A collection of modules included with Python.
- **`math`**: For mathematical functions.
- **`random`**: For generating random numbers.
- **`os`**: For interacting with the operating system.
- **`datetime`**: For working with dates and times.
- **`json`**: For working with JSON data.
- **`re`**: For regular expressions.

---

## FILE OPERATION IN PYTHON
----------------------------------------------------------------------------
Reading from and writing to files.

- **`open()`**: Opens a file. The `with` statement is recommended as it handles closing the file automatically.
- **Modes**: `'r'` (read), `'w'` (write), `'a'` (append).

```python
# Write to a file
with open("greetings.txt", "w") as f:
    f.write("Hello, file!")

# Read from a file
with open("greetings.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## WORKING WITH FILE PATHS
----------------------------------------------------------------------------
- **`os.path`**: Traditional module for path manipulation (`os.path.join()`).
- **`pathlib`**: Modern, object-oriented approach (recommended for Python 3.4+).

```python
from pathlib import Path

# The / operator is used to join paths
path = Path("my_directory") / "my_file.txt"
print(path)
```

---

## EXCEPTION HANDLING IN PYTHON
----------------------------------------------------------------------------
A mechanism to handle runtime errors gracefully.

- **`try`**: Code that might cause an error.
- **`except`**: Code to run if an error occurs.
- **`else`**: Code to run if no error occurs.
- **`finally`**: Code that always runs, with or without an error.
- **`raise`**: To trigger an exception manually.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution finished.")
```

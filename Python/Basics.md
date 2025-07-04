# Python Core Concepts: A Comprehensive Guide

This document provides a detailed summary of fundamental Python programming concepts, from basic syntax to more advanced topics like exception handling and object-oriented programming. Each section provides clear explanations, syntax, and a rich set of practical code examples to aid understanding.

## Table of Contents

1.  [Python Basics: Syntax and Semantics](#python-basics-syntax-and-semantics)
2.  [Variables in Python](#variables-in-python)
3.  [Basic Data Types](#basic-data-types)
4.  [Operators in Python](#operators-in-python)
5.  [Conditional Statements](#conditional-statements-in-python)
6.  [Loops in Python](#loops-in-python)
7.  [In-Depth: Lists](#in-depth-lists)
8.  [In-Depth: Tuples](#in-depth-tuples)
9.  [In-Depth: Sets](#in-depth-sets)
10. [In-Depth: Dictionaries](#in-depth-dictionaries)
11. [The `collections` Module](#the-collections-module)
12. [Functions in Python](#functions-in-python)
13. [Lambda Functions](#lambda-functions-in-python)
14. [Map Function](#map-function-in-python)
15. [Filter Function](#python-filter-function)
16. [Modules and Packages](#import-modules-and-packages-in-python)
17. [The Standard Library](#standard-library-overview)
18. [File Operations](#file-operation-in-python)
19. [Working with File Paths](#working-with-file-paths)
20. [Exception Handling](#exception-handling-in-python)

---

## PYTHON BASICS-SYNTAX AND SEMANTICS
----------------------------------------------------------------------------
Python basics cover the fundamental rules and structure of the Python programming language. Understanding syntax (the rules for writing code) and semantics (the meaning of that code) is the first step to writing effective Python programs.

#### SYNTAX: THE GRAMMAR OF PYTHON
- **Indentation**: Python uses 4 spaces for indentation to define code blocks.
- **Comments**: `#` for single-line, `"""` or `'''` for multi-line docstrings.
- **Statements**: Instructions that the Python interpreter can execute. Can be on a single line or span multiple lines using `\`.
- **Case-Sensitivity**: `myVar` and `myvar` are different variables.

```python
# A single-line comment
name = "Ada Lovelace"  # This is an inline comment

# A multi-line statement using backslash
total = 1 + 2 + 3 + \
        4 + 5 + 6
        
# A function definition using indentation
def my_function():
    """
    This is a multi-line comment (docstring)
    explaining the function.
    """
    if True:
        print("This is an indented block.")  # 4 spaces
    print("Back to the outer block.")

my_function()
```

#### SEMANTICS: THE MEANING OF CODE
- **Expressions**: Combinations of values, variables, and operators that evaluate to a single value (e.g., `5 * 3`).
- **Keywords**: Reserved words with special meanings (`if`, `def`, `for`, `while`, `import`, etc.). You cannot use them as variable names.

```python
import keyword
print("All Python keywords:", keyword.kwlist)
```

---

## VARIABLES IN PYTHON
----------------------------------------------------------------------------
A variable is a name that points to a value. Python is dynamically-typed, so you don't need to declare the type of a variable.

- **Assignment**: `age = 25`
- **Naming Convention**: `snake_case` (e.g., `my_variable_name`).
- **Multiple Assignment**: `x, y = 10, 20`
- **Constants**: Conventionally named in all caps (e.g., `PI = 3.14159`).

```python
# Variable assignment
name = "Alice"
age = 30
is_student = True

# Re-assignment is possible, and type can change
age = "thirty" 
print(f"Age is now a {type(age)}")

# Multiple assignment
x, y, z = 10, "hello", False

# Assigning one value to multiple variables
a = b = c = "same value"

# Legal vs. Illegal variable names
_my_var = "legal"
myVar2 = "legal"
# 2myvar = "illegal" # starts with number
# my-var = "illegal" # contains hyphen
# for = "illegal"    # is a keyword
```

---

## BASIC DATA TYPES
----------------------------------------------------------------------------
- **Numeric**: `int` (100), `float` (3.14), `complex` (2+3j)
- **Text**: `str` ("Hello")
- **Sequence**: `list` ([1, 2, 3]), `tuple` ((1, 2, 3))
- **Mapping**: `dict` ({"key": "value"})
- **Set**: `set` ({1, 2, 3}), `frozenset` (immutable version of set)
- **Boolean**: `bool` (True, False)
- **None**: `NoneType` (represents the absence of a value)

```python
# Examples of data types
an_integer = -50
a_float = 99.95
a_string = "Python is fun!"
a_list = ["apple", "banana", "cherry"]
a_tuple = (1, "config", True)
a_dictionary = {"os": "Linux", "version": "Ubuntu 22.04"}
a_set = {1, 2, 3, 3, 2} # results in {1, 2, 3}
a_boolean = (5 > 3) # True
no_value = None
```

---

## OPERATORS IN PYTHON
----------------------------------------------------------------------------
- **Arithmetic**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent)
- **Comparison**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical**: `and`, `or`, `not`
- **Assignment**: `=`, `+=`, `-=`, `*=`
- **Identity**: `is` (are they the same object?), `is not`
- **Membership**: `in` (is it in the sequence?), `not in`
- **Bitwise**: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

```python
# Arithmetic
print(f"10 // 3 = {10 // 3}") # 3

# Logical
print(f"True and False = {True and False}") # False

# Identity
list1 = [1, 2]
list2 = [1, 2]
list3 = list1
print(f"list1 is list2: {list1 is list2}") # False (different objects)
print(f"list1 == list2: {list1 == list2}") # True (same content)
print(f"list1 is list3: {list1 is list3}") # True (same object)

# Bitwise
print(f"5 & 3 = {5 & 3}") # Binary 101 & 011 = 001 (which is 1)
```

---

## CONDITIONAL STATEMENTS IN PYTHON
----------------------------------------------------------------------------
Execute code based on whether a condition is true or false.

- **`if`**: Executes if the condition is true.
- **`if-else`**: Executes one block if true, another if false.
- **`if-elif-else`**: Chains multiple conditions to test them in order.
- **Ternary Operator**: A one-line `if-else` expression.

```python
# if-elif-else example
day = "Sunday"
if day == "Saturday":
    print("It's the weekend!")
elif day == "Sunday":
    print("It's the weekend, but get ready for Monday!")
else:
    print("It's a weekday.")

# Ternary operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Checking for "truthiness"
my_list = []
if my_list: # This is False because the list is empty
    print("List is not empty.")
else:
    print("List is empty.")
```

---

## LOOPS IN PYTHON
----------------------------------------------------------------------------
Repeat a block of code until a condition is met.

- **`for` loop**: Iterates over a sequence (list, string, range).
- **`while` loop**: Repeats as long as a condition is true.
- **Control Statements**: `break` (exits loop), `continue` (skips to the next iteration), `pass` (a null statement, a placeholder).
- **`else` in loops**: The `else` block executes after the loop finishes, but *only if* the loop was not terminated by a `break` statement.

```python
# For loop with range
for i in range(5):
    print(i, end=" ") # 0 1 2 3 4
print()

# For loop with else
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
else:
    print("Loop finished without a break.")

# While loop with break and continue
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue # Skip even numbers
    if count == 7:
        break # Exit the loop
    print(f"Processing odd number: {count}")

# Nested loops to create a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
```

---

## IN-DEPTH: LISTS
----------------------------------------------------------------------------
A list is an ordered, mutable (changeable) collection of items. Lists can contain items of different data types.

- **Creation**: `my_list = [1, "a", 3.5]`
- **List Comprehension**: A concise and elegant way to create lists: `[x*x for x in range(5)]`

#### COMMON LIST METHODS
- `append(item)`: Adds one item to the end of the list.
- `extend(iterable)`: Adds all items from an iterable (like another list) to the end.
- `insert(index, item)`: Adds an item at a specific position.
- `remove(item)`: Removes the first occurrence of a value. Raises a `ValueError` if the item is not found.
- `pop([index])`: Removes and returns the item at the given index. If no index is specified, it removes and returns the last item.
- `clear()`: Removes all items from the list.
- `index(item)`: Returns the index of the first occurrence of a value. Raises a `ValueError` if not found.
- `count(item)`: Returns the number of times a value appears in the list.
- `sort()`: Sorts the list in place (ascending by default).
- `reverse()`: Reverses the order of elements in the list in place.
- `copy()`: Returns a shallow copy of the list.

```python
# List methods in action
playlist = ["Song A", "Song B", "Song C"]

# append
playlist.append("Song D") # ["Song A", "Song B", "Song C", "Song D"]

# extend
playlist.extend(["Song E", "Song F"]) # [..., "Song D", "Song E", "Song F"]

# insert
playlist.insert(1, "New Song B") # ["Song A", "New Song B", "Song B", ...]

# pop
last_song = playlist.pop() # last_song = "Song F"

# index & count
print(f"Index of 'Song C': {playlist.index('Song C')}")
playlist.append("Song A")
print(f"'Song A' appears {playlist.count('Song A')} times")

# sort
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort(reverse=True) # Sorts in place, descending
print(f"Sorted numbers: {numbers}")

# copy
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print(f"Original: {original_list}") # [1, 2, 3]
print(f"Copied: {copied_list}")   # [1, 2, 3, 4]
```

---

## IN-DEPTH: TUPLES
----------------------------------------------------------------------------
An ordered, **immutable** (unchangeable) collection. Because they are immutable, they can be used as keys in a dictionary.

- **Creation**: `my_tuple = (1, 2, 3)`. A single-element tuple needs a trailing comma: `(1,)`.
- **Use Case**: Storing data that should not be modified (e.g., coordinates, function return values, dictionary keys).
- **Unpacking**: `x, y, z = my_tuple`.

#### TUPLE METHODS
- `count(value)`: Returns the number of times a value appears.
- `index(value)`: Returns the index of the first occurrence of a value. Raises `ValueError` if not found.

```python
# Function returning multiple values (as a tuple)
def get_user_info(user_id):
    # In a real app, you'd look this up in a database
    if user_id == 1:
        return "Alice", 30, "alice@example.com"
    return None, None, None

# Unpacking the result
name, age, email = get_user_info(1)
print(f"User: {name}, Age: {age}")

# Using a tuple as a dictionary key
city_coordinates = {
    ("New York", "USA"): (40.7128, -74.0060),
    ("Tokyo", "Japan"): (35.6895, 139.6917),
}
print(f"Coordinates for Tokyo: {city_coordinates[('Tokyo', 'Japan')]}")

# Tuple methods
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(f"Count of 'p': {my_tuple.count('p')}") # 2
print(f"Index of 'l': {my_tuple.index('l')}") # 3
```

---

## IN-DEPTH: SETS
----------------------------------------------------------------------------
An unordered, mutable collection of **unique** elements. Excellent for membership testing and removing duplicates.

- **Creation**: `my_set = {1, 2, 3}` or `set([1, 2, 3])`. An empty set must be created with `set()`.

#### COMMON SET METHODS
- `add(elem)`: Adds a single element.
- `update(iterable)`: Adds all elements from an iterable.
- `remove(elem)`: Removes an element. Raises a `KeyError` if the element is not found.
- `discard(elem)`: Removes an element, but does nothing if the element is not found.
- `pop()`: Removes and returns an arbitrary element from the set.
- `clear()`: Removes all elements.

#### SET OPERATIONS
- `union(|)`: Returns a new set with all unique elements from both sets.
- `intersection(&)`: Returns a new set with elements that are in both sets.
- `difference(-)`: Returns a new set with elements in the first set but not in the second.
- `symmetric_difference(^)`: Returns a new set with elements in either set, but not both.
- `issubset(<=)` and `issuperset(>=)`: Check for subset/superset relationships.

```python
# Methods
permissions = {"read", "write"}
permissions.add("execute")
permissions.update(["comment", "share"])
permissions.discard("share") # Safely remove
print(f"Permissions: {permissions}")

# Operations
admins = {"alice", "bob", "charlie"}
developers = {"bob", "david", "eve"}

# Who has any role? (Union)
all_staff = admins.union(developers) # or admins | developers
print(f"All staff: {all_staff}")

# Who is both an admin and a developer? (Intersection)
admin_devs = admins.intersection(developers) # or admins & developers
print(f"Admin-Developers: {admin_devs}")

# Is {"alice", "bob"} a subset of admins?
print(f"Is subset? {{'alice', 'bob'}}.issubset(admins)") # True
```

---

## IN-DEPTH: DICTIONARIES
----------------------------------------------------------------------------
An unordered (in Python < 3.7) or insertion-ordered (Python 3.7+), mutable collection of **key-value** pairs.

- **Creation**: `my_dict = {"name": "Alice", "age": 30}`
- **Dictionary Comprehension**: `{k: v for k, v in some_iterable}`

#### COMMON DICTIONARY METHODS
- `get(key[, default])`: Safely gets a value by key. Returns `None` or a specified default if the key is not found.
- `keys()`: Returns a view object displaying a list of all the keys.
- `values()`: Returns a view object displaying a list of all the values.
- `items()`: Returns a view object displaying a list of key-value tuple pairs.
- `update(other_dict)`: Updates the dictionary with key-value pairs from another, overwriting existing keys.
- `pop(key[, default])`: Removes the specified key and returns the corresponding value. If the key is not found, the default is returned (or a `KeyError` is raised if no default is given).
- `popitem()`: Removes and returns the last inserted key-value pair (as a tuple). Raises `KeyError` if the dictionary is empty.
- `clear()`: Removes all items from the dictionary.

```python
# Methods in action
user_profile = {"username": "carol", "email": "carol@dev.com"}

# update
user_profile.update({"location": "Cloud City", "email": "carol.dev@cloud.com"})
print(f"Updated profile: {user_profile}")

# pop
removed_email = user_profile.pop("email")
print(f"Removed email: {removed_email}")

# popitem
last_item = user_profile.popitem() # ("location", "Cloud City")
print(f"Popped item: {last_item}")

# Looping with items()
print("Final Profile:")
for key, value in user_profile.items():
    print(f"- {key.capitalize()}: {value}")
```

---

## THE `collections` MODULE
----------------------------------------------------------------------------
The `collections` module provides specialized, high-performance container datatypes that are alternatives to the general-purpose `dict`, `list`, `set`, and `tuple`.

#### `collections.Counter`
A `dict` subclass for counting hashable objects. It's a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.

```python
from collections import Counter

# Count items in a list
word_list = ["apple", "red", "apple", "blue", "red", "apple"]
word_counts = Counter(word_list)
print(f"Word counts: {word_counts}") # Counter({'apple': 3, 'red': 2, 'blue': 1})

# Find the most common items
print(f"Two most common words: {word_counts.most_common(2)}") # [('apple', 3), ('red', 2)]
```

#### `collections.defaultdict`
A `dict` subclass that calls a factory function to supply missing values. It provides a default value for a key that does not exist, preventing `KeyError`.

```python
from collections import defaultdict

# Grouping items into a list
data = [('fruit', 'apple'), ('vegetable', 'carrot'), ('fruit', 'banana')]
grouped_data = defaultdict(list)
for category, item in data:
    grouped_data[category].append(item)

print(f"Grouped data: {dict(grouped_data)}")
# {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}

# Counting with defaultdict
counter = defaultdict(int) # default value for a new key is int() which is 0
for word in word_list:
    counter[word] += 1
print(f"Counted with defaultdict: {dict(counter)}")
```

#### `collections.namedtuple`
A factory function for creating tuple subclasses with named fields. It allows you to access items by name instead of just by index, making your code more readable.

```python
from collections import namedtuple

# Define a named tuple 'Point'
Point = namedtuple('Point', ['x', 'y', 'z'])

# Create an instance
p1 = Point(10, 20, 30)

# Access fields by name
print(f"X coordinate: {p1.x}") # 10

# Access fields by index
print(f"Y coordinate: {p1[1]}") # 20

print(p1)
```

---

## FUNCTIONS IN PYTHON
----------------------------------------------------------------------------
A reusable block of code that performs a specific task.

- **Definition**: `def my_function(parameter):`
- **Return Value**: `return value`. A function returns `None` if it has no `return` statement.
- **Arguments**: 
    - **Positional**: `greet("Alice", 30)`
    - **Keyword**: `greet(name="Alice", age=30)`
    - **Default**: `def greet(name="World"):`
    - **Arbitrary**: `*args` (tuple of positional args), `**kwargs` (dict of keyword args).

```python
# Function with default, positional, and keyword arguments
def create_user(username, email, role="viewer", is_active=True):
    """Creates a user profile dictionary."""
    return {"username": username, "email": email, "role": role, "is_active": is_active}

user1 = create_user("testuser", "test@test.com")
user2 = create_user("adminuser", "admin@test.com", role="admin")
print(user1)
print(user2)

# Function with *args and **kwargs
def report_generator(report_name, *data_points, **report_settings):
    print(f"--- Report: {report_name} ---")
    print("Data Points:", data_points)
    print("Settings:")
    for key, value in report_settings.items():
        print(f"- {key}: {value}")

report_generator("Sales Report", 100, 150, 200, author="Alice", year=2025)
```

---

## LAMBDA FUNCTIONS IN PYTHON
----------------------------------------------------------------------------
A small, anonymous function defined with the `lambda` keyword. It can have any number of arguments but only one expression.

- **Syntax**: `lambda arguments: expression`
- **Use Case**: Ideal for short, one-time use, especially as an argument for higher-order functions like `sorted()`, `map()`, and `filter()`.

```python
# Simple lambda for addition
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Using lambda to sort a list of dictionaries by a specific key
users = [
    {"name": "Charlie", "age": 35},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}
]
sorted_users = sorted(users, key=lambda user: user["age"])
print(f"Users sorted by age: {sorted_users}")
```

---

## MAP FUNCTION IN PYTHON
----------------------------------------------------------------------------
Applies a given function to each item of an iterable (like a list) and returns a map object (an iterator).

- **Syntax**: `map(function, iterable, ...)`
- **Returns**: A map object (iterator), which is usually converted to a list or tuple.

```python
# Convert a list of strings to uppercase
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(f"Uppercase words: {upper_words}")

# Add corresponding elements from two lists
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sums = list(map(lambda x, y: x + y, nums1, nums2))
print(f"Sums of lists: {sums}")
```

---

## PYTHON FILTER FUNCTION
----------------------------------------------------------------------------
Constructs an iterator from elements of an iterable for which a function returns `True`.

- **Syntax**: `filter(function, iterable)`
- **Returns**: A filter object (iterator).

```python
# Filter a list of numbers to get only the positive ones
numbers = [10, -5, 0, 25, -1, 8]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(f"Positive numbers: {positive_numbers}")

# Filter a list of dictionaries
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 75},
    {"name": "Monitor", "price": 300}
]
expensive_products = list(filter(lambda p: p["price"] > 100, products))
print(f"Expensive products: {expensive_products}")
```

---

## IMPORT MODULES AND PACKAGES IN PYTHON
----------------------------------------------------------------------------
- **Module**: A single `.py` file containing Python code.
- **Package**: A directory of Python modules containing an `__init__.py` file (which can be empty). It helps organize related modules.
- **Importing**: 
    - `import math`: Imports the whole module. Access with `math.sqrt()`.
    - `from math import sqrt`: Imports a specific member. Access directly with `sqrt()`.
    - `import numpy as np`: Imports a module with an alias. Access with `np.array()`.

```python
# Example: Using the 'random' module
import random
# from random import choice, randint # Alternative import

print(f"Random integer from 1-10: {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['rock', 'paper', 'scissors'])}")
```

---

## STANDARD LIBRARY OVERVIEW
----------------------------------------------------------------------------
A vast collection of modules included with every Python installation.

- **`math`**: For mathematical functions (`sqrt`, `sin`, `pi`).
- **`random`**: For generating random numbers.
- **`os`**: For interacting with the operating system (`os.getcwd()`, `os.path.join()`).
- **`sys`**: For system-specific parameters (`sys.argv`, `sys.path`).
- **`datetime`**: For working with dates and times.
- **`json`**: For encoding and decoding JSON data.
- **`re`**: For regular expressions (pattern matching in strings).
- **`collections`**: High-performance container datatypes (`Counter`, `defaultdict`).

```python
# Example with datetime
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
print(f"Today is: {now.strftime('%Y-%m-%d')}")
print(f"Tomorrow will be: {tomorrow.strftime('%Y-%m-%d')}")

# Example with collections.Counter
from collections import Counter
word_counts = Counter("this is a simple sentence with simple words".split())
print(f"Word counts: {word_counts}")
```

---

## FILE OPERATION IN PYTHON
----------------------------------------------------------------------------
Reading from and writing to files is a fundamental task.

- **`open()`**: Opens a file and returns a file object. The `with` statement is the recommended way to work with files as it handles closing the file automatically.
- **Modes**: `'r'` (read), `'w'` (write - overwrites), `'a'` (append), `'b'` (binary), `'t'` (text).

```python
# Write a list of lines to a file
lines_to_write = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("my_document.txt", "w") as f:
    f.writelines(lines_to_write)

# Read a file line by line (memory efficient)
print("--- Reading my_document.txt ---")
with open("my_document.txt", "r") as f:
    for line in f:
        print(line.strip()) # .strip() removes leading/trailing whitespace

# Appending to a file
with open("my_document.txt", "a") as f:
    f.write("This line was appended.\n")
```

---

## WORKING WITH FILE PATHS
----------------------------------------------------------------------------
Managing file paths correctly is key to writing portable code.

- **`os.path`**: The traditional module for path manipulation (`os.path.join()`, `os.path.exists()`).
- **`pathlib`**: The modern, object-oriented approach (recommended for Python 3.4+). It makes path operations more intuitive.

```python
from pathlib import Path
import os

# --- Using pathlib (modern) ---
# The / operator is overloaded for joining paths
data_folder = Path("./data")
output_file = data_folder / "reports" / "2025_report.csv"

# Create parent directories if they don't exist
output_file.parent.mkdir(parents=True, exist_ok=True)

# Write content to the file
output_file.write_text("Header1,Header2\nValue1,Value2")

print(f"File created at: {output_file}")
print(f"File exists: {output_file.exists()}")
print(f"File name: {output_file.name}")
print(f"Parent directory: {output_file.parent}")

# --- Using os.path (traditional) ---
old_path = os.path.join("data", "reports", "2024_report.csv")
print(f"Old path style: {old_path}")
```

---

## EXCEPTION HANDLING IN PYTHON
----------------------------------------------------------------------------
A mechanism to handle runtime errors gracefully without crashing the program.

- **`try`**: Contains the code that might cause an error.
- **`except`**: The block of code to run if an error of a specific type occurs.
- **`else`**: The block of code to run if no error occurs in the `try` block.
- **`finally`**: A block of code that *always* runs, whether an error occurred or not. Used for cleanup.
- **`raise`**: To trigger an exception manually.

```python
# A function that might fail
def get_inverse(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number.")
    if n == 0:
        raise ZeroDivisionError("Cannot calculate the inverse of zero.")
    return 1/n

# Handling different potential errors
inputs = [5, "hello", 0, 10]
for item in inputs:
    try:
        print(f"--- Processing input: {item} ---")
        result = get_inverse(item)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    else:
        # This runs only if the try block was successful
        print(f"The inverse of {item} is {result}")
    finally:
        # This runs no matter what
        print("Cleanup: Finished processing this item.")
```

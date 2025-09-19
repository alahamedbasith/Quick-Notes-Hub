# In Python, a namespace is a container that maps names 
# (identifiers) to objects (variables, functions, classes, etc.).
# A namespace in Python is a system to ensure that names are unique to avoid naming conflicts.

# a = 10, def add() ...
# LEGB (Local, Enclosed, Global, Built-in) is the scope resolution order in Python.

# Build Namespace
# Global Namespace
# Local Namespace
# Enclosed Namespace

# a = 10 # Global Namespace

# def info():
#     def inner():
#         print(a)
#     inner()

# info()

# Local Namespace

# def info():
#     a = 10
#     print(a)

# # print(a)
# info()

# Enclosed Namespace

# def info():
#     a = 10
#     def inner():
#         a = 34
#         print(a)
#     print(a)  # This will print the 'a' from the enclosing scope    
#     inner()

# Built-in Namespace

# print("Hello, World!")
# a = "hi"
# print(len(a))

# Use if
# c = 10

# if c == 10:
#  print("C is 10")
#  b = 20

# print(b)

# nonlocal and global keywords



# def info():
#     a = 20
#     def inner():
#         nonlocal a
#         a = 30
#         print(a)
#     print(a)
#     inner()
#     print(a)

# info()

print(dir(__builtins__))

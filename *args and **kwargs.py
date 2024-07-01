# Introduction
"""
    * and ** are used to pass a variable number of arguments to functions.
    This is particularly useful when you don't know beforehand how many arguments might be passed.
"""

"""
The *args Syntax
 1. *args allows a function to accept any number of positional arguments.
 2. The args is just a name, you can use any name, but args is the convention.
"""

# Eg:
# def my_function(*args):
#     for arg in args:
#         print(arg)
#
# my_function(1, 2, 3)


"""
The **kwargs Syntax
 1. **kwargs allows a function to accept any number of keyword arguments.
 2. The kwargs is just a name, you can use any name, but kwargs is the convention.
"""


# Eg:
# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# my_function(name="Alice", age=30)



"""
Combining *args and **kwargs
    You can use both *args and **kwargs in the same function to accept both positional and keyword arguments.
"""

# Eg:
# def my_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
#
# my_function(1, 2, 3, name="Alice", age=30)


"""
Using * and ** for Argument Unpacking
 1. * can be used to unpack a list or tuple into positional arguments.
 2. ** can be used to unpack a dictionary into keyword arguments.
"""
# def my_function(a, b, c):
#     print(a, b, c)
#
# args = (1, 2, 3)
# my_function(*args)  # Equivalent to my_function(1, 2, 3)
#
# kwargs = {'a': 1, 'b': 2, 'c': 3}
# my_function(**kwargs)  # Equivalent to my_function(a=1, b=2, c=3)
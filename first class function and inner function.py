# 1. First-Class Functions in Python
# Definition: Python treats functions as "first-class citizens," meaning they can be passed around,
# assigned to variables, returned from other functions, and stored in data structures.

# Examples of First-Class Functions:
# 1. Assigning functions to variables:
# def greet(name):
#     return f"Hello, {name}!"
#
# say_hello = greet
# print(say_hello("Alice"))  # Output: Hello, Alice!

# 2. Passing functions as arguments:
# def greet(name):
#     return f"Hello, {name}!"
#
# def process_user_input(callback):
#     user_name = input("Please enter your name: ")
#     print(callback(user_name))
#
# process_user_input(greet)

# 3. Returning functions from other functions:
# def outer_function(message):
#     def inner_function():
#         return message
#     return inner_function
#
# my_function = outer_function("Hi!")
# print(my_function())  # Output: Hi!


# 2. Inner Functions
# Definition: A function defined inside another function is called an "inner function."
# They are often used to encapsulate logic or closures.

# Example of Inner Function:
# def outer():
#     def inner():
#         return "This is the inner function"
#     return inner()
#
# print(outer())  # Output: This is the inner function

# 3. Closure:
# A closure is a nested function that captures the local variables from its outer function
# and retains access to them even after the outer function has completed execution.

# def multiplier(factor):
#     def multiply_by_factor(number):
#         return number * factor
#     return multiply_by_factor
#
# times3 = multiplier(3)
# times5 = multiplier(5)
#
# print(times3(10))  # Output: 30
# print(times5(10))  # Output: 50


# Summary
# First-class functions allow Python to treat functions like objects.
# Inner functions help in encapsulating logic and creating closures.
# Closures retain access to the scope in which they were created
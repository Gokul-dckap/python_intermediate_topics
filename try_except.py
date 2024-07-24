"""
Introduction
handle exceptions detected during execution.
write robust code that handles unexpected errors
"""

"""
# Basic Syntax
try:
    # Code that might raise an exception
except SomeException as e:
    # Code that runs if the exception occurs
"""

# Basic Example
try:
    x = 10 / 0
except ZeroDivisionError as e: #
    print("Error: Division by zero is not allowed.")


"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# another example
try:
    num = int("jasmine")
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered a valid number.")
finally:
    print("This will always execute.")


# Introduction to Python Exception Hierarchy
# Definition: Exceptions are Python objects that represent errors.
# Python has a well-defined hierarchy for handling these exceptions.

# Exception Hierarchy Overview

    # 1. BaseException (Root of all exceptions)
    #    1. SystemExit
    #    2. KeyboardInterrupt
    #    3. GeneratorExit

    # 2. Exception (Subclasses of BaseException, used for most error handling)
    #     1. ArithmeticError (Base for errors like ZeroDivisionError)
        #    1. ZeroDivisionError
        #    2. OverflowError

        # 2. LookupError (Base for indexing errors)
        #     1. IndexError
        #     2. KeyError

        # 3. ImportError
        #     1. ModuleNotFoundError

        # 4. FileNotFoundError

        # 5. OSError

    # 3. Custom Exceptions (User-defined exceptions, subclassed from Exception)


# Examples for Each Level

# BaseException Example
# try:
#     raise BaseException("BaseException raised")
# except BaseException as e:
#     print(f"Caught: {e}")
#
# SystemExit Example
# import sys
# try:
#     sys.exit("Exiting program")
# except SystemExit as e:
#     print(f"Caught: {e}")
#
# KeyboardInterrupt  Example
# try:
#     while True:
#         pass  # Press Ctrl+C to trigger KeyboardInterrupt
# except KeyboardInterrupt:
#     print("Caught KeyboardInterrupt")
#
#
# Exception Example (ZeroDivisionError under ArithmeticError):
# try:
#     result = 1 / 0
# except ZeroDivisionError as e:
#     print(f"Caught: {e}")
#
#
# Example (KeyError under LookupError):
# try:
#     d = {"key": "value"}
#     value = d["nonexistent"]
# except KeyError as e:
#     print(f"Caught: {e}")
#
# Custom Exception Example
# class CustomError(Exception):
#     pass
#
# try:
#     raise CustomError("This is a custom exception")
# except CustomError as e:
#     print(f"Caught: {e}")


# Summary
# Hierarchy Importance: Catch specific exceptions, follow the hierarchy, and create custom exceptions when needed.
# Best Practices: Use Exception for standard errors and only catch broader exceptions when necessary.
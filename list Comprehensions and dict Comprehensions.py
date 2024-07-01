"""
Introduction
    List comprehensions and dictionary comprehensions provide a concise way to create lists and dictionaries.
    They are often more readable and concise than traditional loops.
"""

"""
List Comprehensions
    * A list comprehension provides a way to create lists in a single line.
    * The syntax is [expression for item in iterable if condition]
"""

# Example: Basic List Comprehension

# squares = [x**2 for x in range(11)]
# print(squares)


# Example: List Comprehension with Condition

# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)

"""
Nested List Comprehensions
You can use nested comprehensions to handle nested loops.
"""

# Example: Nested List Comprehension

# matrix = [[j for j in range(5)] for i in range(3)]
# print(matrix)

"""
Dictionary Comprehensions
A dictionary comprehension provides a way to create dictionaries in a single line.
The syntax is {key: value for item in iterable if condition}.
"""


# Example: Basic Dictionary Comprehension
# squares = {x: x**2 for x in range(10)}
# print(squares)

# Example: Dictionary Comprehension with Condition
# even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# print(even_squares)

"""
Nested Dictionary Comprehensions
    Like list comprehensions, dictionary comprehensions can also be nested.
"""

# Example: Nested Dictionary Comprehension
# nested_dict = {i: {j: j**2 for j in range(3)} for i in range(3)}
# print(nested_dict)

"""
Conclusion
List comprehensions and dictionary comprehensions provide a more readable and concise way to create lists and dictionaries.
They are powerful tools for transforming and filtering data.
"""
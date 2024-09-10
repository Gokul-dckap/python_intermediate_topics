from packages.math_operations import MathOperations
from packages.string_operations import StringOperations

# Create an instance of MathOperations
math_ops = MathOperations(10, 5)

# Use the methods from the MathOperations class
print(math_ops.add())        # Output: 15
print(math_ops.divide())     # Output: 2.0

# Create an instance of StringOperations
string_ops = StringOperations("hello")

# Use the methods from the StringOperations class
print(string_ops.to_uppercase())  # Output: HELLO
print(string_ops.count_vowels())  # Output: 2

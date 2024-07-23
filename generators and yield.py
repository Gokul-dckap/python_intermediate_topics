# 1. Introduction
# Generators are a simple way to create iterators in Python using functions.#
# They allow you to iterate over a sequence of values, meaning they generate items one at a time and only when required,
# which can be more memory-efficient than creating an entire list


# 2. What is a Generator?
# A generator is a function that returns an iterator object which we can iterate over (one value at a time).
# Instead of return, a generator uses yield to produce a series of values.

# 3. Using yield in a Function
# The yield statement pauses the function, saving its state, and later continues from there when next() is called.

# Example: Simple Generator
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(gen)
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

# 4. Generator Expressions
# Similar to list comprehensions but with parentheses instead of brackets.
# They are more memory efficient since they do not create the entire list at once.

# gen_exp = (x**2 for x in range(10))
# print(next(gen_exp))  # Output: 0
# print(next(gen_exp))  # Output: 1

# 6. Benefits of Generators
# Memory Efficiency: Generators only produce one item at a time and do not store the entire sequence in memory.
# Infinite Sequences: Useful for representing infinite sequences (e.g., streaming data).

# 7. Conclusion
# Generators provide a powerful tool for creating iterators with less memory overhead.
# yield allows functions to produce a sequence of results lazily, on demand.
# What is @wraps(func)?
# @wraps is a decorator provided by the functools module in Python.
# It's used when writing custom decorators to preserve the original function's metadata like its name, docstring,
# and other attributes.

# Why is it needed?
"""
When you use a decorator to wrap a function, the wrapper function replaces the original function.
This can cause the original function's name and docstring to be hidden by the wrapper.
Using @wraps fixes this by copying over the metadata from the original function to the wrapper function.
"""

# Example Without @wraps:
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")

print(say_hello.__name__)  # Output: wrapper
print(say_hello.__doc__)   # Output: None

# Without @wraps, the function's metadata is lost,
# and say_hello.__name__ becomes "wrapper" instead of "say_hello".


# Example With @wraps:

# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)  # This ensures the original metadata is retained
#     def wrapper(*args, **kwargs):
#         print("Function is being called")
#         return func(*args, **kwargs)
#     return wrapper

# @my_decorator
# def say_hello():
#     """This function says hello."""
#     print("Hello!")
#
# print(say_hello.__name__)  # Output: say_hello
# print(say_hello.__doc__)   # Output: This function says hello.

# Now, using @wraps(func),
# the original function's name (say_hello) and docstring (This function says hello.) are preserved

# In Summary:
# @wraps(func) is used to ensure that when you apply a decorator,
# the original function's metadata (like name and docstring) isn’t lost.
# It's a good practice when writing decorators to maintain the original function’s identity and documentation.
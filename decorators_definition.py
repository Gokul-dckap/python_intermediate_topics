# Basic Syntax.
"""
Decorators used to change the behavour of a function or class without permanently modifying it.
"""
def log_decorator(func):
    def wrapper():
        print(f"Function {func.__name__} is about to be called.")
        func()
        print(f"Function {func.__name__} was called.")
    return wrapper

@log_decorator
def display():
    print("Display function is running.")

display()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function called with arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(5, 10))

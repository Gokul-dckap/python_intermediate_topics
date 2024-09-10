# Example 1: Treating the functions as objects.

# def shout(text):
#     return text.upper()
#
# print(shout('Hello'))
#
# yell = shout
#
# print(yell('Hello'))

# Example 2: Passing the function as an argument

# def shout(text):
#     return text.upper()
#
# def whisper(text):
#     return text.lower()
#
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
#
# greet(shout)
# greet(whisper)
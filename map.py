# # We double all numbers using map()
# def addition(n):
#     return n + n
#
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# || -------------------------------------------------------- ||

# # List of strings

# l = ['dhanush', 'gokulapriyan', 'jeeva', 'brighty']
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# || -------------------------------------------------------- ||

# # Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(num):
#     if num % 2 == 0:
#         return num * 2
#     else:
#         return num
#
# numbers = [1, 2, 3, 4, 5]
# result = list(map(double_even, numbers))
# print(result)
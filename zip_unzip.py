# # Example with Equal Length Iterables:
# a = [1, 2, 3, 4]
# b = ["a", "b", "c", "d"]
#
# data = dict(zip(a,b))
# print(data)


# # Example with Unequal Length Iterables:
# a = [1, 2, 3, 4]
# b = ["a", "b", "c", "d", "e"]
#
# data = list(zip(a, b))
# print(data)


# # Example of Unzipping:
# zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
#
# numbers, letters = zip(*zipped)
#
# numbers = list(numbers)
# letters = list(letters)
#
# print(numbers)
# print(letters)

# Unzipping a Dictionary:
age_dict = {'Alice': 25, 'Bob': 30, 'Charlie': 35}

items = age_dict.items()
names, ages = zip(*items)

names = list(names)
ages = list(ages)

print(names)
print(ages)


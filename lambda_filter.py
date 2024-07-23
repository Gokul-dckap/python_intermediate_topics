# Lambda Function
#Syntax  lambda arguments: expression

# # #single Arguement
add_10 = lambda x: "You are a adult" if x > 18 else "You are a child"
print(add_10(20))


# # Multiple Arguement
multiply = lambda x, y, z: (x * y) - z
print(multiply(2, 3, 4))  # Output: 6



#Filter Function

# #syntax : filter(function, iterable)
def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = filter(is_even, numbers)
print(list(filtered_numbers))  # Output: [2, 4, 6]


# # Combine filter and lambda function
ages = [1, 4, 5, 7, 8, 20]
filtered_ages = filter(lambda age: age > 18, ages)
print(list(filtered_ages))  # Output: [20]
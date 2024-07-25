# 1. Introduction
# #File handling in Python allows you to read, write, and manipulate files.
# It is a fundamental skill for managing data storage and retrieval.


#2. Opening and Closing Files
# Use the open() function to open a file. It returns a file object.
# Use the close() method to close the file.

# Example: Opening and Closing a File
# file = open('example.txt', 'w')
# file.write('Hello, world!')
# file.close()

# 3. Using with Statement
# The with statement handles opening and closing files automatically.
# Example: Using with Statement
# with open('example.txt', 'w') as file:
#     file.write('Hello, world!')


# 4. Reading Files
# Read the entire file using read().
# Read line by line using readline() or readlines()

# Example: Reading Entire File
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)

# Example: Reading Line by Line
# with open('example.txt', 'r') as file:
#     content = file.readlines()
#     print(content)


#         5. Writing to Files
# Use write() to write a string to a file.
# Use writelines() to write a list of strings.

# Example: Writing to a File
# with open('example.txt', 'w') as file:
#     file.write('Hello, world!\n')
#     file.write('Python is awesome!')

# Example: Writing Multiple Lines
# lines = ['Hello, world!\n', 'Python is awesome!\n']
# with open('example.txt', 'w') as file:
#     file.writelines(lines)


#                 6. File Modes
# 'r': Read (default mode)
# 'w': Write (creates a new file or truncates an existing file)
# 'a': Append (writes data to the end of the file)
# 'b': Binary mode (e.g., 'rb', 'wb')
# '+': Read and write (e.g., 'r+', 'w+', 'a+')

# Example: Append Mode
# with open('example.txt', 'a') as file:
#     file.write('\nAppending a new line.')

#             7. Working with Binary Files
# Useful for non-text files like images or executable files.

# Example: Reading a Binary File
# with open('example.jpeg', 'rb') as file:
#     data = file.read()
#     print(data[:10])  # Print the first 10 bytes


#                         8. Conclusion
# File handling in Python is essential for reading and writing data.
# The with statement is recommended for managing file resources efficiently.

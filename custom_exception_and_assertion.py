# #example 1 : Defining Custom Exceptions
#
# # define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass
#
#
# # you need to guess this number
# number = 18
#
# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
#
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")


# #example 2 : Customizing Exception Classes
#
# class SalaryNotInRangeError(Exception):
#     """Exception raised for errors in the input salary.
#
#     Attributes:
#         salary -- input salary which caused the error
#         message -- explanation of the error
#     """
#
#     def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)
#
#
# salary = int(input("Enter salary amount: "))
# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)


##-----------------------------------------------------------------------------------------##

#Python assert Statement

# #Example 1: Using assert without Error Message
#
# def avg(marks):
#     assert len(marks) != 0
#     return sum(marks)/len(marks)
#
# mark1 = []
# print("Average of mark1:",avg(mark1))


# #Example 2: Using assert with error message
#
# def avg(marks):
#     assert len(marks) != 0,"List is empty."
#     return sum(marks)/len(marks)
#
# mark2 = [55,88,78,90,79]
# print("Average of mark2:",avg(mark2))
#
# mark1 = []
# print("Average of mark1:",avg(mark1))
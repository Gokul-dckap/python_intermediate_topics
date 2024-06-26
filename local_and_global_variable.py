# # example for local variable
#
# def fun1():
#     x = 5
#     print ("x value is ",x)
#
# def fun2():
#     x = 10
#     print("x value is ",x)
#     fun1()
#
# fun2()

# # example for global variable
#
# n = 10
#
# def fun1():
#     print("value of n is ",n)
#
# def fun2():
#     print("value of n is ",n)
#     fun1()
#
# fun2()

# # what if we want update the global variable
#
# var = 10
#
# def fun1():
#     # global var
#     var = var+1
#     print ("variable value in fun1 is ",var)
#     return
#
# fun1()
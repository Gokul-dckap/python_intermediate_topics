"""
Introduction
Pip is package manager for python.
It is used to install, upgrade, configure and remove python package and their dependencies.
"""

"""
Basics Commands
Installing a package: "pip install package_name"
Uninstalling a package: "pip uninstall package_name"
Listing installed packages: "pip list"
Display about the information: "pip show package_name"
Upgrade package: "pip install --upgrade package_name"
"""

"""
Modules
A module in Python is a file containing Python code that defines functions, classes, variables, and runnable code. 
Modules are used to organize and reuse code across multiple programs or projects. 
"""

# import requests
# response = requests.get('https://api.github.com')
# print(response.json())
#
#
# import pyfiglet
#
# result = pyfiglet.figlet_format("jasmine!")
# print(result)
#
#
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["Name", "Age", "City"]
# table.add_row(["Alice", 30, "New York"])
# table.add_row(["Bob", 25, "Los Angeles"])
# print(table)

from modules import MathOperation as math

data = math(1,2)
print(data.subtract())
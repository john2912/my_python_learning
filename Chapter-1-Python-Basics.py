#Intro-to-Python-for-Data-Science-Data-Camp
#Chapter 1 Python Basics.py

###The Python Interface
print(5 / 8)
print(7 + 10)

###Any Comments?
# Just testing division
print(5 / 8)

# Addition works too
print(7 + 10)

###Python As A Calculator
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print(100 * 1.1**7)

###Variable Assignment
# = in Python means assignment, not equality
# Create a variable savings
savings = 100

# Print out savings
print(savings)

###Calculations With Variables
# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.10

# Calculate result
result = savings * factor ** 7

# Print out result
print(result)

###Other Variable Types
# int: Integer
# float: Integer and decimal
# str: String
# bool: Boolean
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True

###Operations With Other Types
# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of factor and savings to year1
year1 = savings * factor

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

###Type Conversion
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)

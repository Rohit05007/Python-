a = 1  #  Variable = container to store a value

b = "Rohit"  # Keywords = reserved words in python

c = 71.22  # Identifiers = class / function /variable name
print(a + c)

# Data types---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 1  # a is an integer

b = 5.44  # b is a floating point number

c = "Rohit"  # c is a string

d = False  # d is boolean variable

e = None  # e is a none type variable

# Variables rules------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = 65

aaa = 599

rohit = 34

sumit = 78

_sumit = 87

# @sumit = 56 # Invalid due to @ symbol
# s@meer # Invalid due to @ symbol

# Operators in python--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# (1) Arithmetic operators

a = 7
b = 4
c = a + b
print(c)

# (2) Assignment operators
a = 4 - 2  # Assign 4-2 in a
print(a)
# b+=3 # Increment the value of  b by 3 and then assign it to b
b -= 3  # Decrement the value of  b by 3 and then assign it to b
print(b)

# (3) Comparision operartors
d = 5 < 4
print(d)

e = 5!=5
print(e)

#(4) Logical operators 
e =True or False
print(e)

# Truth table of 'or'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("True or False is ",True or False)
print("True or True is ",True or True)
print("False or True is ",False or True)
print("False or False is ",False or False)

# Truth table of 'and'------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Trueand False is ",True and False)
print("True and True is ",True and True)
print("False and True is ",False and True)
print("False and False is ",False and False)

print(not(True)) # True to False 

# Type funtion and type casting ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
c = 25
e =type(c) # class <int>
print(e)

f = "31.2"
g = type(f)# class<str>
print(g)

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 
print(t)

str(31)     # => "31"   # integer to string conversion
int("32")   # => 32     # string to integer conversion
float(32)   # => 32.0   # integer to float conversion

# Input function ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a = int(input("Enter number 1: "))

b = int(input("Enter number 2: "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)
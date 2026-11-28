name = "Tannu"
print(name)
#no variable declaration is required in python. It is dynamicall.

#Dynamic Binding: Jab ek variable multiple data types ko hold kar sakta hai, to usse dynamic binding kehte hai.
name = 20
print(name)

name = True
print(name)

#keywords
age = 20
if age  >=18:
    print("Adult")
else:                     #here if and else are keywords.
    print("Not Adult")

# Identifiers
name = "Tannu"
age = 20
college = "AEC"
# name,age, college are variable identifiers
def calculate_sum():
    pass
# calculate_sum is function identifier.
class Student:
    pass
#student is class identifier.

import keyword

print(keyword.kwlist) #this will print all the keywords in python.

print(keyword.iskeyword("if")) 
print(keyword.iskeyword("name"))





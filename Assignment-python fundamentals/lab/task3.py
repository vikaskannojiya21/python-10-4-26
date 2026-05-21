# Program to demonstrate Python code structure


def greet_user():
    name = input("Enter your name: ")
    
    print("Hello,", name)
    print("Welcome to Python programming!")


greet_user()

print("*"*80)
# Program to demonstrate creation of variables in Python

name = "Vikas"
age = 20
height = 5.9
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

print("*"*80)
# Program to take user input using input() function

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("City:", city)

print("*"*80)

# Program to check type of variables using type()

name = "Vikas"
age = 20
height = 5.9
is_student = True

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))

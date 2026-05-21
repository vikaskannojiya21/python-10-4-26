# Program to check whether a number is greater or less than 50

num = int(input("Enter a number: "))

if num > 50:
    print("Number is greater than 50")
else:
    print("Number is less than or equal to 50")

print("*"*80)

# Program to check whether a number is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Number is NOT Prime")
            break
    else:
        print("Number is Prime")
else:
    print("Number is NOT Prime")
print("*"*80)

# Program to calculate grade based on percentage

percentage = float(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")
print("*"*80)
# Program to check blood donation eligibility using nested if

age = int(input("Enter your age: "))
weight = int(input("Enter your weight (kg): "))

if age >= 18:
    
    if weight >= 45:
        print("You are eligible to donate blood")
    else:
        print("Not eligible: Weight must be at least 45 kg")
        
else:
    print("Not eligible: Age must be 18 or above")

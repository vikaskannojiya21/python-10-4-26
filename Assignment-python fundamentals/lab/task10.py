# Program to square numbers using map() function

numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

result = map(square, numbers)

print("Squared Numbers:", list(result))

# Program to find product of a list using reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5]

def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)

print("Product of list:", result)
# Program to filter even numbers using filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

result = filter(is_even, numbers)

print("Even Numbers:", list(result))

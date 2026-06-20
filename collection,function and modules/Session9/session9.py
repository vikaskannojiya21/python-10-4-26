#1
square = lambda x: x * x

for i in range(1, 6):
    print(square(i))

#2
prices = [120, 250, 99, 180, 310]

new_prices = list(map(lambda x: x + (x * 0.10), prices))

print(new_prices)
#3
users = [
    ('raj', 800),
    ('simran', 1500),
    ('veer', 1200),
    ('ananya', 950)
]

result = list(filter(lambda x: x[1] > 1000, users))

for user in result:
    print(user[0])

#4
calculate = lambda a, b: (a+b, a*b)

print(calculate(3, 4))
print(calculate(5, 2))
print(calculate(7, 8))
#5
palindrome = lambda text: text == text[::-1]

print(palindrome("madam"))
print(palindrome("python"))
print(palindrome("noon"))

    

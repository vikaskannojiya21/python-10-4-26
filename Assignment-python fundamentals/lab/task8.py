# Program to skip 'banana' using continue statement

List1 = ['apple', 'banana', 'mango']

for item in List1:
    if item == 'banana':
        continue
    print(item)
# Program to stop loop when 'banana' is found

List1 = ['apple', 'banana', 'mango']

for item in List1:
    if item == 'banana':
        break
    print(item)

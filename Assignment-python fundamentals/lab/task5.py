List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    print(fruit)
print("*"*50)

List1 = ['apple', 'banana', 'mango']

for fruit in List1:
    print(f"The length of {fruit} is {len(fruit)}")
print("*"*50)
List1 = ['apple', 'banana', 'mango']
search = 'banana'

for fruit in List1:
    if fruit == search:
        print(search, "found in the list")
        break
print("*"*50)
for i in range(1, 6):        
    for j in range(i):       
        print("*", end="")
    print()                  

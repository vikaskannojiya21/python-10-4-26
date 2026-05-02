sum=0
i=1
while i<=10:
    if i%2==0:
        sum=sum+i
    i=i+1
    
print(sum)

print("-"*50)

sum=0
i=1
while i<=20:
    if i%3==0 and i%5==0:
        sum=sum+i
    i=i+1
    
print(sum)
print("*"*50)

for i in range(1,16):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
print("$"*50)

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


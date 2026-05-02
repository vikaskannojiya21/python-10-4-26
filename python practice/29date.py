for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()
        
print("*"*50)

for i in range(1,31):
    if i%2==0 and i%3==0:
        print(i)
print("*"*50)

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
        
print("*"*50)

n=10
a=0
b=1
print(a)
for i in range(n):
    print(b)
    a,b=b,a+b

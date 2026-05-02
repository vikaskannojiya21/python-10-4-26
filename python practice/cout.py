number=int(input("input number"))
fib=[]
a=0
b=1
for i in range(number):
    fib.append(a)
    a,b=b,a+b

print("fibannoci:",fib)
    

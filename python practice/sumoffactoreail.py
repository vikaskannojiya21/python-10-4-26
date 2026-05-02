total=0
for i in range(1,11):
    fact=1
    for n in range(1,i+1):
        fact=fact*n
    total=total+fact
    print("factorial of ",i,"=",fact)

print(total)

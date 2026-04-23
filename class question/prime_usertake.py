n=int(input("kitna number enter karna hain:"))
number=[]
prime_list=[]

for i in range(n):
    num=int(input("number enter karo:"))
    number.append(num)
print("original list:",number)

print("prime number in list:")

for n in number:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
          prime_list.append(n)
print(prime_list)
                

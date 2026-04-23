n=int(input("kiten number enter karna="))
number=[]
factnum=[]
for i in range(n):
    num=int(input("number enter karo:"))
    number.append(num)
print("original list,",number)

print("factorial of each number:")

            
for num in number:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is:" ,fact)
        
    

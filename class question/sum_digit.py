number=[ 123,45,67]
result=[]
for num in number:
    n=num
    total=0

    while n>0:
        digit=n%10
        total=total+digit
        n=n//10
        
    result.append(total)
    
    print("sum of digit list",result)

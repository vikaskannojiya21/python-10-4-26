number=[123,334,55]
sum=0
for dig in number:
        i=dig
        while i>0:
            digit = i%10
            sum=sum+digit
            i=i//10
            
print ("sum of digit",sum)

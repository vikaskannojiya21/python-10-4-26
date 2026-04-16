n=int(input("enter n:"))

while n>0:
    print("hello world")
    n=n-1

print("----------------------------")

num=int(input("enter num:"))
sum=0
while num>0:
    sum=sum+num
    num=num-1
print("sum:",sum)


print("----------------------------")


#0 1 1 2 3 5 8....89
a,b=0,1
c=int(input("enter num:"))
print(a,end="")
while b<c:
    print(b,end="")
    a,b=b,a+b
print()

    
print("----------------------------")


d=int(input("enter num:"))
if d%2!=0:
      for i in range(3,int(d/2),2):
          if d%i==0:
              print(d,"is not prime")
              break
      else:
          print(d, " is prime")
else:
    print(d,"is not prime")
      

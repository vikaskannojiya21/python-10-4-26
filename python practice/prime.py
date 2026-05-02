n=int(input("enter num:"))
if n%2!=0:
      for i in range(3,n,2):
          if n%i==0:
              print("is not prime")
              break
      else:
          print(n,"is prime")
else:
    print(n,"is not prime")

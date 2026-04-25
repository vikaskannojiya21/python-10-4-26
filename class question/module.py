import udf
while True:
    print("*"*50)
    print("1.oddeven")
    print("2.maxoftwo")
    print("3.maxofthree")
    print("4.fibonaci")
    print("5.prime")
    print("6.exit")
    print("*"*50)

    choice=int(input("enter your choice:"))
    print("*"*50)
    if choice==1:
        a=int(input("enter value"))
        udf.oddeven(a)
    elif choice==2:
        a=int(input("enter value"))
        b=int(input("enter value"))
        udf.maxoftwo(a,b)
    elif choice==3:
         a=int(input("enter value"))
         b=int(input("enter value"))
         c=int(input("enter value"))
         udf.maxofthree(a,b,c)
              
    elif choice==4:
        n=int(input("enter value"))
        udf.fibonacci(n)
    elif choice==5:
        n=int(input("enter value"))
        udf.prime(n)
    elif choice==6:
        print("thank you")
        break
    else:
        print("invalid try again")
    
        
        
        
        

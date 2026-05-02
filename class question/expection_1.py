print("start code")
try:
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a/b
    print(c)

except ZeroDivisionError as e:
    print("expection caught")
print("end code")

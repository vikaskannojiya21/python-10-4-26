print("start code")
try:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    c=a/b
    print("div:",c)
    l1=[12,22,34,45,67]
    index=int(input("enter index number:"))
    print(l1(index))
#except ZeroDivisionError as e:
   # print("Exception caught :",e)
#except ValueError as e:
    #print("Exception caught :",e)
#except IndexError as e:
     #print("Exception caught :",e)
except Exception as e:
   print("Exception caught :",e)
finally:
    print("finally block called")
print("end code")

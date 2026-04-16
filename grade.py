roll=int(input("enter your roll no"))
name=input("Enter your name=")
s1=int(input("Enter marks of subject1="))
s2=int(input("Enter marks of subject2="))
s3=int(input("Enter marks of subject3="))

total=s1+s2+s3
per=total/3

print("Roll_no=",roll)
print("Name=",name)
print("Total=",total)
print("percentage =",per)

if per>=70:
    print("Distinction")
elif per>=60:
    print("first class")
elif per>=50:
    print("Second class")
elif per>=40:
    print("pass")
else:
    print("fail")
    

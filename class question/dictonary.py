student={
    "amit": 83,
    "rahul":90,
    "sita":45,
    "vikas",67
}
name=input("enter student name=")
if name in student:
    print(name,"marks:",students[name])
else:
    print("student not found")
    

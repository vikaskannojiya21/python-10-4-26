student={
     "amit":56,
    "rahul":78,
    "vikas":90
    }
print("original dictionary:",student)

name=input("enter student name to upadte:")

if name in student:
    new_marks=int(input("enter new upadte:"))
    student[name]=new_marks
    print("update dictonary:",student)
else:
    print("studnet not found")
    

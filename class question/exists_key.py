student = {
    "amit": 56,
    "rahul": 89,
    "vikas": 49
}

key = input("Enter student name to check: ")

if key in student:
    print(key, "exists in dictionary with marks:", student[key])
else:
    print(key, "does not exist in dictionary")

student = {"A": 56, "B": 89, "C": 72}


max_value = student["A"]

for value in student.values():
    if value > max_value:
        max_value = value
    

print("Maximum value:",max_value)

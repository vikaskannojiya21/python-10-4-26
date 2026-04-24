n = int(input("Enter a number: "))

table = []

for i in range(1, 11):
    multi=n * i
    table.append(multi)

print("Multiplication table:", table)

n=int(input("kitna number enter karna hai:"))

number=[]
even_number=[]

for i in range(n):
    num=int(input("number enter karo:"))
    number.append(num)
print("orginal list:",number)

print("even number:")
for num in number:
    if num%2==0:
      #  print(num)
        even_number.append(num)
print("even list:",even_number)

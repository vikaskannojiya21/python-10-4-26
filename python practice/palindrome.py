name=input("Enter name")

rev=""
for ch in name:
    rev=ch+rev
if name==rev:
    print(name,"is palindrome")
else:
    print(name,"is not palindrome")
    

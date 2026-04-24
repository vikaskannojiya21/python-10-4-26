t = (10, 20, 30, 40, 50)

element = int(input("Enter element to search: "))

if element in t:
    print(element, "exists in tuple")
else:
    print(element, "does not exist in tuple")

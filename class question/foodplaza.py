#class Foodplaza:
    #r1=Foodplaza()
bill = 0

while True:

    print("\n----- Select Item -----")
    print("1. Pizza - 200rs")
    print("2. Burger - 100rs")

    item = int(input("Enter your item: "))

    if item == 1:
        print("You selected Pizza")
        bill += 200

    elif item == 2:
        print("You selected Burger")
        bill += 100

    else:
        print("Invalid item")

    choice = input("Do you want to order more? (yes/no): ")

    if choice == "no":
        print("Your total bill is:", bill)
        print("Thank you! Visit again")
        break
    

class Restaurant:

    def __init__(self):
        self.bill = 0


    def order(self, item):

        if item == 1:
            print("Pizza selected")
            self.bill += 200

        elif item == 2:
            print("Burger selected")
            self.bill += 100

        elif item == 3:
            print("current Bill =", self.bill)

        elif item == 4:
            print("Total Bill =", self.bill)
            print("Thank you! Visit again")
            return False
        else:
            print("invalid choice")

        return True
r1=Restaurant()
while True:
    print("\n1. Pizza 200")
    print("2. Burger 100")
    print("3. show bill")
    print("4. Exit")

    item=int(input("enter choice:"))
    if r1.order(item)==False:
        break

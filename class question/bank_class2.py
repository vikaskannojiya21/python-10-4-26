class Bank:
    
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("hello",cname,"your Account number ",acno,"is opended for",balance,"RS.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("sorry you need another ",amount-self.balance,"Rs.to withdraw")
    def checkbalance(self):
        print("your current balance is:",self.balance)
b1=Bank()
b1.openAccount(101,"vikas",1000)
while True:
    print("*"*50)
    print("1.Deposit")
    print("2.withdraw")
    print("3.checkbalance")
    print("4.exist")

    choice=int(input("enter your choice"))
    if choice==1:
        amount=int(input("Enter Deposit Amount:"))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("Enter Deposit Amount:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        print("Thank you for using our service")
        print("*"*50)
        break
    else:
        print("invalid choice,please try again")
    print("*"*50)

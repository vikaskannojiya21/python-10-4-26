class bank:
    def openAccount(self,acno,cname,balance):
        self.acno=acno
        self.cname=cname
        self.balance=balance
        print("hello",cname,"Your Account number",acno,"is open with",balance,"Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("sory you need another ",amount-self.balance,"rs")
    def checkbalance(self):
            print("your current balance is :",self.balance)
b1=bank()
b1.openAccount (101,"vikas",1000)
while True:
    print("*"*50)
    print("1.Deposite")
    print("2.withdraw")
    print("3.check balance")
    print("4.Exit")
    print("*"*50)\

    choice=int(input("enter your choice:"))
    
    if choice==1:
        amount=int(input("Enter deposite amount:"))
        b1.deposit(amount)
    elif choice==2:
        amount=int(input("enter withdraw amount:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        print("thank you")
        print("*"*50)
        break
       
    else:
        print("inavlid choice")
    print("*"*50)

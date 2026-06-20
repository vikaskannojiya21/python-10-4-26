'''class A:
    def setdata(self,name,salary):
        self.name=name
        self.salary=salary
    def update(self,newsalary):
        self.salary=newsalary
    def show(self):
        print("Name:",self.name)
        print("salary:",self.salary)
obj=A()
obj.setdata("vikas",30000)
obj.show()
obj.update(4000)
obj.show()'''

class B:
    def setdata(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount
    def show(self):
        print("Name:",self.name)
        print("balance:",self.balance)
obj1=B()
obj1.setdata("vikas",1000)
obj1.show()
obj1.deposit(2000)
obj1.show()
obj1.withdraw(300)
obj1.show()










                 
    

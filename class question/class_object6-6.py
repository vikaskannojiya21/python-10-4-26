class Sale:
    def setdata(self,p_name,price):
        self.p_name=p_name
        self.price=price
    def Afterdic(self,discount):
        self.price=self.price-(self.price*discount/100)
    def show(self):
        print("Product name: ",self.p_name)
        print("Price: ",self.price)
b1=Sale()
b1.setdata("soap",100)
b1.show()

#single
print("*"*50)
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

obj=B()
obj.getA(10)
obj.getB(20)
obj.putA()
obj.putB()

print("*"*50)

#multilevel
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)
    
obj=C()
obj.getA(100)
obj.getB(200)
obj.getC(300)
obj.putA()
obj.putB()
obj.putC()
print("*"*50)
#multiple
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

obj=B()
obj1=C()

obj.getA(1000)
obj.getB(2000)
obj.putA()
obj.putB()

obj1.getA(3000)
obj1.getC(4000)
obj1.putA()
obj1.putC()
print("*"*50)
#hirachical
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

b=C()
b.getA(1500)
b.getB(2500)
b.getC(3500)
b.putA()
b.putB()
b.putC()
print("*"*50)
#Hybrid

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A :",self.a)
    

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B :",self.b)

class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C :",self.c)

class D(B,C):
    
    def getD(self,d):
        self.d=d
    def putD(self):
        print("D :",self.d)
d=D()
d.getA(1500)
d.getB(2500)
d.getC(3500)
d.getD(4500)

d.putA()
d.putB()
d.putC()
d.putD()





















obj.putC()

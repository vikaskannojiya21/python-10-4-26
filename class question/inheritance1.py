#single inheritanc
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)

b1=B()
b1.getA(10)
b1.getB(20)
b1.putA()
b1.putB()
#multilevel inheritanc
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)

b1=C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB()
b1.putC()
#multiple
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B:
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A,B):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
b1=C()
b1.getA(10)
b1.getB(20)
b1.getC(30)
b1.putA()
b1.putB()
b1.putC()
#hirachical
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
class D(A):
    def getD(self,D):
        self.d=d
    def putD(self):
       print("D:",self.D)

b1=B()       
c1=C()
d1=D()
b1.getA(20)
b1.getB(10)
c1.getC(20)
d1.getD(30)
bl.putA()
b1.putB()
c1.putC()
d1.putD()

#hybrid
class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A:",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B:",self.b)
class C(A):
    def getC(self,c):
        self.c=c
    def putC(self):
        print("C:",self.c)
class D(B,C):
    def getD(self,D):
        self.d=d
    def putD(self):
       print("D:",self.D)
b1=D()
b1.getB(10)
b1.getC(20)
b1.getD(30)
b1.putB()
b1.putC()
b1.putD()




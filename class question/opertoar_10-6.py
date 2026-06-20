class Point:
    def __init__(self,x,y):
        print("init called")
        self.x=x
        self.y=y
    def __str__(self):
        print("str called")
        return"({0},{1})".format(self.x,self.y)
    def __add__(self,vikas):
        print("add called")
        x=self.x+vikas.x
        y=self.y+vikas.y
        return Point(x,y)
p1=Point(10,20)
p2=Point(40,60)
print(p1)
print(p2)
print("Addition of 2 object:",p1+p2)

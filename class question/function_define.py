 # it is set of  instruction that perfrom a sepecific task there are two type of fuction are available 1 library and user defin function

 # function with no argument and no return values

def printline():
     print("*"*50)
printline()
print("hello world")
printline()

 #function with argument but no return values

def add(a,b):
     print("Addition:",a+b)
printline()
x=int(input("enter number"))
y=int(input("enter number"))
add(x,y)
printline()


 #function with argument and return values
def sub(a,b):
     return a-b
printline()
x=int(input("enter number"))
y=int(input("enter number"))
print("substraction",sub(x,y))


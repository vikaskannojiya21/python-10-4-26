
#function with no argument and no return value.
def printline():
    print("*"*50)
printline()
print("welcome to user defined fuctuion in python")
printline()

#function with argument but no return value.

def add(a,b):
    print("Add:",a+b)
printline()
x=int(input("Enter value:"))
y=int(input("Enter value:"))
add(x,y)
printline()

#function with argument and return value.

def sub(a,b):
    return a-b
printline()
x=int(input("Enter value:"))
y=int(input("Enter value:"))
#ans=sub(x,y) store karne ka  jab  baar baar use karna ho
print("sun:",sub(x,y))# ek baar print karna ho to is tarah likh na ka
#print(ans)
printline()

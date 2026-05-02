def square(n):
    for i in range(n):
        yield i*i

squ= square(5)
for i in squ:
    print(i)
print("--"*50)

def demo():
    print("start")
    yield 1
g=demo()

print("after call")
for i in g:
    print(i)

print("---"*50)

def even(num):
    for i in num:
        if i%2==0:
            yield i*i
g=even([1,2,3,4,5,6])
for i in g:
    print(i,end=" ")
    
print("---"*50)

def grater(num):
    for i in num:
        if i >10:
            yield i
big=grater([5,10,15,20,25])
for i in big:
    print(i)
print("---"*50)

def cube(num):
   for i in num:
       if i%2==0:
           yield i*i*i
g=cube([1,2,3,4,5,6,7,8,9,10])
for i in g:
   print(i)
       

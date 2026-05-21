l=[]
for i in range(2000,3201):
    if i%5==0 and i%7!=0:
        l.append(i)
print(l)

print("*"*50)
#stack last in first out
a=[]
a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.append(40)
print(a)
a.append(50)
print(a)

a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)

print("*"*80)
#deque
from _collections import deque
l=deque([])
l.append(10)
print(list(l))
l.append(20)
print(list(l))
l.append(30)
print(list(l))
l.append(40)
print(list(l))
l.append(50)
print(list(l))

l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))
l.popleft()
print(list(l))








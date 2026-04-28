from functools import reduce

def add(x,y):
    return x+y

num=[1,2,3,4,5]

result=reduce(add,num)
print(result)

print("--"*50)

def add(x,y):
    return x+y

num=[1,2,3,4,5]

result=reduce(add,num,100)# start from 100
print(result)

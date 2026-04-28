def cube(x):
    return x*x*x
l=[1,2,3,4,5,6,7,8,9]

ans=list(map(cube,l))
print(ans)

print("---"*50)

print("map with lambda function")
      
num=[1,2,3,4,5]
sqaure=map(lambda x:x*x,num)
print(list(sqaure))

print("---"*50)

num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
add=map(lambda x,y:x+y,num1,num2)
print(list(add))

print("---"*50)

words=["vikas","abcd","hello"]
capital=map(lambda word:word.upper(),words)
print(list(capital))

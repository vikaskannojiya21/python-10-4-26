t=(20,10,25,50,10,25)

elemnt=int(input("enter element to count:"))
count=0
for item in t:
    if item==elemnt:
           count=count+1
print(elemnt,"appear",count,"time in tuple")

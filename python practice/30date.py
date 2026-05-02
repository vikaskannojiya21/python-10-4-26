num=[12,45,7,89,23]
max_num=num[0]
for i in num:
    if i > max_num:
        max_num=i
print("max:",max_num)
print("--"*50)
nums=[10,20,30,40]
sum=0
for i in nums:
    sum+=i
print("total:",sum)
print("--"*50)
nums=[1,2,3,4,5,6,7,8]
for i in nums:
    if i%2==0:
        print("Even:",i)
print("--"*50)
nums=[3,5,7,2,9]
sum=0
for i in nums:
    if i>=5:
        sum+=i
print("sum of above of five:",sum)

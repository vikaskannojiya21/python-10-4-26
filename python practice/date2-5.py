nums=[15,8,22,5,31]
min_value=nums[0]
for i in nums:
    if i< min_value:
        min_value=i
print(min_value)
print("--"*50)
nums=[4,9,2,7,6]
for i in nums:
    if i%2!=0:
        squ=i*i
        print(squ)
print("---"*50)
nums=[10,25,30,15,8]
for i in nums:
    if i>10:
     print(i)
print("---"*50)
nums=[5,2,9,1,7]
max_value=nums[0]
min_value=nums[0]
for i in nums:
    if i>max_value:
        max_value=i
    if i<min_value:
        min_value=i
print(max_value)
print(min_value)
print("---"*50)
nums = [2, 4, 6, 8]
multi=1
for i in nums:
    multi=multi*i
print(multi)
print("---"*50)
nums=[1,2,3,4,5,6]
pro=1
for i in nums:
    if i%2==0:
        pro=pro*i
print(pro)

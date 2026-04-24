t=(19,30,45,5,6,10,11)
min_val=t[0]
max_val=t[0]
for num in t:
    if num > max_val:
        max_val=num
    if num < min_val:
        min_val=num

print("maximum",max_val)
print("minimum",min_val)

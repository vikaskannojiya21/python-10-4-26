
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print("---------------------")

for i in range(6):
    for k in range(6-i-1):
        print(" ",end=" ") 
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
    
print("---------------------")

for i in range(1,6):
    for k in range(5-i):
        print(" ",end=" ") 
    for j in range(2*i-1):
        print(chr(65+j),end=" ")
    print()
print("---------------------")

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end=" ") 
    for j in range(2*i-1):
        print(chr(65+j),end=" ")
    print()




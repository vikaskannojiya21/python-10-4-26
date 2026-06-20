import random
data=open("data.txt","w")
for i in range(10):
    num=random.randint(1,100)
    data.write(str(num)+",")
data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.txt","w")
prime=open("prime.txt","w")

l=data.read().split(",")[:-1]
for i in l:
        if int(i)%2==0:
          even.write(i+",")
        else:
            odd.write(i+",")

        if int(i)%2!=0:
            for a in range(3,int(int(n)):
                if int(n)%a==0:
                    break
                else:
                    prime.write(n+",")
                    
data.close()
even.close()
odd.close()
prime.close()



print("data file content")
data=open("data.txt","r")
print (data.read())
data.close()

print("even file content")
even=open("even.txt","r")
print (even.read())
even.close()

print("odd file content")
odd=open("odd.txt","r")
print (odd.read())
odd.close()

print("prime file content")
prime=open("prime.txt","r")
print(prime.read())
prime.close()


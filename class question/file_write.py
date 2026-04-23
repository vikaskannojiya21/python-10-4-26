data=open("text.txt","w")
data.write("hello vikas")
data .close()


data=open("text.txt","r")
print(data.read())
data.close()

data.append("text.txt","a")
data.write("\n this file is now append")
data.close()


data=open("text.txt","r")
print(data.read())
data.close()

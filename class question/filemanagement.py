print("*"*50)
file=open("tops1.txt","w")
file.write("this is file management demo using python")
file.close()
print("*"*50)

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*50)


file=open("tops1.txt","a")
file.write("\nthis  fileis now append")
file.close()
print("*"*50)


file=open("tops1.txt","r")
print(file.read())
file.close()
print("*"*50)


file=open("tops2.txt","w+")
file.write("this is W+ mode using python")
print("current cursor position:",file.tell())
file.seek(0)
print(file.read())
file.close()
print("*"*50)




            

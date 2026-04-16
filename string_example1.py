s=input("enter sting")
nm=0
al=0
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1
print("Total apha +" ,al)
print("Total numeric +" ,nm)
print("Total space +" ,sp)
print("Total upper+" ,uc)
print("Total lower+" ,lc)

      

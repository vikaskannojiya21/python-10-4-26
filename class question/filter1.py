l1=["anjali","priyanshi","om","ashvi"]

def findvowels(name):
    if name[0] in "aeiou":
        return name
l2=list(filter(findvowels,l1))
print(l2)

print("--"*50)
print("filter with lambda")

string=["hello","","world","","python",""]
non_empty_string=filter(lambda x:x!="",string)

print(list(non_empty_string))
print("--"*50)


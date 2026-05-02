name=input("enter a string")
count=0
for ch in name:
    if ch in "aieouAIEOU":
        count = count+1
print("total vowels",count)

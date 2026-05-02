import json
user_data={}
user_data["name"]=input("Enter your name:")
user_data["age"]=int(input("enter your age:"))
user_data["city"]=input("enter your city:")

with open ("user_data.json","w") as file:
    json.dump(user_data, file, indent=4)
print("data added!!")

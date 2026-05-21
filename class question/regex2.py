import re
print("Match function")
print(re.match(r,'dog','Dog dog cat',re.IGNORECASE))
print("Serach function")
print(re.search(r,'dog','cat dog cat',re.IGNORECASE))

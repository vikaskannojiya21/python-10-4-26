import re
phone="2004-959-559ABC % This is phone number"
num=re.sub(r'%.*$'," ",phone)
print("phone num:",num)

num=re.sub(r'\D',"",phone)
print("phone Num:",num)


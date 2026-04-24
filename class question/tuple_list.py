t=(20,12,30,49,50)

print("origina",t)

l=list(t)
print("converted list:",l)

l.append(50)
print("Modified list:",l)

t=tuple(l)
print("final tuple:",t)

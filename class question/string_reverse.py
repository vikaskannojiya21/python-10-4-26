words = ["vikas", "ab"]

rev_list = []

for word in words:
    rev = ""

    for ch in word:
        rev = ch + rev

    rev_list.append(rev)

print(rev_list)

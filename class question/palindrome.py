words=["madam","hello","level","abc"]

for word in words:
    rev=""

    for ch in word:
        rev=ch+rev
    if word == rev:
        print(word,"is palindrome")
    else:
        print(word,"is not palimdrome")

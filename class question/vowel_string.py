text = input("Enter a string: ")

vowels = 0
consonants = 0

for char in text:
    #if char.isalpha():   # only letters
        if char in "AEIOUaeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

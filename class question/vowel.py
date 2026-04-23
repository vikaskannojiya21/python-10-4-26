words = ["hello", "world", "python"]

vowels = "aeiouAEIOU"

for word in words:
    vowel_list = []

    for ch in word:
        if ch in vowels:
            vowel_list.append(ch)

    print(vowel_list)
  

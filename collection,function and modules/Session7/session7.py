#1
print("*"*50)
text = input("Enter a string: ")

char_count = {}

for ch in text:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)
print("*"*50)
#2
review = """
Zomato is a good food delivery app.
Zomato provides fast delivery and good food.
"""

review = review.lower()

words = review.replace(".", "").split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print("*"*50)
#3
def word_freq_dict(text):
    words = text.lower().replace(",", "").replace(".", "").split()

    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
print(word_freq_dict(text))
print("*"*50)

#4
text = "Virat scored 100 and Rohit scored 80 in the IPL match"

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

words = text.lower().split()

result = {}

for word in words:
    if word not in stopwords:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

print(result)
print("*"*50)

#5
def char_count_dict(text):
    result = {}

    for ch in text:
        if ch != " ":
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1

    return result


text = "Python"

count = char_count_dict(text)

for ch in sorted(count):
    print(ch, count[ch])

















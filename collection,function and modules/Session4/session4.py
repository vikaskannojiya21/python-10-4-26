# 1. Create tuple
my_profile = ("Vikas", 18, "Pizza", True)

print(my_profile)


# 2. Tuple slicing
playlist = ('Shape of You', 'Blinding Lights', 'Believer', 'Senorita', 'Levitating')

print(playlist[1:4])


# 3. Tuple -> List -> Tuple
order = ('Burger', 'Fries', 'Coke')

order = list(order)

order.append("Ice Cream")

order = tuple(order)

print(order)


# 4. Mixed tuple
insta_post = (101, "vikas", 500, ["python", "coding"], True)

print(insta_post)

for item in insta_post:
    print(type(item))


# 5. WhatsApp call durations
calls = (12, 5, 0, 20, 7, 3, 15)

calls = list(calls)

new_calls = []

for c in calls:
    if c >= 5:
        new_calls.append(c)

calls = tuple(new_calls)

print(calls)

import math
import random

# 1. Square root
print("Square Roots:")
print(math.sqrt(16))
print(math.sqrt(49))
print(math.sqrt(81))


# 2. Price rounder using ceil()
prices = [199.1, 349.8, 599.3]

print("\nRounded Prices:")
for price in prices:
    print(math.ceil(price))


# 3. Zomato bill calculator using floor()
bill = 850

discount = bill * 0.10
final_bill = bill - discount

print("\nFinal Bill:")
print(math.floor(final_bill))


# 4. Dice roll
dice = random.randint(1, 6)

print("\nDice Result:")
print(dice)


# 5. Spotify playlist shuffle
songs = [
    "Kesariya",
    "Believer",
    "Shape of You",
    "Faded",
    "Thunder",
    "Perfect",
    "Closer",
    "Havana"
]

playlist = random.sample(songs, 3)

print("\nToday's Playlist:")
print(playlist)

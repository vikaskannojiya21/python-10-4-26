# 1
playlist = ["Believer", "Thunder", "Faded", "Perfect", "Senorita"]

for i in range(5):
    print(i + 1, "-", playlist[i])

# 2
foods = ["Pizza", "Burger", "Dosa", "Pasta", "Fries"]

for i in range(3):
    print(foods[i])

# 3
prices = [299, 499, 150, 1200, 350]

total = 0
for p in prices:
    total = total + p

print("Total =", total)

# 4
unread_counts = [2, 0, 15, 120, 5]

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)

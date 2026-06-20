
# 1. Even numbers between 10 and 50

even = [i for i in range(10, 51) if i % 2 == 0]

print("Even Numbers:")
print(even)


# 2. Playlist durations greater than 200

songs = [[210, 180, 240], [150, 200], [300, 120, 90]]

result = [x for a in songs for x in a if x > 200]

print("Song Durations:")
print(result)


# 3. Products with price above 1000

names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

products = [(n, p) for n, p in zip(names, prices) if p > 1000]

print("Products:")
print(products)


# 4. Ratings above 4

ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

high = [x for row in ratings for x in row if x > 4]

print("High Ratings:")
print(high)

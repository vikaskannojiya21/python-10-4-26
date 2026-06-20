#1
scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded = []

for s in scores:
    rounded.append(round(s))

print(scores)
print(rounded)
#2
ratings = [4.2, 3.8, 4.9, 2.5, 4.0]

ratings = sorted(ratings, reverse=True)

print(ratings)
#3
products = ["Mobile", "Laptop", "Camera", "Watch"]

products.sort()

print(products)
#4
restaurants = ["Burger Hub", "Pizza Point", "Sushi House"]

times = [30, 25, 40]

for r, t in zip(restaurants, times):
    print(r, "-", t, "min")
#5
def video_data(titles, views):
    result = []

    for t, v in zip(titles, views):
        result.append((t, round(v, -3)))

    return result


titles = ["Python", "Django", "Java"]
views = [12500, 23500, 45600]

print(video_data(titles, views))

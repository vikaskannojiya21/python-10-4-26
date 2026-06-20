#1
products = ["Mobile", "Laptop", "Watch"]
prices = [15000, 50000, 2000]

product_dict = dict(zip(products, prices))

print(product_dict)
#2
usernames = ["raj", "ananya", "vikas"]
followers = [500, 1000, 300]

users = {}

for i in range(len(usernames)):
    users[usernames[i]] = followers[i]

print(users)
#3
teams = ["CSK", "MI", "GT", "RCB"]
points = [12, 8, 15, 10]

team_points = dict(zip(teams, points))

for team, point in team_points.items():
    if point > 10:
        print(team, point)
#4
titles = ["Avatar", "Interstellar", "Titanic"]
genres = ["Sci-Fi", "Adventure", "Romance"]
ratings = [8.5, 9.0, 7.9]

movies = []

for t, g, r in zip(titles, genres, ratings):
    movies.append({
        "title": t,
        "genre": g,
        "rating": r
    })

print(movies)

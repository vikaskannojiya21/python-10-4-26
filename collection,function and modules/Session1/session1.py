# 1. Create list
fav_items = ["Believer", 17, 3.5, True]

# 2. Update values
fav_items[0] = "Thunder"
fav_items[1] = fav_items[1] + 1

# 3. Remove mobile data usage
fav_items.pop(2)

print(fav_items)

# 4. Weekend plan
weekend_plan = ["Study", "Movie", "Cricket", 2, "Shopping"]

removed = weekend_plan.pop()

print("Removed:", removed)
print(weekend_plan)

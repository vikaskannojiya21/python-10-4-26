orders = {}


def add_order(id, restaurant, items, total):
    orders[id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }


def update_total(id, new_total):
    orders[id]["total"] = new_total


add_order(1, "Pizza Point", ["Pizza", "Coke"], 500)

update_total(1, 600)

print(orders)

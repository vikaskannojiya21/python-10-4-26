#1
def calculate_total(price, quantity):
    return price * quantity


result = calculate_total(120, 3)

print(result)
print("*"*50)
#2
def format_username(username, prefix="user_"):
    return prefix + username


print(format_username("vikas"))

print(format_username("vikas", "admin_"))
print("*"*50)
#3
def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat:", seat_type)
    print("Snacks:", snacks)
    print()


book_movie_ticket("Jawan")
book_movie_ticket(movie_name="Pathaan", seat_type="VIP", snacks="Popcorn")
book_movie_ticket("Jawan", snacks="Cold Drink", seat_type="Premium")
print("*"*50)
#4
def apply_coupon(amount, coupon_code=None):

    if coupon_code == "SAVE10":
        amount = amount - (amount * 0.10)

    return amount
print(apply_coupon(1000))
print(apply_coupon(1000, "SAVE10"))










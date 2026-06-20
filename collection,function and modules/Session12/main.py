from musicplayer import play_song
from foodorder import get_menu,place_order
from shoppingcart import add_to_cart
from instahelpers import format_likes
from ticketbooking import search_event, book_ticket


play_song()
menu=get_menu()
print(menu)
place_order("Pizza")
add_to_cart("Mobile")
print(format_likes(1200))
print(format_likes(1500000))
print(format_likes(500))
search_event("Concert")
book_ticket("Concert")


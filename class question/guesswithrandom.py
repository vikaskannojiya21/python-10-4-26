import random
num=random.randint(1,20)

while True:
    guess=int(input("Guess A number between 1 to 20:"))
    if guess==num:
        print("You guessed A correct number")
        break
    elif guess>num:
        print("You guessed A greater number")
    elif guess<num:
        print("you guessed A smaller number")

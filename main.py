from data import data
from art import logo
from art import vs
import random

print(logo)

a = eval(str(random.choice(list(data))))
follower_a = a.get('follower_count')

b = eval(str(random.choice(list(data))))
follower_b = b.get('follower_count')

x = " "

player_score = 0

while follower_a != follower_b or follower_b != follower_a is not True:

    (f"Compare A: {b.get('name')}, a {b.get('description')}, from {b.get('country')}")
    (follower_b)

    b1_name = b.get('name')
    b1_description = b.get('description')
    b1_from = b.get('country')
    b1_follower = follower_b

    print(x)
    print(x)
    print(f"Compare A: {b1_name}, a {b1_description}, from {b1_from}")

    print(vs)

    b = eval(str(random.choice(list(data))))
    follower_b = b.get('follower_count')
    print(f"Against B: {b.get('name')}, a {b.get('description')}, from {b.get('country')}")

    answer = input("Type 'A' or 'B', Who has more followers? ").lower()

    player_score = player_score + 1
    if answer == "a":
        if b1_follower > follower_b:
            print("You got it! Keep playing.")
            print(f"Your current score is {player_score}")
        elif follower_b == b1_follower:
            player_score = player_score - 1
            print("It's a draw, keep playing.")
        elif follower_b > b1_follower:
            player_score = player_score - 1
            print("You Lose, Sorry.")
            print(f"Your final score is {player_score}")
            break
    elif answer == "b":
        if follower_b > b1_follower:
            print("You got it! Keep playing.")
            print(f"Your current score is {player_score}")
        elif follower_b == b1_follower:
            player_score = player_score - 1
            print("It's a draw, keep playing.")
        elif b1_follower > follower_b:
            player_score = player_score - 1
            print("You Lose, Sorry.")
            print(f"Your final score is {player_score}")
            break
    else:
        print("Invalid input, please restart and try again")
        break

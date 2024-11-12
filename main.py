import art
import game_data
import random
score = 0
print(art.logo)


def game(current_score):
    person_a = random.randint(0, 50)
    name = game_data.data[person_a]["name"]
    description = game_data.data[person_a]["description"]
    country = game_data.data[person_a]["country"]
    follower_count_a = game_data.data[person_a]["follower_count"]
    print(f"Compare A: {name}, a {description}, from {country} ")
    print(art.vs)
    person_b = random.randint(0, 50)
    name = game_data.data[person_b]["name"]
    description = game_data.data[person_b]["description"]
    country = game_data.data[person_b]["country"]
    follower_count_b = game_data.data[person_b]["follower_count"]
    print(f"against B: {name}, a {description}, from {country}")
    choose = input("Who has more followers? Type 'A' or 'B' : ").lower()
    if follower_count_a == follower_count_b:
        person_b = random.randrange(0,50)
    elif choose == "a" and follower_count_a > follower_count_b:
        current_score += 1
        person_b = person_a
        print("\n"*20)
        print(art.logo)
        print(f"You're right! Current score : {current_score}")
        game(current_score)
    elif choose == "b" and follower_count_b > follower_count_a:
        current_score += 1
        person_b = person_a
        print("\n" * 20)
        print(art.logo)
        print(f"You're right! Current score : {current_score}")
        game(current_score)
    else:
        print(f"Sorry, that's wrong. Final score : {current_score}")


game(score)

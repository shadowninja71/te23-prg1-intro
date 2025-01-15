from random import randint
player_one_score = 0
player_two_score = 0
while player_one_score < 5 or player_two_score < 5:
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        player_one_score += 1
        print(f"spelare ett van och har nu {player_one_score} poäng")

    elif player_two_roll > player_one_roll:
        player_two_score += 1
        print(f"spelare två van och har nu {player_two_score} poäng")
    else:
        print(f"det vart oavgjort och ingen fick poäng, rundan spelas om")
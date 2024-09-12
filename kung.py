from random import randint
play_game = "j"
player_one_score = 0
player_two_score = 0
while play_game.upper() == "J":
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"Spelare ett vinner med tärningskastet: {player_one_roll}")
        player_one_score += 1
    elif player_two_roll > player_one_roll:
        print(f"Spelare två vinner med tärningskastet: {player_two_roll}")
        player_two_score += 1
    else:
        print(f"ingen spelare vinner, det är oavgjort med tärningstalet: {player_one_roll}")
    if player_one_score == 1000:
        print(f"spelare ett van med {player_one_score} över {player_two_score}")
        play_game = "n"
    elif player_two_score == 1000:
        print(f"spelare två van med {player_two_score} över {player_one_score}")
        play_game = "n"
from random import randint
play_game = "j"
while play_game.upper() == "J":
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print(f"Spelare ett vinner med tärningskastet: {player_one_roll}")
    elif player_two_roll > player_one_roll:
        print(f"Spelare två vinner med tärningskastet: {player_two_roll}")
    else:
        print(f"ingen spelare vinner, det är oavgjort med tärningstalet: {player_one_roll}")
    play_game = input("vill du spela igen {J/N}: ")
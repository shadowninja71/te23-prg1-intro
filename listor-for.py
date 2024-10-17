print("välkommen till det bästa programmet, där du sparar spel")
run = True
games = ["minecraft", "terraria", "beat_saber"]
while run:
    choice = input("vad vill du göra \n[1] skriv ut\n[2] lägg till spel\n[3] avsluta\n")
    if choice == "1":
        print("spelen är:")
        for game in games:
            print(game)
    elif choice =="2":
        game = input("skriv in ett nyt spel:")
        games.append(game)
    elif choice == "3":
        run = False
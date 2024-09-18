#gissa talet
import random
största = int (input("det största möjliga talet:"))
försök = int (input("hur många försök får man:"))
tal = random.randint (1, största)
for i in  range(försök) :
    gissning = int (input("gissa talet?"))
    if gissning < tal:
        print("för liten")
    elif gissning > tal:
        print("för stort")
    else:
        print("rätt gissat")
else:
    print("inga fler försök")
    print("talet var", tal)
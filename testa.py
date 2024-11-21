
def kollaTal():
    while True:
        try:
            tal = input("skriv in ett tal:")
            talRetur = int(tal)
            return talRetur
        except:
            print("Tal är ej gilltigt,är du dum eller, prova igen!")

tal1 = 18
tal2 = kollaTal()

if tal2 > tal1 :
    print("ditt tal var större, dit tal:",tal2)

else:
    print("datorns tal är störe,datorns tal:",tal1)
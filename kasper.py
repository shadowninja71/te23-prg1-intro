count = 0
svar = "ja"
while svar == "ja":
    count += 1
    if count % 7 == 0:
        print("klapp")
    elif count % 11 == 0:
        print("klapp")
    else:
        print(count)
    svar = input("vil du forstäta:")
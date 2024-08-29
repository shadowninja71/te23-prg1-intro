print("hej och välkommen till mitt program")
namn = input("vad heter du, skriv dit namn: ")

print(f"hej {namn}! vad kul att du är här!")

print("jag undrar hur gammal du är")

user_age = input("skriv din ålder i år: ")

print(f"tack, vad fint att du är {user_age} år ung.")

user_age_converted = int(user_age)

if user_age_converted >= 15:
    print("du får köra mopped. ")
else:
    print("😡")
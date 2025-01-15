user_input = input("skriv ett ord att översätta till rövarspråket: ")
translation = ""
vowels = ["a," "o", "u", "e", "i", "y", "å", "ä", "ö"]

for letter in user_input:
    if letter.lower() in vowels:
        translation += letter
    else:
        translation += letter + "o" + letter

print(translation)
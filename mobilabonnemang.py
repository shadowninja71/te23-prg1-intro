tid = input("hur mycket tror du att du kommer ringa värje månad:")

tid = int(tid)

if tid <= 33:
    print("du borde skaffa ett kontant abonnemang")
elif tid > 33 and tid <= 66:
    print("du borde skaffa ett normal abonnemang")
else:
    print("du borde skaffa ett plus abonnemang")
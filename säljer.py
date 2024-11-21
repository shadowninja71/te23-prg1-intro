äpplen_sålda = 1    
päron_sålda = 1

äpple = 7
päron = 13

axel = äpplen_sålda * äpple
petra = päron_sålda * päron

if axel < petra:
    print("petra har skänat mer pengar")
elif axel > petra:
    print("axel har skänat mer pengar")
else:
    print("dom båda har skänat lika mycket pengar")
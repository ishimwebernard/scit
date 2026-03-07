i = 1
conditioner = True

while conditioner:
    passednumbers = 0
    
    for j in range(1,21):
        if i % j == 0:
            passednumbers += 1
    
    if passednumbers == 20:
        conditioner = False
        print(i, passednumbers)
    i += 1
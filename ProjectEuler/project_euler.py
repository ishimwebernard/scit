def cancelsimilaritems(numerator, denominator):
    arnum = list(str(numerator))
    ardeno = list(str(denominator))

    arnum_copy = list(arnum)
    ardeno_copy = list(ardeno)

    for i in range(0, 2):
        if arnum[i] in ardeno and int(arnum[i]) != 0:
            try:
                arnum_copy.remove(arnum[i])
                ardeno_copy.remove(arnum[i])
            except ValueError:
                break
        
    num = "".join(arnum_copy)
    deno = "".join(ardeno_copy)
    
    if num and deno:
        intnum = int(num)
        intdeno = int(deno)
        if intnum != 0 and intdeno != 0 and len(list(str(intnum))) < 2 and len(list(str(intdeno))) < 2  and intnum/intdeno == numerator/denominator:
            print(intnum, "/", intdeno)
  

for i in range(10,99, 1):
    for j in range(i,99,1):
        cancelsimilaritems(i,j)

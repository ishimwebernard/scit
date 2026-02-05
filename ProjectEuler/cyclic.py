def shape(k,n):
    strlist = []
    if k == 3:
        for i in range(1,n,1):
            if hastwosimilardigits((i*(i+1)/2)):
                strlist.append((i*(i+1)/2))
    elif k == 4:
        for i in range(1,n,1):
            if hastwosimilardigits((i**2)):
                strlist.append(i**2)
    elif k == 5:
        for i in range(1,n,1):
            if hastwosimilardigits(i*(3*i-1)/2):
                strlist.append(i*(3*i-1)/2)
    elif k == 6:
        for i in range(1,n,1):
            if hastwosimilardigits(i*(2*i-1)):
                strlist.append(i*(2*i-1))
    elif k == 7:
        for i in range(1,n,1):
            if hastwosimilardigits(i*(5*i-3)/2):
                strlist.append(i*(5*i-3)/2)
    elif k == 8:
        for i in range(1,n,1):
            if hastwosimilardigits(i*(3*i-2)):
                strlist.append(i*(3*i-2))
    if int(len(strlist)) == 4:
        print(strlist)

def hastwosimilardigits(number):
    arrnumber = list(str(number))
    try:
        if arrnumber.index('.'):
            del arrnumber[arrnumber.index('.'):arrnumber.index('.')+2]
    except ValueError:
        print("Value not found")

    print(arrnumber)
    retval = 0
    if len(arrnumber) == 4:
        for i in range(0, 4, 1):
            j=0
            for j in range(i+1,4,1):
                if int(arrnumber[i]) == int(arrnumber[j]):
                    retval = 1
    return retval

shape(3,200)
#shape(4,100)
    







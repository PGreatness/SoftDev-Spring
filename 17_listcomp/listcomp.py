def forComp():
    ret = []
    for x in range(5):
        ret.append(str(2 * x) + str(2 * x))
    return ret

def listComp():
    return [str(2 * x) + str(2 * x) for x in range(5)]

print(forComp())
print(listComp())

def forComp2():
    ret = []
    for x in range(5):
        ret.append(x * 10 + 7)
    return ret
def listComp2():
    return [x*10+7 for x in range(5)]

def forComp3():
    ret = []
    for x in range(3):
        ret.append(0)
    for x in range(3):
        ret.append(x)
    for x in range(3):
        ret.append(x*2)
    return ret


def listComp3():
    arr1 = [0 for x in range(3)]
    arr2 = [x for x in range(3)]
    arr3 = [2 * x for x in range(3)]
    return arr1 + arr2 + arr3

def forComp4():
    ret = []
    for x in range(2, 100):
        for a in range(2, x):
            if (x % a == 0):
                ret.append(x)
                break
    return ret

def listComp4():
    return [x if x % a == 0 for x in range(2, 100) for a in range(2, x) ]

print(forComp4())
print(listComp3())
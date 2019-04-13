"""
Comprehende (Roster: Ahnaf Hasan && Kendrick Liang)
SoftDev2 pd06
K #17: PPFTLCW
2019-04-12
"""

def forComp():
    ret = []
    for x in range(5):
        ret.append(str(2 * x) + str(2 * x))
    return ret

def listComp():
    return [str(2 * x) + str(2 * x) for x in range(5)]

print("\n============ Return ['00', '22', '44', '66', '88'] ===============\n")
print("For: " + str(forComp()))
print("Comp: " + str(listComp()))

def forComp2():
    ret = []
    for x in range(5):
        ret.append(x * 10 + 7)
    return ret

def listComp2():
    return [x*10+7 for x in range(5)]

print("\n============ Return [7, 17, 27, 37, 47] ===============\n")
print("For: " + str(forComp2()))
print("Comp: " + str(listComp2()))

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


print("\n============ Return [0, 0, 0, 0, 1, 2, 0, 2, 4] ===============\n")
print("For: " + str(forComp3()))
print("Comp: " + str(listComp3()))

def forComp4():
    ret = []
    for x in range(2, 100):
        for a in range(2, x):
            if (x % a == 0):
                ret.append(x)
                break
    return ret

def listComp4():
    a = [ x for x in range(2, 100) for a in range(2, x) if x % a == 0 ]
    a = list(dict.fromkeys(a)) # turn to dict, can't have dupes. then turn to list
    return a

print("\n============ Return Composite numbers from [0, 100] ===============\n")
print("For: " + str(forComp4()))
print("Comp: " + str(listComp4()))

def forComp5():
    ret = []
    for x in range(2, 100):
        isPrime = True
        for a in range(2, x):
            if x % a == 0:
                isPrime = False
                break
        if isPrime:
            ret.append(x)
    return ret

def listComp5():
    composites = listComp4()
    return [ x for x in range(2, 100) if x not in composites ]

print("\n============ Return Prime numbers from [0, 100] ===============\n")
print("For: " + str(forComp5()))
print("Comp: " + str(listComp5()))

def forComp6(num):
    ret = []
    if num < 2:
        return 1
    for x in range(2, num):
        if num % x == 0:
            ret.append(x)
    return ret

def listComp6(num):
    if num < 2:
        return 1
    return [ x for x in range(2, num) if num % x == 0 ]

num = 100
print(f"\n============ Return All divisors of a number (case: {num}) ===============\n")
print("For: " + str(forComp6(num)))
print("Comp: " + str(listComp6(num)))

def forComp7(matrix):
    ret = []
    for col in range(len(matrix) + 1):
        tmp_matrix = []
        for row in matrix:
            tmp_matrix.append(row[col])
        ret.append(tmp_matrix)
    return ret

def listComp7(matrix):
    return [[row[col] for row in matrix ] for col in range(len(matrix) + 1)]

mat = [
    [3, 4, 10, 23, 1],
    [5, 6, 12, 10, 51],
    [1, 6, 9, 3, 1],
    [12, 5, 1, 8, 9001]
]
print(f"\n============ Transpose Matrix {mat} ===============\n")
print("For: " + str(forComp7(mat)))
print("Comp: " + str(listComp7(mat)))
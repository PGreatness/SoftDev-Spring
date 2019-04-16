def union(a, b):
    return [x for x in a] + [x for x in b if x not in a]

print(union([1, 3, 4, 5], [4, 3, 7, 9]))

def intersection(a, b):
    return [x for x in a if x in b]

print(intersection([1, 2, 3], [2, 3, 4]))

def set_difference(a, b):
    return [x for x in a if x not in b]

print(set_difference([1, 2, 3], [2, 3, 4]))
print(set_difference([2, 3, 4], [1, 2, 3]))

def sym_diff(a, b):
    return [x for x in a if x not in b] + [x for x in b if x not in a]

print(sym_diff([1, 2, 3], [2, 3, 4]))

def cart_prod(a, b):
    return [(x, y) for x in a for y in b]

print(cart_prod([1, 2], ["red", "white"]))

def subsets(a):
    return [x for x in a if type(x) is list]

print(subsets([1, 3, 5, [4, 5, 1], 3, [5, 2]]))
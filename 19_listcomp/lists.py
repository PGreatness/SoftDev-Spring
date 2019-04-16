"""
Listless (Roster: Ahnaf Hasan && Kendrick Liang)
SoftDev2 pd06
K #19:
2019-04-16
"""

""" Returns the union of a and b, both of which are lists. """
def union(a, b):
    return [x for x in a] + [x for x in b if x not in a]

print(union([1, 3, 4, 5], [4, 3, 7, 9]))

""" Returns the intersection of a and b, both of which are lists. """
def intersection(a, b):
    return [x for x in a if x in b]

print(intersection([1, 2, 3], [2, 3, 4]))

""" Returns the set difference of a and b, both of which are lists. The
    set difference is the all values of a that are not in b. """
def set_difference(a, b):
    return [x for x in a if x not in b]

print(set_difference([1, 2, 3], [2, 3, 4]))
print(set_difference([2, 3, 4], [1, 2, 3]))

""" Returns the symbolic difference of a and b, both of which are lists.
    The symbolic difference are all values in a that aren't in b and all
    values of b that aren't in a. """
def sym_diff(a, b):
    return [x for x in a if x not in b] + [x for x in b if x not in a]

print(sym_diff([1, 2, 3], [2, 3, 4]))

""" Returns the cartesian product of a and b, both of which are lists.
    Returns all possible combinations of a and b. """
def cart_prod(a, b):
    return [(x, y) for x in a for y in b]

print(cart_prod([1, 2], ["red", "white"]))

""" Returns all the subsets of a. """
def subsets(a):
    return [x for x in a if type(x) is list]

print(subsets([1, 3, 5, [4, 5, 1], 3, [5, 2]]))
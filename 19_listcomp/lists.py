"""
Listless (Roster: Ahnaf Hasan && Kendrick Liang)
SoftDev2 pd06
K #19:
2019-04-16
"""

""" Returns the union of a and b, both of which are lists. """
def union(a, b):
    return [x for x in a] + [x for x in b if x not in a]

first = [1, 3, 4, 5]
second = [4, 3, 7, 9]
print(f"============== Union of {first} and {second} =================\n")
print(f"The union of {first} and {second}:\n {union(first, second)}")

""" Returns the intersection of a and b, both of which are lists. """
def intersection(a, b):
    return [x for x in a if x in b]

print(f"============== Intersection of {first} and {second} ================\n")
print(f"The intersection of {first} and {second}:\n {intersection(first, second)}")

""" Returns the set difference of a and b, both of which are lists. The
    set difference is the all values of a that are not in b. """
def set_difference(a, b):
    return [x for x in a if x not in b]

print(f"=============== Set Difference of {first} and {second} ================\n")
print(f"The set difference of {first} and {second}:\n {set_difference(first, second)}")
print(f"The set difference of {second} and {first}:\n {set_difference(second, first)}")

""" Returns the symbolic difference of a and b, both of which are lists.
    The symbolic difference are all values in a that aren't in b and all
    values of b that aren't in a. """
def sym_diff(a, b):
    return [x for x in a if x not in b] + [x for x in b if x not in a]

print(f"============= Symbolic Difference of {first} and {second} ================\n")
print(f"Sybolic difference of {first} and {second}:\n {sym_diff(first, second)}")

""" Returns the cartesian product of a and b, both of which are lists.
    Returns all possible combinations of a and b. """
def cart_prod(a, b):
    return [(x, y) for x in a for y in b]

print(f"============ Cartesian Product of {first} and {second} =============\n")
this = [1, 2, 3, 5]
that = ['red', 'white', 'blue', 'green']
print(f"Cartesian Product of {this} and {that}:\n {cart_prod(this, that)}")

""" Returns all the subsets of a. """
def subsets(a):
    return [x for x in a if type(x) is list]

sub = [1, 3, 5, [4, 5, 1], 3, [5, 2]]
print(f"============ Subsets of {sub} ===============\n")
print(f"Subsets of {sub}:\n {subsets(sub)}")
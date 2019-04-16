"""
Ahnaf Hasan
SoftDev2 pd06
K #18:
2019-04-15
"""
def triples(end_range=2):
    """
    The Pythagorean Theorem: a^2 + b^2 == c^2
    They are all ints for range so this has to
    produce Pythagorean Triples
    """
    return [(a, b, c) for a in range(2, end_range) for b in range(end_range) for c in range(end_range) if a * a + b * b == c * c and a is not 0 and b is not 0 and c is not 0]

def quickHelp(data, start, dupes):
    """
    Helper function. Seperates into two parts and recursively goes through each
    data -- the data in list form
    start -- pivot
    dupes -- number of duplicate items in data
    """
    if len(data) <= dupes: # making the largest duplicate count allows this to handle duplicates to avoid infinite recursion
        return data
    else:
        print(data)
        return quickHelp([x for x in data if x < start], min(data), dupes) + quickHelp([x for x in data if x >= start], max(data), dupes)

def quicksort(data=[]):
    """
    Quicksort function. Finds number of duplicate items first and stores largest occurrence. Uses helper quickHelp(int list, int, int)
    """
    dupes = [(x, data.count(x)) for x in data if data.count(x) > 1] # all duplicate items in the list
    count = 1 # largest amount of duplicate items
    for x in dupes:
        if x[1] > count:
            count = x[1]
    return quickHelp(data, data[0], count)


print(f"\n==================== Testing triples =======================\n")
r = 100
print(f"The range is 0 to {r}:\n{triples(r)}")

print(f"\n=================== Testing Quicksort ======================\n")
data = [7 , 1, 5, 2, 0, 8, -1]
print(f"Testing data {data} by quicksort: {quicksort(data)}")
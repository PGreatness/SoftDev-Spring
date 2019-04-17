from functools import reduce
from collections import Counter

def singleWord(file=''):
    f = open(file, 'r', encoding='utf-8')
    print("here")
    lines = ' '.join([line for line in f])
    print("2")
    words = [line.strip() for line in lines.split(' ')]
    print(3)
    print(len(words))
    counts = Counter(words)
    print(4)
    return counts.most_common(1)[0]

most_common = singleWord('./golden.txt')
print(f"The most common word in the text is \"{most_common[0]}\" with a count of: {most_common[1]}")
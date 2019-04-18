"""
Listless (Roster: Ahnaf Hasan && Kendrick Liang)
SoftDev2 pd06
K #19: Reductio ad Absurdum
2019-04-16
"""

from functools import reduce
from collections import Counter
from string import punctuation

text_file = 'golden.txt'

""" def searchFor(file='', word=''):
    f = open(file, 'r', encoding='utf-8')
    lines = ' '.join([line for line in f])
    words = [line.strip() for line in lines.split(' ')]
    counts = Counter(words)
    return (word, counts[word]) """

""" def groupWords(file='', words=''):
    f = open(file, 'r', encoding='utf-8')
    lines = [line.strip() for line in f]
    occurrences = [x for x in lines if words.lower() in x.lower()]
    return (words, len(occurrences))
 """

def singleWord(file=''):
    f = open(file, 'r', encoding='utf-8')
    lines = ' '.join([line for line in f])
    words = [line.strip() for line in lines.split(' ')]
    counts = Counter(words)
    return counts.most_common(1)[0]

def reduceSearchFor(file='', word=''):
    f = open(file, 'r', encoding='utf-8')
    lines = ' '.join([line for line in f])
    words = [line.strip() for line in lines.split(' ')]
    return (word, reduce(lambda x,y: x + 1 if word.lower() == y.lower() else x, words, 0))

def reducedGroup(file='', words=''):
    f = open(file, 'r', encoding='utf-8')
    lines = [line.strip() for line in f]
    return (words, reduce(lambda x,y: x + 1 if words.lower() in y.lower() else x, lines, 0))

def reducedCommon(file=''):
    f = open(file, 'r', encoding='utf-8')
    lines = ' '.join([line for line in f])
    words = [line.strip() for line in lines.split(' ')]
    largest = ('', 0)
    done = []
    for item in words:
        if item.lower() in done:
            continue
        done.append(item.lower())
        s = reduce(lambda x,y: x + 1 if y.lower() == item.lower() else x, words, 0)
        print(item)
        if s > largest[1]:
            largest = (item, s)
            print(largest)
    return largest

most_common = singleWord(text_file)
print(f"The most common word in the text is \"{most_common[0]}\" with a count of: {most_common[1]}")

""" groups = groupWords(text_file, 'Information about')
print(f"The search for {groups[0]} returned: {groups[1]}") """

""" searched = searchFor(text_file, 'common')
print(f"Your search for \"{searched[0]}\" yielded {searched[1]} results.") """

red= reduceSearchFor(text_file, 'common')
print(f"Your reduced search for \"{red[0]}\" returned {red[1]} results.")

rg = reducedGroup(text_file, 'Information about')
print(f"The search for \"{rg[0]}\" returned: {rg[1]}")

# Terrible timing, takes 5 mins to find
com = reducedCommon(text_file)
print(f"The most common word in the text is \"{com[0]} with a count of: {com[1]}")

#jacard  - comparing words

import collections

def jaccard(a, b):
    c = a.intersection(b)
    print("this is intersection", c)
    d=a.union(b)
    print("this is union", d)
    _a = collections.Counter(a)
    _b = collections.Counter(b)
    c = (_a - _b) + (_b - _a)
    print("c", c)
    n = sum(c.values())
    print(_a)
    print(_b)
    print("_a and _b")
    print ("n", n)
    return float(len(c)) / (len(a) + len(b) - len(c))

list1 = ['dog', 'cat', 'rat', 'gerbil', 'rat', 'rat']
list2 = ['dog', 'cat', 'mouse', 'cow', 'horse', 'rat']

words1 = set(list1)
words2 = set(list2)
print("words1:  ", words1)
print("words2:  ", words2)
z = jaccard(words1, words2)
print("this is z", z*100)

from typing import Counter

a = 'aabb'


def slove(a):
    lol = Counter(a)
    index = -1
    for i, x in lol.items():
        if x <= 1:
            index = a.index(i)
            break
    return index

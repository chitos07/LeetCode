from typing import Counter


def isAnagram(s, t) -> bool:
    return Counter(s) == Counter(t)

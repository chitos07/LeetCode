from typing import Counter


def slove(ransomNote, magazine):
    return not Counter(ransomNote) - Counter(magazine)

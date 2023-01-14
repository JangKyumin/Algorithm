from typing import Counter

def solution(array, n):
    group = Counter(array)
    return group.get(n) if group.get(n) else 0
import collections

def solution(numbers, direction):
    x  = collections.deque(numbers)
    if direction == "right":
        x.rotate(1)
    else:
        x.rotate(-1)
    return list(x)
def solution(sides):
    sides.sort(reverse = True)
    max_val = max(sides)
    
    if max_val >= sum(sides[1:3]):
        return 2
    else:
        return 1
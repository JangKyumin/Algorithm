def solution(sides):
    answer = 0
    side_max = max(sides)
    side_min = min(sides)
    side_long = side_min + side_max
    
    if (side_min == 1 and side_max == 2):
        return 1
    
    for i in range(side_max - side_min + 1, side_max + 1):
        if side_min + i > side_max:
            answer += 1
            
    for i in range(side_max + 1, side_long):
        answer += 1
        
    return answer
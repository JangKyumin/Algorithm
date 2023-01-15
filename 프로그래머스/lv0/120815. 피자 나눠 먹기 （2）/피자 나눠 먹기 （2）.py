def solution(n):
    result = 1
    while True:
        if (result * 6) % n == 0:
            return result
        else:
            result += 1
        
        
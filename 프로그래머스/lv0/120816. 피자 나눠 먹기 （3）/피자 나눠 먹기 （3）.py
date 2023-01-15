def solution(slice, n):
    result = 1
    
    if n <= slice:
        return result
    else:
        return (n // slice) + 1 if n % slice != 0 else n // slice
    
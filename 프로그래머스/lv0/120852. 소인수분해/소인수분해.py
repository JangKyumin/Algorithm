def solution(n):
    answer = []
    num = 2
    while n > 1:
        if n == 1:
            break
            
        if n % num == 0:
            answer.append(num) if num not in answer else None
            n //= num
        else:
            num += 1
    
    return answer
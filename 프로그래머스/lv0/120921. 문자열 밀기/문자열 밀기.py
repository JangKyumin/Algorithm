def solution(A, B):
    answer = -1
    
    if A == B:
        return 0
    
    for i in range(1, len(A)):
        if A[-i:] + A[:len(A) - i] == B:
            answer = i
            break
            
    return answer
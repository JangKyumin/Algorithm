def solution(array):
    answer = 0
    for i in array:        
        answer += sum([1 for i in str(i) if i == '7'])            
            
    return answer
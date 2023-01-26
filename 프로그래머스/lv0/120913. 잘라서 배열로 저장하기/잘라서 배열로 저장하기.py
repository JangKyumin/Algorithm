def solution(my_str, n):
    answer = []
    for i in range((len(my_str) // n) + 1 if len(my_str) % n else len(my_str) // n):    
        answer.append(my_str[n * i:n * (i + 1)])
    return answer
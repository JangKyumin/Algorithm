def solution(num, total):
    answer = []
    mid = total / num
    val = (num - 1) / 2
    
    for i in range(int(mid - val), int(mid + val) + 1):
        answer.append(i)
    return answer
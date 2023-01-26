def solution(num, k):
    answer = 0
    li = list(str(num))
    if str(k) in li:
        answer = li.index(str(k)) + 1
    else:
        answer = -1
    return answer
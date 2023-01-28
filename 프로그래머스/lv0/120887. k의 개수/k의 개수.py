def solution(i, j, k):
    answer = 0
    for i in range(i, j + 1):
        answer += sum([1 if str(k) == j else 0 for j in str(i)])
    return answer
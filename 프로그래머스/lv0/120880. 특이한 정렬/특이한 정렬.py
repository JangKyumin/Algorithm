def solution(numlist, n):
    answer = []
    group = {}
    for i in numlist:
        ch = n - i if n - i > 0 else -(n - i)
        if ch not in group:
            group[ch] = [i]
        else:
            group[ch].append(i)
            
    for i in sorted(group.items()):
        answer += sorted(i[1], reverse=True)
    return answer
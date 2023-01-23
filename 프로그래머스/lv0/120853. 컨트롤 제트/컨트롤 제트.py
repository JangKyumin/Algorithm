def solution(s):
    answer = 0
    s_l = s.split(' ')
    for i in range(len(s_l)):
        if s_l[i] != "Z":
            if (i + 1) < len(s_l) and s_l[i + 1] != "Z" or i == (len(s_l) - 1):
                answer += int(s_l[i])
    return answer
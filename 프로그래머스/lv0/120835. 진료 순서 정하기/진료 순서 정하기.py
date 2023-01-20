def solution(emergency):
    answer = []
    tmp_emergency = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(tmp_emergency.index(i) + 1)
    return answer
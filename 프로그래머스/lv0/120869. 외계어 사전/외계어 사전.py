def solution(spell, dic):
    answer = 0
    for i in dic:
        if len(set(spell) - set(list(i))) == 0:
            answer = 1
            break
        else:
            answer = 2
    return answer
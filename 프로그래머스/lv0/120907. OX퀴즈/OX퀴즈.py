def solution(quiz):
    answer = []
    for q in quiz:
        if eval(q.replace("=", "==")):
            answer.append("O")
        else:
            answer.append("X")
    return answer
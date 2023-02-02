def solution(score):
    answer = []
    sum_li = [sum(i) / len(i) for i in score]
    rank_li = sorted(sum_li, reverse=True)
    
    for i in sum_li:
        answer.append(rank_li.index(i) + 1)
    return answer
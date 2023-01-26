def solution(rsp):
    gbb = {
        "2": "0", "0": "5", "5": "2"
    }
    answer = ''
    for s in rsp:
        answer += gbb.get(s)
    return answer
def solution(id_pw, db):
    answer = "fail"
    
    if id_pw in db:
        return "login"
    
    for val in db:
        if id_pw[0] in val and id_pw[1] != val[1]:
            answer = "wrong pw"
    return answer
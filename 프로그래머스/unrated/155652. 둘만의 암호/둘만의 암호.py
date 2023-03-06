def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for ch in skip:
        if ch in alpha:
            alpha = alpha.replace(ch, "")
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)]
        answer += change
    
    return answer
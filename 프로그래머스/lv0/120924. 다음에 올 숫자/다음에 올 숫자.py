def solution(common):
    d_c_yn = (common[1] - common[0]) == (common[2] - common[1])    
    dif = common[1] - common[0] if d_c_yn else common[1] // common[0]    
    return common[-1] + dif if d_c_yn else common[-1] * dif
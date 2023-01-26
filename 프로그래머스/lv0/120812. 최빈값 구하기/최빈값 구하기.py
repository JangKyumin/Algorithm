from collections import Counter

def solution(array):
    array_dic = Counter(array)
    most = array_dic.most_common()
    max_val = most[0][1]
    max_key = most[0][0]
    cnt = 0
    
    for key, val in array_dic.items():
        if max_val == val:
            cnt += 1

        if cnt > 1:
            return -1
    return max_key
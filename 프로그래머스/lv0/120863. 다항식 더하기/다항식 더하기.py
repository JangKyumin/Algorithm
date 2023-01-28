def solution(polynomial):
    cnt = 0
    num = 0
    
    for i in polynomial.split():
        if 'x' in i:
            if len(i) > 1:
                i = i.replace('x', '')
                cnt += int(i)
            else:
                cnt += 1
        elif i.isnumeric():
            num += int(i)

    return ("{}x".format(cnt if cnt > 1 else "") if cnt > 0 else "") + (" + " if cnt > 0 and num > 0 else "") + ("{}".format(num) if num > 0 else "")
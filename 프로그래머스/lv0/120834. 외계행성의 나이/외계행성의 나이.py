def solution(age):
    answer = ""
    alphabat = [
        'a','b','c','d','e',
        'f','g','h','i','j',
        'k','l','m','n','o',
        'p','q','r','s','t',
        'u','v','w','x','y','z'
    ]
    for i in str(age):
        answer += alphabat[int(i)]
    return answer
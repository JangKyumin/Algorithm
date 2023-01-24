def solution(cipher, code):
    answer = ''
    cipher_num = len(cipher) // code
    for i in range(1, cipher_num + 1):
        answer += cipher[(i * code) - 1]
    return answer
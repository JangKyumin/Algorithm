# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return True # 소수가 아님
    return False # 소수임

def solution(n):
    answer = 0
    for i in range(0, n + 1):
        if is_prime_number(i):
            print(i)
            answer += 1
    return answer
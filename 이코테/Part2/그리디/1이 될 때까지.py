n, k = map(int, input().split())

ret = 0

""" 단순하게 푸는 답안
# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        ret += 1
    # K로 나누기
    n //= k
    ret += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    ret += 1
    
print(ret)
"""

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    ret += (n - target)
    n = target

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break

    # K로 나누기
    ret += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
ret += (n - 1)
print(ret)

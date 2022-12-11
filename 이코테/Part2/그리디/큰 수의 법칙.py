"""
입력 조건
    첫째 줄에 N(2 <= N <= 1_000), M(1<= M <= 10_000), K(1<= K <= 10_000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    둘째 중에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10_000 이항의 수로 주어진다.
    입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건
    첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

5 8 3
2 4 5 4 6    => 46
"""
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬하기
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)

""" 단순하게 푸는 버전
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
"""

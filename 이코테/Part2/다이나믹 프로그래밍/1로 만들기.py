x = int(input())

# 작은 값을 재사용하기 위해 다이나믹 프로그래밍 값을 가져간다.
dp = [0] * 30_001

# 최소 2는 되야 1이 나오기때문에 2부터 시작하여 값을 저장한다.
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])

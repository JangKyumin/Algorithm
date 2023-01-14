def solution(n):
    dp = [0] * 100_001
    
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567
    
    return dp[n]
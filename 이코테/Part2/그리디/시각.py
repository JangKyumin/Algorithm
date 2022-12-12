"""
0시 0분 0초부터 n시 59분 59초까지 3이 포함되는 횟수를 구하시오.
"""
n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
z = max(m)

for i in range(m.__len__()):
    m[i] = m[i] / z * 100

print(sum(m) / len(m))

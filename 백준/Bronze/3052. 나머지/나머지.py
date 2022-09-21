import sys

n = []

for i in range(10):
    val = int(sys.stdin.readline())
    n.append(val % 42) if val % 42 not in n else None

print(n.__len__())

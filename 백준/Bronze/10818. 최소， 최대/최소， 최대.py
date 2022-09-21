import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

print(f"{min(m)} {max(m)}")

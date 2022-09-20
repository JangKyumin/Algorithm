import sys

n, x = map(int, sys.stdin.readline().split())
num_li = list(map(int, sys.stdin.readline().split()))

print(" ".join([str(i) for i in num_li if x > i] if num_li.__len__() == n else []))

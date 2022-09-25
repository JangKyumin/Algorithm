import sys

# 참조 : https://doctorson0309.tistory.com/376

a, b, c = map(int, sys.stdin.readline().split())

if b >= c:
    print(-1)
else:
    print((a // (c - b)) + 1)

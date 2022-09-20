import sys

count = int(input())

for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(f"Case #{i + 1}: {a} + {b} = {a + b}")

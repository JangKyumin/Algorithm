import sys

n = []

while n.__len__() <= 8:
    n.append(int(sys.stdin.readline()))

print(val := max(n))
print(n.index(val) + 1)

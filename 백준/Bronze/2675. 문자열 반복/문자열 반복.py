t = int(input())

for i in range(t):
    a, b = map(str, input().split())
    print(*[i * int(a) for i in b], sep='')

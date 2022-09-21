n = int(input())

for i in range(n):
    m = list(map(int, input().split()))
    av = sum(m[1:]) / m[0]
    s = 0

    for j in m[1:]:
        s += 1 if j > av else 0

    print('{:.3f}%'.format(round(s / m[0] * 100, 3)))

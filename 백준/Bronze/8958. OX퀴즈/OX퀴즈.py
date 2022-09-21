n = int(input())

for i in range(n):
    a = b = 0
    m = [i for i in input()]

    for j in m:
        b = b + 1 if j == 'O' else 0
        a += b

    print(a)

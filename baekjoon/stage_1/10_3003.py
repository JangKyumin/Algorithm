list = list(map(int, input().split()))
list2 = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(list2[i] - list[i], end=' ')

n = int(input())
h = 0

for i in range(1, n + 1):
    i_li = list(map(int, str(i)))
    if i < 100:
        h += 1
    elif i_li[0] - i_li[1] == i_li[1] - i_li[2]:
        h += 1
    else:
        pass

print(h)

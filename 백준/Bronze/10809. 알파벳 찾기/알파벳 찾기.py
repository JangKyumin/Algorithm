alphabat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
n = [i for i in str(input())]

for i in alphabat:
    index = alphabat.index(i)

    for j in n:
        if i == j:
            alphabat[index] = n.index(i)

    if not str(alphabat[index]).isnumeric():
        alphabat[index] = -1

print(*alphabat, sep=' ')

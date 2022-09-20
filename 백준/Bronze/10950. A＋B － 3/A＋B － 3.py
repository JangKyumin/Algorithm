a = int(input())
li = list()

for i in range(a):
    b, c = map(int, input().split())
    li.append(b + c)

for i in li:
    print(i)

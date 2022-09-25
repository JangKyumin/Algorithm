n = int(input())

val = 1
cnt = 1

while n > val:
    val += 6 * cnt
    cnt += 1

print(cnt)
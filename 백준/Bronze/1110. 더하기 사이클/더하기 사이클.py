n = nn = input().zfill(2)
z = None
cnt = 0

while n != z:
    m = str(int(nn[:1]) + int(nn[1:2])).zfill(2)
    z = nn = nn[1:2] + m[1:2]
    cnt += 1

print(cnt)
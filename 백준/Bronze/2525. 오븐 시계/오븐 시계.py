h, m = map(int, input().split())
mp = int(input())

m += mp
if m >= 60:
    hp = m // 60
    h += 1 * hp
    if h >= 24:
        h -= 24
    m -= 60 * hp

print(f"{h} {m}")

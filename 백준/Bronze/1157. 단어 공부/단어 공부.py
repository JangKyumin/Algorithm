t = input().lower()
k = list(set(t))
c = []

for i in k:
    c.append(t.count(i))

if c.count(max(c)) > 1:
    print("?")
else:
    print(str(k[c.index(max(c))]).upper())

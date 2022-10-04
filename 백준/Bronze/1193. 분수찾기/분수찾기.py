"""
1/1(1)
1/2(2) -> 2/1(3)
3/1(4) -> 2/2(5) -> 1/3(6)
1/4(7) -> 2/3(8) -> 3/2(9) -> 4/1(10)

"""
X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line - X + 1
else:
    a = line - X + 1
    b = X

print(a, '/', b, sep='')
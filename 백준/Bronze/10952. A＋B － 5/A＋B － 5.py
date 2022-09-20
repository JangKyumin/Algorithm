import sys

end = True
while end:
    a, b = map(int, sys.stdin.readline().split())

    if a + b == 0:
        quit()
    
    print(f"{a + b}")

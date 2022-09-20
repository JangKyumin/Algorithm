total_amt = int(input())
count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    total_amt -= a * b

print("Yes") if total_amt == 0 else print("No")

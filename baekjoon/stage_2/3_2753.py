yn = int(input())

if yn % 4 == 0 and (yn % 100 != 0 or yn % 400 == 0):
    print("1")
else:
    print("0")

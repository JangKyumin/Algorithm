nums = list(range(1, 10001))
re_num = set()

for num in nums:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        re_num.add(num)

for re in re_num:
    nums.remove(re)

print(*nums, sep='\n')

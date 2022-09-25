import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(n):
    text = sys.stdin.readline().strip()
    text_s = list(set(text))
    falg_cnt = 0

    for j in text_s:
        if text[text.index(j):text.count(j) + text.index(j)] == j * text.count(j):
            falg_cnt += 1

    cnt += 1 if falg_cnt == len(text_s) else 0

print(cnt)

# 2579 계단 오르기

n = int(input())
score = [0] * (n + 1)
for i in range(1, n + 1):
    score[i] = int(input())
d = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        d[i] = score[i]
    elif i == 2:
        d[i] = score[i] + score[i - 1]
    elif i == 3:
        d[i] = max(score[i] + score[i - 2], score[i] + score[i - 1])
    else:
        d[i] = max(d[i - 3] + score[i - 1] + score[i], d[i - 2] + score[i])

print(d[n])

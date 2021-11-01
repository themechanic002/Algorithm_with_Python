# 1912 연속합

n = int(input())
num = list(map(int, input().split()))
max = -1000
sum = 0
for i in range(n):
    sum += num[i]
    if max < sum:
        max = sum
    if sum < 0:
        sum = 0

print(max)

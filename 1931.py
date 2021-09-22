# 1931 회의실 배정

n = int(input())
arr = []
now = 0
count = 0

for i in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr.sort(key=lambda x: (x[1], x[0]))

for one in arr:
    if one[0] >= now:
        count += 1
        now = one[1]

print(count)

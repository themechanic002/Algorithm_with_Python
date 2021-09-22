# 13305 주유소
n = int(input())
dist = list(map(int, input().split()))
cities = list(map(int, input().split()))
result = 0
all = []
for i in range(len(dist)):
    all.append([cities[i], dist[i]])

min = 1_000_000_000
for i in all:
    if i[0] < min:
        min = i[0]
    else:
        i[0] = min
    result += i[0] * i[1]

print(result)
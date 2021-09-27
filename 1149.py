# 1149 RGB거리

n = int(input())
d = [[] for _ in range(n)]

for i in range(n):
    RGB = list(map(int, input().split()))
    R = RGB[0]
    G = RGB[1]
    B = RGB[2]

    if i == 0:
        d[i] = [R, G, B]
    else:
        for j in range(len(d[i - 1])):
            if j % 3 == 0:
                d[i].append(1000)
                d[i].append(d[i - 1][j] + G)
                d[i].append(d[i - 1][j] + B)
            elif j % 3 == 1:
                d[i].append(d[i - 1][j] + R)
                d[i].append(1000)
                d[i].append(d[i - 1][j] + B)
            else:
                d[i].append(d[i - 1][j] + R)
                d[i].append(d[i - 1][j] + G)
                d[i].append(1000)

print(min(d[n - 1]))
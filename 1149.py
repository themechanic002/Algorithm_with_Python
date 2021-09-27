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
            prevCol = d[i - 1][j]
            if prevCol != 'R' and prevCol != 'G' and prevCol != 'B':

                if j % 3 == 0:
                    d[i].append(999)
                    d[i].append(prevCol + G)
                    d[i].append(prevCol + B)

                elif j % 3 == 1:
                    d[i].append(prevCol + R)
                    d[i].append(999)
                    d[i].append(prevCol + B)

                elif j % 3 == 2:
                    d[i].append(prevCol + R)
                    d[i].append(prevCol + G)
                    d[i].append(999)

print(min(d[n - 1]))

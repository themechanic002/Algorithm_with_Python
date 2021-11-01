# 1904 01타일

n = int(input())
d = [i for i in range(n + 1)]
for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 2]) % 15746
print(d[n])

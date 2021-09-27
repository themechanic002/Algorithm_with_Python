# 9461 파도반 수열

n, p = int(input()), [0 for _ in range(101)]

p[1], p[2], p[3] = 1, 1, 1
p[4], p[5] = 2, 2

def pado(n):
    if p[n] != 0:
        return p[n]
    else:
        p[n] = pado(n - 1) + pado(n - 5)
        return p[n]

for i in range(n):
    print(pado(int(input())))

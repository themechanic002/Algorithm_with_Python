# 1992 쿼드트리

n = int(input())
image = []
for i in range(n):
    image.append(list(map(int, input())))
line = ""


def isAllSame(n, x, y):
    global image
    count = 0
    for i in range(n):
        for j in range(n):
            count += image[y + i][x + j]
    if count == n * n:
        return "black"
    elif count == 0:
        return "white"
    else:
        return "mixed"


def divide(n, x, y):
    global line
    is_all_same = isAllSame(n, x, y)
    if (is_all_same == "black"):
        line += "1"
        return
    elif (is_all_same == "white"):
        line += "0"
        return
    if n > 1:
        line += "("
        divide(n // 2, x, y)
        divide(n // 2, x + (n // 2), y)
        divide(n // 2, x, y + (n // 2))
        divide(n // 2, x + (n // 2), y + (n // 2))
        line += ")"


divide(n, 0, 0)
print(line)

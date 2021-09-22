# 2630 색종이 만들기

n = int(input())
papers = []
whiteNum = 0
blueNum = 0

for i in range(n):
    papers.append(list(map(int, input().split())))

def isAllSame(n, x, y):
    global papers
    count = 0
    for i in range(n):
        for j in range(n):
            count += papers[y + i][x + j]

    # 그 구역에 흰색만 있는 경우
    if (count == 0):
        return 0
    # 그 구역에 파란색만 있는 경우
    elif (count == n * n):
        return 1
    # 섞여 있는 경우
    else:
        return -1


def divide(n, x, y):
    global whiteNum
    global blueNum

    is_all_same = isAllSame(n, x, y)
    # 그 구역에 흰색만 있는 경우
    if (is_all_same == 0):
        whiteNum += 1
        return
    # 그 구역에 파란색만 있는 경우
    elif (is_all_same == 1):
        blueNum += 1
        return

    if (n > 1):
        divide(n // 2, x, y)
        divide(n // 2, x + (n // 2), y)
        divide(n // 2, x, y + (n // 2))
        divide(n // 2, x + (n // 2), y + (n // 2))

divide(n, 0, 0)
print(whiteNum)
print(blueNum)

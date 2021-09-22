n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

minusone = 0
zero = 0
plusone = 0


def isAllSame(x, y, len):
    first_val = paper[x][y]
    for i in range(len):
        for j in range(len):
            if paper[x + i][y + j] != first_val:
                return 2
    return first_val


def divide(x, y, len):
    global minusone
    global zero
    global plusone

    isAllSameValue = isAllSame(x, y, len)
    if isAllSameValue == 2:
        if len != 1:
            for i in range(3):
                for j in range(3):
                    divide(x + (i * (len // 3)), y + (j * (len // 3)), len // 3)
        else:
            if paper[x][y] == -1:
                minusone += 1
            elif paper[x][y] == 0:
                zero += 1
            else:
                plusone += 1
    else:
        if isAllSameValue == -1:
            minusone += 1
        elif isAllSameValue == 0:
            zero += 1
        else:
            plusone += 1


divide(0, 0, n)
print(minusone)
print(zero)
print(plusone)

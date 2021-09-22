# 11582 치킨 TOP N

n = int(input())
chickenListAll = list(map(int, input().split()))
k = int(input())
i = 1
while (i <= (n / k)):
    chickenList = []
    for j in range(0, n, i):
        chickenList.append(chickenListAll[j:j + i])
    for each in chickenList:
        each.sort()
    chickenListAll = []
    for e in chickenList:
        chickenListAll += e
    i *= 2

for i in chickenListAll:
    print(str(i) + " ", end="")

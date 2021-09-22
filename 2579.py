# 2579 계단 오르기

n = int(input())
dp_table = []
for i in range(n):
    dp_table.append(list(map(int, input().split())))

for line in range(1, n):
    for j in range(len(dp_table[line])):
        if j == 0:
            dp_table[line][j] += dp_table[line - 1][j]
        elif j == len(dp_table[line]) - 1:
            dp_table[line][j] += dp_table[line - 1][j - 1]
        elif dp_table[line - 1][j - 1] > dp_table[line - 1][j]:
            dp_table[line][j] += dp_table[line - 1][j - 1]
        else:
            dp_table[line][j] += dp_table[line - 1][j]

print(max(dp_table[n - 1]))

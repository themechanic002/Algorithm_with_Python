# 2579 계단 오르기
n = int(input())
dp_table = []
for i in range(n):
    dp_table.append(list(map(int, input().split())))

for i in range(n):
    for j in range(len(dp_table[n])):
        if i != 0:
            if j == 0:
                dp_table[n][j] += dp_table[n - 1][j]
            elif j == len(dp_table[n]) - 1:
                dp_table[n][j] += dp_table[n - 1][j - 1]
            elif dp_table[n - 1][j - 1] > dp_table[n - 1][j]:
                dp_table[n][j] += dp_table[n - 1][j - 1]
            else:
                dp_table[n][j] += dp_table[n - 1][j]

print(dp_table)
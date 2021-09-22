# 11047 동전 0
n, k = map(int, input().split())
coinList = []
result = 0

for i in range(n):
    coinList.append(int(input()))

for coin in reversed(coinList):
    result += k // coin
    k = k % coin

print(result)

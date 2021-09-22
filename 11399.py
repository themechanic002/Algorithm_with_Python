# 11399 ATM
n, result = int(input()), 0
list = sorted(map(int, input().split()))
for i in list:
    result += i * n
    n -= 1
print(result)

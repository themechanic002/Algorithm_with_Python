# 1003 피보나치 함수

totalNum = int(input())
d = [0] * 41
d[0] = 0
d[1] = 1

for i in range(2, 41):
    d[i] = d[i - 1] + d[i - 2]

for i in range(totalNum):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print(str(d[n - 1]) + " " + str(d[n]))

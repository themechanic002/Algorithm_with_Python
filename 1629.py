# 1629 곱셈

a, b, n = list(map(int, input().split()))
result = 1

def divide(a, b):
    global result
    global n
    if b == 1:
        return a % n
    else:
        temp = divide(a, b // 2)
        if b % 2 == 0:
            return temp * temp % n
        else:
            return temp * temp * a % n

print(divide(a, b))

"""
a, b, n = list(map(int, input().split()))
result = 1

def divide(a, b):
    global result
    global n
    if b == 1:
        result *= a % n
    else:
        if b % 2 == 0:
            divide(a, b // 2) * divide(a, b // 2) % n
        else:
            divide(a, b // 2) * divide(a, (b + 1) // 2) % n
    result *= a % n

divide(a, b)
print(result % n)
"""
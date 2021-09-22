# 1541 잃어버린 괄호
newList = []
isFirstPositive = True
for i in input().split("-"):
    if i == '':
        isFirstPositive = False
    elif "+" in i:
        newList.append(sum(map(int, i.split("+"))) * -1)
    else:
        newList.append(int(i) * -1)
if isFirstPositive:
    newList[0] *= -1

print(sum(sorted(newList)))

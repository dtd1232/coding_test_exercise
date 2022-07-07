# https://www.acmicpc.net/source/45667735
x = int(input())

if x < 1:
    exit()

list = [0, 1]
for i in range(2, x + 1):
    list.append(list[i - 1] + list[i - 2])

print(list[x])
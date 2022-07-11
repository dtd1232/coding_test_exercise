# https://www.acmicpc.net/problem/1712

temp = list(map(int, input().split()))

result = 0

if temp[1] >= temp[2]:
    print('-1')
else:
    result = temp[0] / (temp[2] - temp[1]) + 1

    result = int(result)

    print(result)

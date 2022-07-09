# 백준 10867
# https://www.acmicpc.net/problem/10867

a = int(input())

a_list = list(map(int, input().split()))

temp = []

for i in a_list:
    if i not in temp:
        temp.append(i)

temp.sort()

for i in temp:
    print(i, end=' ')

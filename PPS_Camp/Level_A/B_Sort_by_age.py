# 백준 10814
# https://www.acmicpc.net/problem/10814

n = int(input())

user = []

for i in range(n):
    user.append(list(input().split()))

user.sort(key=lambda a: int(a[0]))

for i in range(n):
    print(user[i][0], user[i][1])

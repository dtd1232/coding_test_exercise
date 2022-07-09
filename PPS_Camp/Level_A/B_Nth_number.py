# 백준 2693
# https://www.acmicpc.net/problem/2693

n = int(input())

for i in range(n):
    num_list = list(map(int, input().split()))

    num_list.sort(reverse=True)

    print(num_list[2])

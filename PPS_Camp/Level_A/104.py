# https://www.acmicpc.net/problem/14487

n = int(input())

v = list(map(int, input().split()))

max_v = max(v)

print(sum(v) - max_v)

# https://www.acmicpc.net/problem/2953

import sys
input = sys.stdin.readline()

idx = 0
result = -1
for i in range(5):
    A = list(map(int, input().split()))

    if sum(A) > result:
        result = sum(A)
        idx = i + 1

print(idx, result)
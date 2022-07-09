# 검증수 백준 2475
# https://www.acmicpc.net/problem/2475

input_list = list(map(int, input().split()))

answer = 0

for i in input_list:
    answer += i**2

print(answer % 10)

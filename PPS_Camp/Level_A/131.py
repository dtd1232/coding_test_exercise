# https://www.acmicpc.net/problem/2108

num = int(input())

total = 0
max = int(-4001)
min = int(4001)

lst = []

for i in range(num):
    lst.append(int(input()))
    total += list[i]

# average
avg = total / num
print(avg)

# middle
mid = list[num/2]
print(mid)

# mode


# range
for n in lst:
    if n < min:
        min = n
    if n > max:
        max = n

num_range = max - min
print(num_range)

'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))

# 산술평균 - 다 더해서 / n
print(round(sum(li) / n))

# 중앙값 - 오름차순 -> 중간값
li.sort()
print(li[n // 2])

# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
if len(cnt_li) > 1 and cnt_li[0][1] == cnt_li[1][1]:  # 최빈값 2개 이상
    print(cnt_li[1][0])
else:
    print(cnt_li[0][0])

# 범위 - 최댓값-최솟값
print(max(li) - min(li))
'''
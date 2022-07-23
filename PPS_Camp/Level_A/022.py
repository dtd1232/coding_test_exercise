# https://www.acmicpc.net/problem/1267

num_call = int(input())

total_call = list(map(int, input().split()))

y = 0
m = 0

for i in range(num_call):
    y_tmp = int(total_call[i] / 30 + 1) * 10
    m_tmp = int(total_call[i] / 60 + 1) * 15

    y += y_tmp
    m += m_tmp

if y > m:
    print("M", m)
elif m > y:
    print("Y", y)
else:
    print("Y M", y)

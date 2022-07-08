# 백준 4344번 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

repeat = int(input())

for i in range(repeat):
    stu_list = list(map(int, input().split()))
    stu_avg = sum(stu_list[1:]) / stu_list[0]
    count = 0

    for j in stu_list[1:]:
        if j > stu_avg:
            count += 1

    stu_rate = count / stu_list[0] * 100
    print(f'{stu_rate:.3f}%')
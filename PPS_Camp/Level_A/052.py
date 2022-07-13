# https://www.acmicpc.net/problem/8958

n = int(input())

for i in range(n):
    score = 0
    num_o = 1
    string = list(input())
    for c in string:
        if c == 'O':
            score += num_o
            num_o += 1
        else:
            num_o = 1

    print(score)

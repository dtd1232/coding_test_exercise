# https://www.acmicpc.net/problem/5598

string = list(input())

answer = []

for s in string:
    if s == 'A' or s == 'B' or s == 'C':
        answer.append(chr(ord(s)+23))
    else:
        answer.append(chr(ord(s)-3))

print(''.join(answer))

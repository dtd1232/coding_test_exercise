# https://www.acmicpc.net/problem/17213

n = int(input())
r = int(input())

result = 1
a = 1
b = 1

for i in range(n-1):
    a *= (i+1)

for i in range(n-1):
    b *= (r-1-i)

result = int(b / a)

print(result)

# https://www.acmicpc.net/problem/3062

for _ in range(int(input())):
    s = input()
    n = str(int(s) + int(s[::-1]))
    print("YES" if n == n[::-1] else "NO")
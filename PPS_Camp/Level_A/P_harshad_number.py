# 하샤드 수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True

    temp = x
    sum = 0

    while temp > 0:
        sum += temp % 10
        temp //= 10

    if x % sum == 0:
        answer = True
    else:
        answer = False

    return answer
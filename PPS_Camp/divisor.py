# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []

    for a in arr:
        a = int(a)
        if a % divisor == 0:
            answer.append(a)

    answer.sort()

    if not answer:
        answer.append(-1)

    return answer

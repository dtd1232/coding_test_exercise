# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    s = 0
    f = 0

    for c in commands:
        s = int(c[0] - 1)
        f = int(c[1])
        slice = array[s:f]
        slice.sort()
        count = int(c[2] - 1)
        answer.append(slice[count])

    return answer

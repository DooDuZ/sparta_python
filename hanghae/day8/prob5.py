# BOJ 28114 팀명 정하기

import sys

input = sys.stdin.readline


def get_input():
    params = []

    for i in range(3):
        params.append(input().strip().split())

    return params


def solution(params):
    answer = []
    params.sort(key=lambda x: int(x[1]))

    # 연도 오름차순 조합
    years = []
    for param in params:
        years.append(param[1][2:])

    # 이름 solve 수 조합
    names = []
    params.sort(key=lambda x: -int(x[0]))
    for param in params:
        names.append(param[2][:1])

    answer.append("".join(years))
    answer.append("".join(names))

    return answer


print("\n".join(solution(get_input())))

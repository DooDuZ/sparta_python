import sys
from itertools import combinations

input = sys.stdin.readline


def get_input():
    params = []

    n, s = list(map(int, input().split()))

    params.append(s)
    params.append(list(map(int, input().split())))

    return params


def solution(params):
    s, numbers = params

    total = 0

    # 조합 직접 구현해보기

    return total


if __name__ == "__main__":
    print(solution(get_input()))

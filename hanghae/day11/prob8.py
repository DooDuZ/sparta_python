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

    # combinations로 길이별 부분 수열 구하기
    for i in range(1, len(numbers) + 1):
        comb = list(combinations(numbers, i))

        for c in comb:
            if sum(c) == s:
                total += 1

    return total


if __name__ == "__main__":
    print(solution(get_input()))

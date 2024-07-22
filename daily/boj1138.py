# BOJ 1138 한 줄로 서기

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())
    taller = list(map(int, input().split()))

    return [n, taller]


def solution(params):
    n, taller = params

    answer = []

    for height in range(n - 1, -1, -1):
        answer.insert(taller[height], height + 1)

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

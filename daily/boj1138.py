# BOJ 1138 한 줄로 서기

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())
    taller = list(map(int, input().split()))

    return [n, taller]


def solution(params):
    def shift(numbers, idx):
        for i in range(n - 1, idx, -1):
            numbers[i] = numbers[i - 1]

    n, taller = params

    answer = [0 for _ in range(n)]

    for height in range(n - 1, -1, -1):
        idx = taller[height]
        if answer[idx] != 0:
            shift(answer, idx)

        answer[idx] = height + 1

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

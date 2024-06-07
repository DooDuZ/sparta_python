# BOJ 10815 숫자 카드
# 이분탐색 머하러함...

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    return [numbers, targets]


def solution(params):
    answer = []
    numbers, targets = params

    hashing = set(numbers)

    for target in targets:
        if target in hashing:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(*solution(get_input()))

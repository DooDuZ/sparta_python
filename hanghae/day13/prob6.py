# BOJ 2012 등수 매기기
# 동석차 불가능 -> 결국 앞에 사람이 생기면 한칸씩 밀릴 수 밖에 없음
# 당장 불만도가 낮은 순으로 등수를 매기자

import sys
from heapq import *


input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(int(input()))

    return params


def solution(expected):
    # 등수가 높아져도 불만이 생기는듯
    # 1등부터 하나씩 채우기
    total = 0
    rank = 1
    heapify(expected)

    while expected:
        total += abs(rank - heappop(expected))
        rank += 1

    return total


if __name__ == "__main__":
    print(solution(get_input()))

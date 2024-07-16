# BOJ 1246 온라인 판매
import sys
from heapq import *

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    buy = []

    for _ in range(m):
        buy.append(int(input()))

    return [n, m, buy]


def solution(params):
    n, m, buy = params

    buy.sort(reverse=True)

    total = 0
    cnt = 0

    for i in range(m):
        c = min(n, i + 1)
        t = buy[i] * c

        if t > total:
            total = t
            cnt = c

    return [buy[cnt - 1], total]


if __name__ == "__main__":
    print(*solution(get_input()))

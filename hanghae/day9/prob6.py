import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(int(input()))

    return params


def solution(params):
    dasom = params[0]

    heap = []

    for param in params[1:]:
        heappush(heap, -param)

    cnt = 0
    while heap and dasom <= -heap[0]:
        heappush(heap, heappop(heap) + 1)
        dasom += 1
        cnt += 1

    return cnt


print(solution(get_input()))

"""

4
10
10
10
9

4
11
10
10
10

"""

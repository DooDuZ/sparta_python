# BOJ 1374 강의실

import sys
from heapq import *

input = sys.stdin.readline


def get_input():

    n = int(input())

    lecture = []

    for _ in range(n):
        lecture.append(list(map(int, input().split())))

    return [n, lecture]


def solution(params):
    n, lecture = params

    count = 0

    heap = []

    lecture.sort(key=lambda x: (x[1], x[2], x[0]))

    for l in lecture:
        idx, start, end = l
        while heap and heap[0] <= start:
            heappop(heap)
        heappush(heap, end)

        if len(heap) > count:
            count = len(heap)

    return count


if __name__ == "__main__":
    print(solution(get_input()))

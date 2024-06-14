# BOJ 1931 회의실 배정

import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(list(map(int, input().split())))

    return params


def solution(time_table):
    # 회의 시작순 정렬
    time_table.sort()

    heap = []

    for t in time_table:
        # -heap[0] > t[0] -> 앞의 회의가 끝나지 않았음
        # -heap[0] > t[1] -> 현재 회의가 더 일찍 끝나는 경우
        # pop
        while heap and (-heap[0] > t[0] and -heap[0] > t[1]):
            heappop(heap)
        if not heap or t[0] >= -heap[0]:
            heappush(heap, -t[1])

    return len(heap)


if __name__ == "__main__":
    print(solution(get_input()))

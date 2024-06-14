# BOJ 1461 도서관
# 그리디

import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))
    books = list(map(int, input().split()))

    return [n, m, books]


def solution(params):
    n, m, books = params

    positive_heap = []
    negative_heap = []

    for book in books:
        if book > 0:
            heappush(positive_heap, -book)
        else:
            heappush(negative_heap, book)

    # 가장 먼 거리의 책을 묶어서 거리를 저장한다
    # 모든 경우에 대해 왕복 거리를 더해주고
    # 처음에 저장한 값을 빼준다
    def get_cnt(heap):
        # 총 이동 거리
        total = 0
        # 마지막 이동 거리
        first = 0

        while heap:
            # 이동해야할 거리
            # 이번에 이동할 가장 먼 책을 저장한 후
            distance = heappop(heap)

            # 첫 pop이면 값을 저장해주고
            if first == 0:
                first = distance

            for i in range(m - 1):
                if not heap:
                    break
                # 함께 들고갈 다른 책만큼 pop
                heappop(heap)

            # 왕복거리 더해주기
            total += distance * 2

        return [-total, -first]

    pos = get_cnt(positive_heap)
    neg = get_cnt(negative_heap)

    # 양쪽 거리를 더한 뒤, 가장 큰 이동 거리 빼주기
    return pos[0] + neg[0] - max(pos[1], neg[1])


if __name__ == "__main__":
    print(solution(get_input()))

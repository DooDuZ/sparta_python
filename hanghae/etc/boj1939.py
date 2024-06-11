# 멘토님 추천 문제
# BOJ 1939 중량 제한
# 그래프의 일반적인 최소 비용 문제
# 다익스트라 사용

import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(n)

    edges = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1

        edges[a].append([b, c])
        edges[b].append([a, c])

    p1, p2 = list(map(int, input().split()))

    params.append(p1 - 1)
    params.append(p2 - 1)
    params.append(edges)

    return params


def solution(params):
    n, p1, p2, edges = params

    def dijkstra():
        INF = 1_000_000_000
        costs = [0 for _ in range(n)]
        costs[p1] = INF
        heap = []

        heappush(heap, [-INF, p1])

        while heap:
            c, v = heappop(heap)

            c *= -1
            if costs[v] != c:
                continue

            for e in edges[v]:
                nv, nc = e[0], min(e[1], c)
                if nc > costs[nv]:
                    heappush(heap, [-nc, nv])
                    costs[nv] = nc

        return costs

    return dijkstra()[p2]


print(solution(get_input()))

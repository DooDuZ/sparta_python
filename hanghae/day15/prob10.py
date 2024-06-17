# BOJ 5972 택배배송

import sys
from heapq import *

input = sys.stdin.readline

INF = 1_000_000_000


def get_input():
    n, m = list(map(int, input().split()))

    edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, c = list(map(int, input().split()))

        edges[s].append([e, c])
        edges[e].append([s, c])

    return [n, m, edges]


def solution(params):
    n, m, edges = params

    dist = [INF for _ in range(n + 1)]

    def dijkstra():
        heap = [[0, 1]]
        dist[1] = 0

        while heap:
            cost, visit = heappop(heap)

            if cost != dist[visit]:
                continue

            for edge in edges[visit]:
                nv, nc = edge

                if cost + nc < dist[nv]:
                    dist[nv] = cost + nc
                    heappush(heap, [cost + nc, nv])

    dijkstra()

    return dist[n]


if __name__ == "__main__":
    print(solution(get_input()))

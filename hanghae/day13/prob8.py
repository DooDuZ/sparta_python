# BOJ 1916 최소비용 구하기
# 다익스트라

import sys
from heapq import *

input = sys.stdin.readline
INF = 1_000_000_000


def get_input():
    n = int(input())
    m = int(input())

    edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, c = list(map(int, input().split()))

        edges[s].append([c, e])

    start, end = list(map(int, input().split()))

    params = [n, m, edges, start, end]

    return params


# 주석 달만한 게 없어요...
def solution(params):
    n, m, edges, start, end = params

    dist = [INF for _ in range(n + 1)]

    def dijkstra():
        # 출발점 set
        heap = [[0, start]]
        dist[start] = 0

        while heap:
            c, v = heappop(heap)

            if dist[v] != c:
                continue

            for edge in edges[v]:
                nc, nv = edge
                if c + nc < dist[nv]:
                    dist[nv] = c + nc
                    heappush(heap, [c + nc, nv])

    dijkstra()

    return dist[end]


if __name__ == "__main__":
    print(solution(get_input()))

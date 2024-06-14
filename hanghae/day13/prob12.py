# BOJ 1238 파티
# 파티 마을을 기준으로 다익스트라
# 간선 방향을 뒤집어서 다익스트라 2번으로 해결할 수 있다.

import sys
from heapq import *

input = sys.stdin.readline

INF = 1_000_000_000


def get_input():
    n, m, x = list(map(int, input().split()))

    in_edges = [[] for _ in range(n + 1)]
    out_edges = [[] for _ in range(n + 1)]

    for _ in range(m):
        s, e, c = list(map(int, input().split()))
        in_edges[s].append([e, c])
        out_edges[e].append([s, c])

    return [n, m, x, in_edges, out_edges]


def solution(params):
    n, m, x, in_edges, out_edges = params

    def dijkstra(edges):
        dist = [INF for _ in range(n + 1)]
        heap = [[0, x]]
        dist[x] = 0

        while heap:
            c, v = heappop(heap)

            if dist[v] != c:
                continue

            for edge in edges[v]:
                nv, nc = edge

                if c + nc < dist[nv]:
                    dist[nv] = c + nc
                    heappush(heap, [c + nc, nv])

        return dist

    # 파티 가요
    to_party = dijkstra(in_edges)
    # 집에 와요
    to_home = dijkstra(out_edges)

    longest = 0

    # 왕복 거리 중 가장 큰 값 찾기
    for i in range(1, n + 1):
        if i == x:
            continue
        longest = max(longest, to_home[i] + to_party[i])

    return longest


if __name__ == "__main__":
    print(solution(get_input()))

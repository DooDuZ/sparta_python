# 풀이 1 다익스트라 응용
# ?? 실수로 maxheap안하고 minheap했는데 통과됨...
# 정렬 기준도 뒤에 놨는데 통과됨...
# maxheap + 가중치 앞으로해서 다시

import sys
from heapq import *

input = sys.stdin.readline
INF = 1_000_000_000


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    edge_input = []

    for _ in range(m):
        edge_input.append(list(map(int, input().split())))

    params.append(n)
    params.append(edge_input)
    s, e = list(map(int, input().split()))
    params.append(s)
    params.append(e)

    return params


def get_edges(n, edge_input):
    edges = [[] for _ in range(n + 1)]

    for edge in edge_input:
        start, end, cost = edge
        edges[start].append([end, cost])
        edges[end].append([start, cost])

    return edges


def dijkstra(costs, edges, city):
    heap = [[-INF, city]]

    while heap:
        weight, v = heappop(heap)

        if costs[v] != weight:
            continue

        for edge in edges[v]:
            nv, nw = edge
            nw = max(weight, -nw)

            if costs[nv] > nw:
                costs[nv] = nw
                heappush(heap, [nw, nv])


def solution(params):
    n, edge_input, start, end = params
    edges = get_edges(n, edge_input)
    costs = [0 for _ in range(n + 1)]
    costs[start] = -INF
    dijkstra(costs, edges, start)

    return -costs[end]


if __name__ == "__main__":
    print(solution(get_input()))

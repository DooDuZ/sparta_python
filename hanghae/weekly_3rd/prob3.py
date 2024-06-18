# BOJ 10473 인간 대포

import sys
import math
from heapq import *

input = sys.stdin.readline
INF = 1_000_000_000


def get_input():
    params = []

    start = list(map(float, input().split()))
    end = list(map(float, input().split()))

    n = int(input())

    node = [start, end]

    for _ in range(n):
        node.append(list(map(float, input().split())))

    return [n, node]


def solution(params):
    def get_distance(start_node, end_node):
        d = (
            abs(start_node[0] - end_node[0]) ** 2
            + abs(start_node[1] - end_node[1]) ** 2
        ) ** (1 / 2)

        if d > 10:
            if d <= 50:
                d = 10
            else:
                d -= 40

        return d / 5

    def dijkstra():
        heap = [[0, 0]]

        while heap:
            cost, visit = heappop(heap)

            if dist[visit] != cost:
                continue

            for nv, nc in enumerate(edges[visit]):
                if nv == visit:
                    continue

                if cost + nc < dist[nv]:
                    dist[nv] = cost + nc
                    heappush(heap, [cost + nc, nv])

    n, nodes = params
    dist = [INF for _ in range(n + 2)]
    dist[0] = 0

    # 인접 행렬
    # 걸어서 갈 수 있기 때문에 모든 노드는 연결되어 있다
    # 출발, 도착점도 하나의 노드로 추가
    edges = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    # 대포 노드들 사이의 거리 구하기
    # 끝점까지 거리도 구한다.. 대포 타고 갈 수 있으니깐..
    for i in range(2, n + 2):
        for j in range(1, n + 2):
            if i == j:
                edges[i][j] == 0
                continue
            edges[i][j] = get_distance(nodes[i], nodes[j])

    # 첫 노드에서 다른 노드들까지의 거리 구하기
    for i in range(1, n + 2):
        edges[0][i] = (
            math.sqrt(
                abs(nodes[0][0] - nodes[i][0]) ** 2
                + abs(nodes[0][1] - nodes[i][1]) ** 2
            )
            / 5
        )

    dijkstra()

    return dist[1]


if __name__ == "__main__":
    print(round(solution(get_input()), 6))

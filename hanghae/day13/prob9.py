# BOJ 4485 녹색 옷 입은 애가 젤다지?
# 최소 비용
# 인접 리스트의 형태만 조금 다름 / 다익스트라로 해결

import sys
from heapq import *

input = sys.stdin.readline
INF = 1_000_000_000


def get_input():
    params = []

    while True:
        n = int(input())
        if n == 0:
            break

        cave = []

        for _ in range(n):
            cave.append(list(map(int, input().split())))
        params.append([n, cave])

    return params


def convert_to_format(t, number):
    return f"Problem {t}: {number}"


def solution(param):
    def check_range(row, col):
        return 0 <= row < n and 0 <= col < n

    n, cave = param
    dist = [[INF for _ in range(n)] for _ in range(n)]

    def dijkstra():
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        heap = [[0, 0, cave[0][0]]]
        dist[0][0] = cave[0][0]

        while heap:
            row, col, cost = heappop(heap)

            if dist[row][col] != cost:
                continue

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if check_range(nr, nc) and cost + cave[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = cost + cave[nr][nc]
                    heappush(heap, [nr, nc, cost + cave[nr][nc]])

    dijkstra()

    return dist[n - 1][n - 1]


if __name__ == "__main__":
    params = get_input()
    for i, param in enumerate(params):
        print(convert_to_format(i + 1, solution(param)))

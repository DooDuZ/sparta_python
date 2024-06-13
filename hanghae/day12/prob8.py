# BOJ 17086 아기상어
# 단순 bfs

import sys
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))


def get_input():
    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return cells


def check_range(row, col):
    return 0 <= row < n and 0 <= col < m


def bfs(q, dist):
    dr = [1, -1, 0, 0, 1, 1, -1, -1]
    dc = [0, 0, 1, -1, 1, -1, 1, -1]

    while q:
        r, c, d = q.popleft()

        # 다음 이동 거리
        nd = d + 1

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            # 범위 안쪽이고 안전 거리가 기존보다 더 작으면 갱신
            if check_range(nr, nc) and dist[nr][nc] > nd:
                dist[nr][nc] = nd
                q.append([nr, nc, nd])


def solution(cells):
    q = deque()
    dist = [[50 for _ in range(m)] for _ in range(n)]

    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            # 아기 상어자리에서 탐색 시작
            if cell == 1:
                dist[i][j] = 0
                q.append([i, j, 0])
                bfs(q, dist)

    # 최대값 구하기
    max_d = 0

    for row in dist:
        max_d = max(max_d, max(row))

    return max_d


if __name__ == "__main__":
    print(solution(get_input()))

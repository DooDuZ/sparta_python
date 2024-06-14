# BOJ 1261 알고스팟
# 데이터의 크기가 작기 때문에 다익스트라 없이 bfs로도 풀린다

import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    # n m 평소랑 다르게 뒤집어서 줌...
    m, n = list(map(int, input().split()))

    cells = []
    for _ in range(n):
        cells.append(list(map(int, input().strip())))

    return [n, m, cells]


def solution(params):
    n, m, cells = params

    count = [[200 for _ in range(m)] for _ in range(n)]

    def check_range(row, col):
        return 0 <= row < n and 0 <= col < m

    def bfs():
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        q = deque()
        q.append([0, 0, 0])
        count[0][0] = 0

        while q:
            row, col, cost = q.popleft()

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if (
                    check_range(nr, nc)
                    and cells[nr][nc] == 1
                    and cost + 1 < count[nr][nc]
                ):
                    count[nr][nc] = cost + 1
                    q.append([nr, nc, cost + 1])
                elif (
                    check_range(nr, nc) and cells[nr][nc] == 0 and cost < count[nr][nc]
                ):
                    count[nr][nc] = cost
                    q.append([nr, nc, cost])

    bfs()

    return count[n - 1][m - 1]


if __name__ == "__main__":
    print(solution(get_input()))

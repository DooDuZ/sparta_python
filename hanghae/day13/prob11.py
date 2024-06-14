# BOJ 1261 알고스팟
# 거리 대신 벽을 부순 횟수를 2차원 리스트로 저장한다

import sys
from heapq import *

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

    def dijkstra():
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        heap = [[0, 0, 0]]
        count[0][0] = 0

        while heap:
            row, col, cnt = heappop(heap)

            if count[row][col] != cnt:
                continue

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                # 3중 if문 레전드...
                if check_range(nr, nc):
                    # 벽이면
                    if cells[nr][nc] == 1:
                        # 벽부순 횟수 1 더해서 비교
                        if cnt + 1 < count[nr][nc]:
                            count[nr][nc] = cnt + 1
                            heappush(heap, [nr, nc, cnt + 1])
                    else:
                        # 통로면 횟수 증가 없이 진행
                        if cnt < count[nr][nc]:
                            count[nr][nc] = cnt
                            heappush(heap, [nr, nc, cnt])

    dijkstra()

    return count[n - 1][m - 1]


if __name__ == "__main__":
    print(solution(get_input()))

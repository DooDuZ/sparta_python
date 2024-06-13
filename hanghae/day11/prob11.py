# BOJ 2573 빙산

import sys
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def get_input():
    iceberg = []

    for i in range(n):
        iceberg.append(list(map(int, input().split())))

    return iceberg


def count_group(iceberg):
    visited = [[True for _ in range(m)] for _ in range(n)]
    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] <= 0:
                continue

            if visited[i][j]:
                visited[i][j] = False
                q.append([i, j])
                bfs(q, visited, iceberg)
                cnt += 1

    return cnt


def check_range(row, col):
    if 0 <= row < n and 0 <= col < m:
        return True
    return False


def bfs(q, visited, iceberg):
    while q:
        row, col = q.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if check_range(nr, nc) and visited[nr][nc] and iceberg[nr][nc] > 0:
                visited[nr][nc] = False
                q.append([nr, nc])


# 인접한 바다를 카운트해서 차감
# 즉시 차감 시 옆 빙산이 더 녹을 수 있으므로 녹는 양과 좌표를 저장했다가 한번에 처리
def melt_iceberg(iceberg):
    store = []

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]

                    cnt = 0
                    if check_range(nr, nc) and iceberg[nr][nc] == 0:
                        cnt += 1

                    if cnt > 0:
                        store.append([i, j, cnt])

    while store:
        row, col, cnt = store.pop()
        iceberg[row][col] -= cnt
        if iceberg[row][col] < 0:
            iceberg[row][col] = 0


def solution(iceberg):
    cnt = 0

    while True:
        group = count_group(iceberg)
        if group > 1:
            return cnt
        elif group == 0:
            return 0
        cnt += 1
        melt_iceberg(iceberg)


if __name__ == "__main__":
    print(solution(get_input()))

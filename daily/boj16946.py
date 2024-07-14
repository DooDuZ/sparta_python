# BOJ 16946 벽 부수고 이동하기 4
import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))

    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().rstrip())))

    return [n, m, cells]


def solution(params):

    def check_range(row, col):
        return 0 <= row < n and 0 <= col < m

    def bfs(q):
        cnt = 0

        while q:
            row, col = q.popleft()

            cell_group[row][col] = group_count

            cnt += 1

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if check_range(nr, nc) and cells[nr][nc] == 0 and visited[nr][nc]:
                    visited[nr][nc] = False
                    q.append([nr, nc])

        return cnt

    def get_size(row, col):
        cnt = 1

        visit = set()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if (
                check_range(nr, nc)
                and cells[nr][nc] == 0
                and cell_group[nr][nc] not in visit
                and cell_group[nr][nc] in group
            ):
                visit.add(cell_group[nr][nc])
                cnt += group[cell_group[nr][nc]]

        return cnt

    n, m, cells = params

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    group_count = 0
    cell_group = [[-1 for _ in range(m)] for _ in range(n)]
    group = dict()

    visited = [[True for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if cells[i][j] == 0 and visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = False
                size = bfs(q)
                group[group_count] = size
                group_count += 1

    for i in range(n):
        for j in range(m):
            if cells[i][j] == 1:
                cells[i][j] = get_size(i, j) % 10

    return cells


if __name__ == "__main__":
    cells = solution(get_input())
    print("\n".join("".join(map(str, line)) for line in cells))

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())


def get_input():
    params = []

    for _ in range(n):
        params.append(input().strip())

    return params


def get_color(color, is_weakness):
    if is_weakness and color == "G":
        return "R"
    return color


def check_range(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def bfs(q, grid, visited, is_weakness):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        row, col, color = q.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if (
                check_range(nr, nc)
                and get_color(grid[nr][nc], is_weakness)
                == get_color(color, is_weakness)
                and visited[nr][nc]
            ):
                visited[nr][nc] = False
                q.append([nr, nc, color])


def check_grid(grid, is_weakness):
    q = deque()

    visited = [[True for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                visited[i][j] = False
                q.append([i, j, grid[i][j]])
                bfs(q, grid, visited, is_weakness)
                cnt += 1

    return cnt


def solution(grid):
    answer = []

    # 정상 시력 cnt
    answer.append(check_grid(grid, False))
    # 색약 cnt
    answer.append(check_grid(grid, True))

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

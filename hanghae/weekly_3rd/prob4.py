# BOJ 16236 아기상어

import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    n = int(input())

    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return [n, cells]


def solution(params):
    def check_range(row, col):
        return 0 <= row < n and 0 <= col < n

    def find_smaller(shark):
        # 위, 좌우, 아래 순 은 의미없음...!!
        dr = [-1, 0, 0, 1]
        dc = [0, -1, 1, 0]

        row, col, size = shark

        q = deque()
        visited = [[True for _ in range(n)] for _ in range(n)]
        q.append([row, col, 0])
        visited[row][col] = False

        flag = False
        final_d = 0

        ret = [row, col, 0]

        fish = []

        while q:
            r, c, d = q.popleft()

            if flag:
                if d > final_d:
                    q.append([r, c, d])
                    break

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if check_range(nr, nc) and visited[nr][nc] and cells[nr][nc] <= size:
                    if cells[nr][nc] < size:
                        if cells[nr][nc] > 0:
                            fish.append([nr, nc, d + 1])
                        if not flag and cells[nr][nc] != 0:
                            flag = True
                            final_d = d

                    visited[nr][nc] = False
                    q.append([nr, nc, d + 1])

        fish.sort(key=lambda x: (x[0], x[1]))

        return ret if not fish else fish[0]

    n, cells = params

    shark = [0, 0, 0]

    total = 0
    feed = 0

    for i, line in enumerate(cells):
        for j, cell in enumerate(line):
            if cell == 9:
                shark = [i, j, 2]
                cells[i][j] = 0
                break

    while True:
        nr, nc, d = find_smaller(shark)
        cells[nr][nc] = 0

        if d == 0:
            break

        feed += 1
        total += d

        shark[0] = nr
        shark[1] = nc

        if feed == shark[2]:
            feed = 0
            shark[2] += 1

    return total


if __name__ == "__main__":
    print(solution(get_input()))

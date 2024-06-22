# BOJ 17144 미세먼지 안녕

import sys

input = sys.stdin.readline


def get_input():
    r, c, t = list(map(int, input().split()))
    cells = []

    for _ in range(r):
        cells.append(list(map(int, input().split())))

    return [r, c, t, cells]


def solution(params):
    def check_range(row, col):
        return 0 <= row < r and 0 <= col < c

    def set_cleaner():
        cur = 0

        for i in range(r):
            if cells[i][0] == -1:
                cur = i
                break

        return [cur, cur + 1]

    def round(row, dr, row_limit):
        col = 0
        idx = 0
        flag = True

        while idx < 4:
            nr = row + dr[idx]
            nc = col + dc[idx]

            if row == row_limit and idx >= 1 and flag:
                flag = False
                idx += 1
                continue

            if not check_range(nr, nc):
                idx += 1
                continue

            if cells[nr][nc] == -1:
                break

            if cells[row][col] != -1:
                cells[row][col] = cells[nr][nc]
            cells[nr][nc] = 0

            row = nr
            col = nc

    def extends(row, col, values):
        d_r = [1, -1, 0, 0]
        d_c = [0, 0, 1, -1]

        value = cells[row][col] // 5

        for i in range(4):
            nr = row + d_r[i]
            nc = col + d_c[i]

            if check_range(nr, nc) and cells[nr][nc] != -1:
                values.append([nr, nc, value])
                values.append([row, col, -value])

    r, c, t, cells = params

    round_up = [-1, 0, 1, 0]
    round_down = [1, 0, -1, 0]

    dc = [0, 1, 0, -1]

    up_row, down_row = set_cleaner()

    for _ in range(t):
        # 미세먼지 확산
        values = []
        for i in range(r):
            for j in range(c):
                if cells[i][j] == -1:
                    continue
                extends(i, j, values)

        for value in values:
            d_r, d_c, d_v = value
            cells[d_r][d_c] += d_v

        round(up_row, round_up, up_row)
        round(down_row, round_down, down_row)

    total = 2

    for i in range(r):
        for j in range(c):
            total += cells[i][j]

    return total


if __name__ == "__main__":
    print(solution(get_input()))

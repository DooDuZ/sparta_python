import sys
from collections import deque

input = sys.stdin.readline

board = [list(map(int, input().strip().split())) for _ in range(19)]

# 세로 가로 대각 2개
dr = [[1, -1], [0, 0], [1, -1], [-1, 1]]
dc = [[0, 0], [1, -1], [-1, 1], [-1, 1]]


def is_possible(row, col):
    if (0 <= row < 19) and (0 <= col < 19):
        return True
    return False


def check_win(row, col, color):
    ret = [False, []]

    for direction in range(4):
        cnt = 0
        q = deque()
        visited = [[True for _ in range(19)] for _ in range(19)]
        visited[row][col] = False
        q.append([row, col])

        left_stone = [row, col]
        while q:
            cur_r, cur_c = q.popleft()
            cnt += 1
            if cur_c < left_stone[1]:
                left_stone = [cur_r, cur_c]

            for j in range(2):
                nr = cur_r + dr[direction][j]
                nc = cur_c + dc[direction][j]
                if is_possible(nr, nc) and visited[nr][nc] and board[nr][nc] == color:
                    visited[nr][nc] = False
                    q.append([nr, nc])
        if cnt == 5:
            ret[0] = True
            ret[1] = left_stone
            break

    return ret


win_color = 0
coords = []

for i in range(19):
    flag = False
    for j in range(19):
        if board[i][j] == 0:
            continue

        result = check_win(i, j, board[i][j])

        if result[0]:
            flag = True
            win_color = board[i][j]
            coords = [result[1][0] + 1, result[1][1] + 1]
            break
    if flag:
        break

print(win_color)
if coords:
    print(*coords)

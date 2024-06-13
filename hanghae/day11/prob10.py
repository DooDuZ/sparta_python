# BOJ 11559 puyo puyo
# 전체 탐색, 4개 이상 그룹 제거, 낙하 반복

import sys
from collections import deque

input = sys.stdin.readline
n, m = 12, 6


def get_input():
    board = []

    for i in range(12):
        board.append(list(input().strip()))

    return board


# bfs 돌면서 4개 이상 연결된 것 제거
# 제거한 횟수 return
def count_puyo(board):
    total = 0

    # bfs를 진행하며 같은 그룹인 뿌요를 카운트한다
    visited = [[True for _ in range(m)] for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(m):
            if visited[i][j] and board[i][j] != ".":
                visited[i][j] = False
                q.append([i, j, board[i][j]])
                total += bfs(q, visited, board)
    return total


# 같은 색 탐색
def bfs(q, visited, board):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 순회한 puyo의 좌표를 담을 stack
    # size가 4보다 큰 상태로 마무리 되면 pop하면서 빈칸으로 바꿔준다
    memory_stack = []

    while q:
        row, col, color = q.popleft()
        memory_stack.append([row, col])

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if check_range(nr, nc) and visited[nr][nc] and board[nr][nc] == color:
                visited[nr][nc] = False
                q.append([nr, nc, color])

    if len(memory_stack) >= 4:
        remove_puyo(memory_stack, board)
        return 1

    return 0


# 뿌요 게임보드에서 제거
def remove_puyo(stack, board):
    while stack:
        row, col = stack.pop()
        board[row][col] = "."


# 뿌요 낙하 시키기
def drop_puyo(board):
    # 아래부터 당겨야하기 때문에 위아래 역순 탐색
    for i in range(n - 1, -1, -1):
        for j in range(m):
            if board[i][j] == ".":
                continue
            row = i
            color = board[i][j]
            while row + 1 < n and board[row + 1][j] == ".":
                row += 1

            board[i][j] = "."
            board[row][j] = color


# 범위 체크
def check_range(row, col):
    if 0 <= row < n and 0 <= col < m:
        return True
    return False


def solution(board):
    total = 0
    while True:
        cnt = count_puyo(board)
        if cnt == 0:
            break
        total += 1
        drop_puyo(board)

    return total


if __name__ == "__main__":
    print(solution(get_input()))

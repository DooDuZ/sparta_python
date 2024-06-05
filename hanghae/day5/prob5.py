import sys

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

dc = ["W", "B"]

SIZE = 8
change = 64

board = [input().strip() for _ in range(n)]


def check_board(r, c, color):
    cnt = 0

    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if board[i][j] != dc[color]:
                cnt += 1
            # 검사 후 색 변경
            color += 1
            color %= 2
        # 행 전환 시 색 바뀜
        color += 1
        color %= 2

    return cnt


# 8*8을 포함할 수 있는 모든 정점 탐색
for i in range(n - SIZE + 1):
    for j in range(m - SIZE + 1):
        change = min(change, check_board(i, j, 0), check_board(i, j, 1))

print(change)

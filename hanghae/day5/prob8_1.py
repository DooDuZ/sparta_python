import sys

input = sys.stdin.readline

N, M, r = list(map(int, input().strip().split()))

board = [list(map(int, input().strip().split())) for _ in range(N)]

state = [[0 for _ in range(M)] for _ in range(N)]


def rotate(prev):
    n_board = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(min(N, M) // 2):
        shift_outline(i, i, n_board, i, prev)

    return n_board


def shift_outline(row, col, next_board, indent, prev):
    idx = 0
    dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while idx < 4:
        nr, nc = row + dc[idx][0], col + dc[idx][1]
        if is_forward(nr, nc, indent):
            next_board[row][col] = prev[nr][nc]

            row = nr
            col = nc

        else:
            idx += 1


def is_forward(r, c, indent):
    if not (0 + indent <= r < N - indent) or not (0 + indent <= c < M - indent):
        return False
    return True


lng = (N - 1 + M - 1) * 2
dp = [[] for _ in range(lng)]
dp[0] = board


def set_dp(idx):
    for i in range(1, idx + 1):
        dp[i] = rotate(dp[i - 1])


set_dp(lng - 1)


def get_rotate_r():
    n_board = [[0 for _ in range(M)] for _ in range(N)]
    dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(min(N, M) // 2):
        row, col = i, i
        idx = 0
        while idx < 4:
            nr, nc = row + dc[idx][0], col + dc[idx][1]
            if is_forward(nr, nc, i):
                n_board[row][col] = dp[r % (lng - i)][row][col]

                row = nr
                col = nc

            else:
                idx += 1

    return n_board


print("\n".join(" ".join(map(str, row)) for row in get_rotate_r()))

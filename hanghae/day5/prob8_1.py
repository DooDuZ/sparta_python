import sys

input = sys.stdin.readline

n, m, r = list(map(int, input().strip().split()))

board = [list(map(int, input().strip().split())) for _ in range(n)]

state = [[0 for _ in range(m)] for _ in range(n)]


def rotate(prev):
    n_board = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(min(n, m) // 2):
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
    if not (0 + indent <= r < n - indent) or not (0 + indent <= c < m - indent):
        return False
    return True


lng = (n - 1 + m - 1) * 2
dp = [[] for _ in range(lng)]
dp[0] = board


def set_dp(idx):
    for i in range(1, idx + 1):
        dp[i] = rotate(dp[i - 1])


set_dp(lng - 1)


def get_rotate_r():
    n_board = [[0 for _ in range(m)] for _ in range(n)]
    dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(min(n, m) // 2):
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

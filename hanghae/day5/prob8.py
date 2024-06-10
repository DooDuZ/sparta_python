import sys

input = sys.stdin.readline

N, M, r = list(map(int, input().strip().split()))

board = [list(map(int, input().strip().split())) for _ in range(N)]
dp = [[] for _ in range(N * M)]
dp[0] = board


def rotate():
    global board

    n_board = [[0 for _ in range(M)] for _ in range(N)]

    # 바깥부터 1칸씩 들어가며 돌려줍니다
    for i in range(min(N, M) // 2):
        shift(i, i, n_board, i)
    board = n_board


def shift(row, col, next_board, indent):
    idx = 0
    # 방향 리스트
    # 오른쪽 -> 아래 -> 왼쪽 -> 위 순서
    dc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 4방향 다 돌 때까지
    while idx < 4:
        nr, nc = row + dc[idx][0], col + dc[idx][1]
        # 다음 방향 진행이 가능하면
        if is_forward(nr, nc, indent):
            # 현재 위치에 다음 위치 값을 넣어준다
            next_board[row][col] = board[nr][nc]

            row = nr
            col = nc

        else:
            # 진행 끝나면 방향 전환
            idx += 1


def is_forward(r, c, indent):
    if not (indent <= r < N - indent) or not (indent <= c < M - indent):
        return False
    return True


for _ in range(r):
    rotate()

print("\n".join(" ".join(map(str, row)) for row in board))

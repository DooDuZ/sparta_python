import sys

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

lng = 0

board = [[int(x) for x in input().strip()] for _ in range(n)]


# r,c = 좌표, l = 현재 좌표에서 가능한 최대 크기
def find_bigger(r, c, l):
    while l > 0 and not is_square(r, c, l):
        l -= 1

    return l


# 모든 꼭지접 값 비교
def is_square(r, c, l):
    return board[r][c] == board[r + l][c] == board[r][c + l] == board[r + l][c + l]


# 모든 정점 탐색
for i in range(n):
    for j in range(m):
        # 현재 정점에서 가능한 정사각형의 최대 크기
        l = min(n - i - 1, m - j - 1)
        # 가능한 최대 길이가 탐색한 최대 길이보다 짧다면 continue
        if l < lng:
            continue
        lng = max(lng, find_bigger(i, j, l))

lng += 1
print(lng * lng)

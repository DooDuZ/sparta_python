# BOJ 14890 경사로
# 리팩토링 했는데도 더러움... 더 안할랍니다.

import sys

input = sys.stdin.readline
n, L = list(map(int, input().split()))
cells = []

dr = [1, 0]
dc = [0, 1]


def get_input():
    for _ in range(n):
        cells.append(list(map(int, input().split())))


def check_range(row, col):
    return 0 <= row < n and 0 <= col < n


def count_length(row, col, direction, build, is_forward):
    cnt = 0

    start = cells[row][col]

    # 검사 방향 따라서 더할지 뺄지 달라짐
    d = 1 if is_forward else -1

    # 범위 안넘고 설치 안한 땅이고 cnt는 L넘을 필요 없고 검사 위치가 시작 위치와 같은 높이라면
    while (
        check_range(row, col)
        and build[row if direction == 0 else col]
        and cnt < L
        and cells[row][col] == start
    ):
        # 길이 늘려주고
        cnt += 1
        # 건물 표시 해주고
        build[row if direction == 0 else col] = False
        # 좌표 이동
        row += dr[direction] * d
        col += dc[direction] * d

    return cnt


def move(row, col, direction):
    # 설치 정보 저장 배열
    build = [True for _ in range(n)]

    # 끝칸에 도달할 때까지
    while row + dr[direction] < n and col + dc[direction] < n:
        nr = row + dr[direction]
        nc = col + dc[direction]

        # 앞칸과 높이가 같으면 진행
        if cells[nr][nc] == cells[row][col]:
            row = nr
            col = nc
        # 앞쪽이 한 칸 높으면
        elif cells[nr][nc] - 1 == cells[row][col]:
            # 지난 길에 설치 가능 체크
            if L <= count_length(row, col, direction, build, False):
                row = nr
                col = nc
            else:
                return 0
        # 한 칸 낮으면
        elif cells[nr][nc] + 1 == cells[row][col]:
            # 앞쪽땅 설치 가능 체크
            if count_length(nr, nc, direction, build, True) >= L:
                row = row + L * dr[direction]
                col = col + L * dc[direction]
            else:
                return 0
        else:
            return 0

    return 1


def solution():
    cnt = 0

    for i in range(n):
        cnt += move(i, 0, 1)

    for i in range(n):
        cnt += move(0, i, 0)

    return cnt


if __name__ == "__main__":
    get_input()
    print(solution())

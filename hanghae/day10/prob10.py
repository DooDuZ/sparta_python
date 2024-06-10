import sys
from collections import deque

input = sys.stdin.readline
N, M, H = 0, 0, 0
# 토마토 수 세기
cnt = 0


def get_input():
    global N, M, H, cnt
    N, M, H = list(map(int, input().split()))

    tomatoes = []

    # 귀찮다... 다 만들어서 넘기자
    for _ in range(H):
        floor = []
        for _ in range(M):
            row = []
            for tomato in list(map(int, input().split())):
                row.append(tomato)
                if tomato == -1:
                    cnt += 1
            floor.append(row)
        tomatoes.append(floor)

    cnt = N * M * H - cnt

    return tomatoes


def check_range(r, c, height):
    if (0 <= r < M) and (0 <= c < N) and (0 <= height < H):
        return True
    return False


def bfs(q, tomatoes):
    global cnt

    dr = [1, -1, 0, 0, 0, 0]
    dc = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    duration = 0

    while q:
        h, r, c, day = q.popleft()
        cnt -= 1

        duration = max(day, duration)

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = h + dh[i]

            if check_range(nr, nc, nh) and tomatoes[nh][nr][nc] == 0:
                tomatoes[nh][nr][nc] = 1
                q.append([nh, nr, nc, day + 1])

    if cnt > 0:
        return -1

    return duration


def solution(tomatoes):
    q = deque()

    for height, floor in enumerate(tomatoes):
        for i, row in enumerate(floor):
            for j, tomato in enumerate(row):
                if tomato == 1:
                    q.append([height, i, j, 0])

    return bfs(q, tomatoes)


if __name__ == "__main__":
    print(solution(get_input()))

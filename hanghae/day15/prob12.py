# BOJ 17142 연구소3
# 주어진 조건에서 조합의 최대 개수는 10C5 = 252개
# cell의 최대 크기 50 * 50
# 최대 탐색 63만번
# python3 시간제한 1.5초 충분할듯

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))

    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return [n, m, cells]


def solution(params):
    def check_range(row, col):
        return 0 <= row < n and 0 <= col < n

    def bfs(q, visited):
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        # 감염시킨 칸 수
        cnt = 0
        # 마지막으로 통로에 전파된 시간
        last = 0

        while q:
            row, col, t = q.popleft()

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                # 벽만 아니면 진행
                if check_range(nr, nc) and visited[nr][nc] and cells[nr][nc] != 1:
                    visited[nr][nc] = False
                    q.append([nr, nc, t + 1])
                    # 통로에 전파될 때만 갱신
                    if cells[nr][nc] == 0:
                        cnt += 1
                        last = t + 1

        return [last, cnt]

    n, m, cells = params

    # 바이러스 위치 저장
    virus_set = set()
    # 통로의 개수
    path_cnt = 0

    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if cell == 2:
                virus_set.add((i, j))
            elif cell == 0:
                path_cnt += 1

    # 바이러스 위치 조합
    comb = list(combinations(virus_set, m))

    # 실제 가능한 최대값은 2500의 절반 정도
    time = 2500

    for c in comb:

        q = deque()
        visited = [[True for _ in range(n)] for _ in range(n)]

        # q만들어서
        for coord in c:
            row, col = coord
            q.append([row, col, 0])
            visited[row][col] = False

        # 탐색
        last, cnt = bfs(q, visited)
        # 모든 통로를 감염시켰다면 time 갱신
        if cnt == path_cnt:
            time = min(last, time)

    return time if time != 2500 else -1


if __name__ == "__main__":
    print(solution(get_input()))

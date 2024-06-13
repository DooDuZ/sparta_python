# BOJ 14502 연구소
# 브루트포스
# dfs로도 구현해보기

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))


def get_input():
    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return cells


# 전역 변수를 사용하므로 밖에 선언
def check_range(r, c):
    return 0 <= r < n and 0 <= c < m


def solution(cells):

    area = 0
    # 벽을 3개 추가할 예정이므로 3 시작
    walls = 3

    def bfs(q, visited):
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        cnt = 0

        while q:
            r, c = q.popleft()
            cnt += 1

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if check_range(nr, nc) and visited[nr][nc] and cells[nr][nc] != 1:
                    visited[nr][nc] = False
                    q.append([nr, nc])

        return cnt

    path = []
    viruses = []

    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if cell == 0:
                path.append((i, j))
            elif cell == 1:
                walls += 1
            elif cell == 2:
                viruses.append((i, j))

    comb = list(combinations(path, 3))

    for c in comb:
        # 전체 넓이 - 벽의 개수
        # 여기서 바이러스의 수만 빼주면 안전구역의 넓이임
        total = n * m - walls

        # 벽 세우기
        for coord in c:
            row, col = coord
            cells[row][col] = 1

        # 바이러스 영역 차감
        visited = [[True for _ in range(m)] for _ in range(n)]
        q = deque()
        for virus in viruses:
            # 이미 확산된 지역이면 pass
            if not visited[virus[0]][virus[1]]:
                continue
            q.append(virus)
            visited[virus[0]][virus[1]] = False
            total -= bfs(q, visited)

        # 안전 지역 계산하기
        area = max(total, area)

        # 설치한 벽 제거하기
        for coord in c:
            row, col = coord
            cells[row][col] = 0

    return area


if __name__ == "__main__":
    print(solution(get_input()))

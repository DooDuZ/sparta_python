# BOJ 21609 상어 중학교

import sys
from collections import deque
from heapq import *

input = sys.stdin.readline
N, M = list(map(int, input().split()))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def get_input():
    cells = []

    for _ in range(N):
        cells.append(list(map(int, input().split())))

    return cells


def check_range(row, col):
    return 0 <= row < N and 0 <= col < N


def get_cnt(q, visited, color, cells):
    # 무지개 블록 개수 세기
    rainbow = 0
    # 넓이
    cnt = 0
    while q:
        row, col = q.popleft()
        cnt += 1

        if cells[row][col] == 0:
            rainbow += 1

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if (
                check_range(nr, nc)
                and visited[nr][nc]
                and (cells[nr][nc] == color or cells[nr][nc] == 0)
            ):
                visited[nr][nc] = False
                q.append([nr, nc])

    # 맥스힙 사용 예정이므로 -
    return [-cnt, -rainbow]


def rotate(cells):
    new_cells = []

    for i in range(N - 1, -1, -1):
        row = []
        for j in range(N):
            row.append(cells[j][i])
        new_cells.append(row)

    return new_cells


def drop(cells):
    # 아래부터 내려줘야함
    for i in range(N - 1, -1, -1):
        for j in range(N):
            if cells[i][j] >= 0:
                nr = i
                # -2 == 공백값으로 사용
                while check_range(nr + 1, j) and cells[nr + 1][j] == -2:
                    nr += 1
                # 값이 변한 경우에만 내려주기
                if nr != i:
                    cells[nr][j] = cells[i][j]
                    cells[i][j] = -2


def uncheck(visited, rainbow_set):
    for coord in rainbow_set:
        r, c = coord
        visited[r][c] = True


def remove_blocks(row, col, cells):
    color = cells[row][col]

    q = deque()
    visited = [[True for _ in range(N)] for _ in range(N)]
    visited[row][col] = False
    q.append([row, col])

    while q:
        r, c = q.popleft()

        # 공백 처리
        cells[r][c] = -2

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (
                check_range(nr, nc)
                and visited[nr][nc]
                and (cells[nr][nc] == color or cells[nr][nc] == 0)
            ):
                visited[nr][nc] = False
                q.append([nr, nc])


def store_rainbow(rainbow_set, cells):
    for i, row in enumerate(cells):
        for j, cell in enumerate(row):
            if cell == 0:
                rainbow_set.add((i, j))


def solution(cells):
    score = 0
    # 무지개블럭은 여러 일반 블록이 공유할 수 있으므로, 새로운 탐색마다 방문 체크를 해제해줘야함
    # 빠른 체크해제를 위한 좌표 저장 set
    rainbow_set = set()

    while True:
        # 무지개 블럭 위치 저장
        store_rainbow(rainbow_set, cells)
        heap = []
        visited = [[True for _ in range(N)] for _ in range(N)]
        q = deque()

        for i in range(N):
            for j in range(N):
                if visited[i][j] and cells[i][j] > 0:
                    visited[i][j] = False
                    # 무지개 블록은 다른 그룹도 사용할 수 있으므로 체크 해제
                    uncheck(visited, rainbow_set)
                    q.append([i, j])
                    # 그룹의 넓이와 rainbow 블록 개수
                    ret = get_cnt(q, visited, cells[i][j], cells)
                    # 오름차순이므로 -
                    ret.append(-i)
                    ret.append(-j)

                    heappush(heap, ret)

        # 지운 블럭 없거나 최대 그룹 크기가 1이면
        if not heap or heap[0][0] == -1:
            break

        # 탐색 끝났으면 꺼내주고
        area, rainbow_cnt, r, c = heappop(heap)

        # 점수 더해주고
        score += area**2
        # 큰 그룹 삭제하고
        remove_blocks(-r, -c, cells)
        # 중력 작용 하고
        drop(cells)
        # 돌리고
        cells = rotate(cells)
        # 다시 중력 작용
        drop(cells)
        # 블럭들 위치가 바뀌었으니 초기화
        rainbow_set.clear()

    return score


if __name__ == "__main__":
    print(solution(get_input()))

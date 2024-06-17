import sys
from collections import deque

input = sys.stdin.readline

# Magic Number
AIR = 2
CHEESE = 1
HOLE = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def get_input():
    n, m = list(map(int, input().split()))
    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return [n, m, cells]


def solution(params):
    n, m, cells = params

    def check_range(row, col):
        return 0 <= row < n and 0 <= col < m

    # 시작 시 외부 공기 채워주기
    def init():
        q = deque()
        visited = [[True for _ in range(m)] for _ in range(n)]
        visited[0][0] = False
        q.append([0, 0])

        fill_air(q, visited)

    # 공기와 맞닿아있는지 체크
    def check_air(row, col):
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if check_range(nr, nc) and cells[nr][nc] == AIR:
                return True

        return False

    # 치즈 녹이기
    def melt(remove_set):
        for coord in remove_set:
            row, col = coord
            cells[row][col] = AIR

    # 구멍에 공기 채우기
    def fill_air(q, visited):

        remove_set = set()

        while q:
            row, col = q.popleft()

            cells[row][col] = AIR
            remove_set.add((row, col))

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if check_range(nr, nc) and visited[nr][nc] and cells[nr][nc] == HOLE:
                    visited[nr][nc] = False
                    q.append([nr, nc])

        return remove_set

    cheese_set = set()
    hole_set = set()

    # 순회 횟수를 줄이기 위해 치즈와 치즈 내부 구멍의 위치를 저장합니다.
    for i, line in enumerate(cells):
        for j, cell in enumerate(line):
            if cell == CHEESE:
                cheese_set.add((i, j))
            elif cell == HOLE:
                hole_set.add((i, j))

    # 외부 공기 주입
    init()

    prev_del = 0
    cnt = 0
    while cheese_set:
        cnt += 1
        prev_del = len(cheese_set)

        # 제거된 치즈 좌표 저장
        remove_cheese_set = set()

        # 치즈 확인 후 녹이기
        for cheese in cheese_set:
            row, col = cheese

            if check_air(row, col):
                remove_cheese_set.add((row, col))

        melt(remove_cheese_set)

        # 순회 끝나면 치즈 제거
        cheese_set -= remove_cheese_set

        # 채워진 구멍 좌표 저장
        filled_set = set()
        # 구멍 확인 후 공기 채우기
        for hole in hole_set:
            row, col = hole

            if check_air(row, col):
                q = deque()
                visited = [[True for _ in range(m)] for _ in range(n)]
                q.append([row, col])
                visited[row][col] = False
                filled_set.update(fill_air(q, visited))

        # 채워진 구멍 제거
        hole_set -= filled_set

    return [cnt, prev_del]


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

import sys
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
min_d = 2500


def get_input():
    map = []

    for i in range(n):
        map.append(list(input().strip()))

    return map


def check_range(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def spread_water(q, map):
    nq = deque()

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if check_range(nr, nc) and map[nr][nc] == ".":
                nq.append([nr, nc])
                map[nr][nc] = "*"

    return nq


def move_dochi(q, map, visited):
    global min_d
    nq = deque()

    while q:
        r, c, distance = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (
                check_range(nr, nc)
                and visited[nr][nc]
                and (map[nr][nc] == "." or map[nr][nc] == "D")
            ):
                if map[nr][nc] == "D":
                    min_d = distance + 1
                    return deque()
                visited[nr][nc] = False
                nq.append([nr, nc, distance + 1])

    return nq


def solution(map):
    water_q = deque()
    dochi_q = deque()
    visited = [[True for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map[i][j] == "*":
                water_q.append([i, j])
            elif map[i][j] == "S":
                visited[i][j] = False
                dochi_q.append([i, j, 0])
                map[i][j] = "."

    while dochi_q:
        water_q = spread_water(water_q, map)
        dochi_q = move_dochi(dochi_q, map, visited)

    return min_d if min_d != 2500 else "KAKTUS"


if __name__ == "__main__":
    print(solution(get_input()))

# BOJ 16918 봄버맨
# 아.. 귀찮다..
# n^3 = 800만
# 단순하게 구현해도 됨
# 3개 패턴이 반복될 것 같은데 굳이 다 구현해야하나...?
# 패턴 만들고 돌려보자

import sys

input = sys.stdin.readline
n, m, t = list(map(int, input().split()))


def get_input():
    maps = []

    for i in range(n):
        maps.append(list(input().strip()))

    return maps


def check_range(r, c):
    if 0 <= r < n and 0 <= c < m:
        return True
    return False


def solution(maps):
    states = []
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 1초 - 초기와 같음
    # 2초 - 모두 폭탄, 모든 짝수초와 같음
    state = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append("O")
        state.append(row)
    states.append(state)

    # 3초 - 초기 폭탄 터짐
    state = []

    # 폭탄 모두 채운 뒤에
    for i in range(n):
        row = []
        for j in range(m):
            row.append("O")
        state.append(row)
    states.append(state)

    for i in range(n):
        for j in range(m):
            # 1초때 폭탄이 설치되어 있던 자리면
            if maps[i][j] == "O":
                states[1][i][j] = "."
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if check_range(nr, nc):
                        states[1][nr][nc] = "."

    # 4초 - 모든칸 폭탄 동일
    states.append(states[0])

    # 5초 3초 그림 폭탄 터짐
    state = []

    # 모든 폭탄 채운 뒤에
    for i in range(n):
        row = []
        for j in range(m):
            row.append("O")
        state.append(row)
    states.append(state)

    for i in range(n):
        for j in range(m):
            # 3초때 폭탄이 설치되어 있던 자리면
            if states[1][i][j] == "O":
                states[3][i][j] = "."
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if check_range(nr, nc):
                        states[3][nr][nc] = "."

    if t == 1:
        return maps

    # 맨처음 2초 빼고 시작
    time = t - 2

    time %= 4

    return states[time]


if __name__ == "__main__":
    print("\n".join("".join(row) for row in solution(get_input())))

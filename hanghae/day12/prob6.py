# BOJ 8911 거부기

import sys

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(input().strip())

    return params


def solution(commands):
    def forward():
        cur[0] += dv[idx][0]
        cur[1] += dv[idx][1]
        set_outline()

    def back():
        cur[0] -= dv[idx][0]
        cur[1] -= dv[idx][1]
        set_outline()

    def turn_left():
        nonlocal idx
        idx -= 1
        idx %= 4

    def turn_right():
        nonlocal idx
        idx += 1
        idx %= 4

    def set_outline():
        nonlocal min_r, min_c, max_r, max_c

        min_r = min(cur[0], min_r)
        min_c = min(cur[1], min_c)
        max_r = max(cur[0], max_r)
        max_c = max(cur[1], max_c)

    # 명령어에 따른 메서드 저장
    cmd = {"F": forward, "B": back, "L": turn_left, "R": turn_right}

    cur = [0, 0]
    dv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    idx = 0

    min_r = 0
    max_r = 0
    min_c = 0
    max_c = 0

    for command in commands:
        # 실행
        cmd[command]()

    # 넓이 구하기
    return (max_r - min_r) * (max_c - min_c)


if __name__ == "__main__":
    params = get_input()
    for param in params:
        print(solution(param))

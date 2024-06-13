# BOJ 20056 마법사 상어와 파이어볼

import sys
from collections import defaultdict

input = sys.stdin.readline
N, M, K = list(map(int, input().split()))
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def get_input():
    fireballs = []

    for _ in range(M):
        fireballs.append(list(map(int, input().split())))

    return fireballs


# 속력만큼 움직인 후 mod
def move_fireball(fireball):
    row, col, m, s, d, cnt = fireball

    row += dr[d] * s
    row %= N
    col += dc[d] * s
    col %= N

    fireball[0] = row
    fireball[1] = col


def merge_fireball(f_list):
    merged = [f_list[0][0], f_list[0][1], 0, 0, 0, 0]

    is_even = True

    start = f_list[0][4] % 2

    for fireball in f_list:
        r, c, m, s, d, cnt = fireball
        merged[2] += m
        merged[3] += s
        merged[5] += 1

        if fireball[4] % 2 != start:
            is_even = False

    if is_even:
        merged[4] = 0
    else:
        merged[4] = 1

    return merged


def divide_fireball(fireball):
    ret = []

    r, c, m, s, d, cnt = fireball

    m //= 5
    s //= cnt

    if m == 0:
        return ret

    start = 0
    if d == 1:
        start = 1

    for i in range(start, 8, 2):
        ret.append([r, c, m, s, i, 1])

    return ret


def solution(fireballs):

    # 좌표를 키로 사용하는 fireball 저장소
    info = defaultdict(list)

    for fireball in fireballs:
        # 몇 개가 merge되었는지 cnt 정보 추가
        fireball.append(1)
        row, col = fireball[0], fireball[1]
        info[(row, col)].append(fireball)

    for _ in range(K):
        # 이동/머지/분할 후의 정보 저장용
        n_info = defaultdict(list)

        # 각 좌표의 파이어볼을 이동시킨 후 저장
        for f_list in info.values():
            for fireball in f_list:
                move_fireball(fireball)
                n_info[(fireball[0], fireball[1])].append(fireball)

        # 이동한 파이어볼들 조작
        for key in n_info.keys():
            # 좌표에 파이어볼이 하나만 있다면 pass
            if len(n_info[key]) < 2:
                continue
            f_list = n_info[key]
            # 겹친 파이어볼 병합
            fireball = merge_fireball(f_list)
            # 합친 파이어볼 나누기
            n_info[key] = divide_fireball(fireball)

            if not f_list:
                del n_info[key]

        info = n_info

    total = 0

    for f_list in info.values():
        for fireball in f_list:
            total += fireball[2]

    return total


if __name__ == "__main__":
    print(solution(get_input()))

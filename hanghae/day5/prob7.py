import sys

input = sys.stdin.readline

N = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

coords = []

min_r, min_c, max_r, max_c = 500, 500, -500, -500

r, c = 0, 0

for _ in range(6):
    direction, distance = list(map(int, input().strip().split()))

    r += dr[direction - 1] * distance
    c += dc[direction - 1] * distance
    min_r = min(min_r, r)
    min_c = min(min_c, c)
    max_r = max(max_r, r)
    max_c = max(max_c, c)

    coords.append([r, c])

sqaure = (max_r - min_r) * (max_c - min_c)


def get_small_area():

    ret = [0, 0]

    prev = [0, 0]

    flag = False

    for coord in coords:
        if flag:
            idx = 0 if ret[0] == 0 else 1
            ret[idx] = abs(prev[idx] - coord[idx])

            break

        if (
            coord[0] != min_r
            and coord[0] != max_r
            and coord[1] != min_c
            and coord[1] != max_c
        ):
            ret[0] = abs(prev[0] - coord[0])
            ret[1] = abs(prev[1] - coord[1])
            flag = True

        prev = coord

    return ret[0] * ret[1]


# 최소, 최대 값이 아닌 점이 마지막에 있는 경우를 대비해 2번 반복으로 연장
coords.extend(coords)

small = get_small_area()

area = (max_r - min_r) * (max_c - min_c) - small

print(area * N)

"""
7
1 20
4 100
2 50
3 160
1 30
4 60
"""

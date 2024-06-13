# BOJ 21610 마법사 상어와 비바라기
# 구현

import sys
from collections import deque

input = sys.stdin.readline
n, m = list(map(int, input().split()))

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]


def get_input():
    params = []

    cells = []
    for _ in range(n):
        cells.append(list(map(int, input().split())))

    directions = []

    for _ in range(m):
        directions.append(list(map(int, input().split())))

    params.append(cells)
    params.append(directions)

    return params


def check_range(row, col):
    return 0 <= row < n and 0 <= col < n


def move_cloud(row, col, direction_info):
    direction, distance = direction_info
    direction -= 1

    # mod로 범위 초과 제어
    row += dr[direction] * distance
    row %= n

    col += dc[direction] * distance
    col %= n

    return [row, col]


# 구름 있는 곳에 비내리기
def raining(cloud_q, cells):
    for cloud in cloud_q:
        row, col = cloud

        cells[row][col] += 1


def copy_water(cloud_q, cells):
    while cloud_q:
        row, col = cloud_q.popleft()
        # 대각선만 검사
        for i in range(1, 8, 2):
            nr = row + dr[i]
            nc = col + dc[i]

            if check_range(nr, nc) and cells[nr][nc] > 0:
                cells[row][col] += 1


# 구름 생성
def make_clouds(cloud_q, cells, cloud_set):
    for i, row in enumerate(cells):
        for j, bucket in enumerate(row):
            # 바구니에 있는 물의 양이 2보다 많고, 직전에 구름이 있던 위치가 아니라면
            if bucket >= 2 and not tuple([i, j]) in cloud_set:
                # 물을 줄이고 구름을 q에 삽입
                cells[i][j] -= 2
                cloud_q.append([i, j])


def solution(params):
    cells, directions = params
    # 구름 정보 저장
    cloud_q = deque()
    # 초기 구름 init
    cloud_q.append([n - 1, 0])
    cloud_q.append([n - 2, 0])
    cloud_q.append([n - 1, 1])
    cloud_q.append([n - 2, 1])

    # visit 리스트 사용 시 구름 없는 공간이 많으면 메모리 낭비인듯함
    # 직전 구름 위치를 기억할 set 생성
    cloud_set = set()

    # 방향 정보만큼 실행
    for direction_info in directions:
        # q에 있는 구름의 개수만큼 구름 이동 실행
        size = len(cloud_q)
        for _ in range(size):
            row, col = cloud_q.popleft()
            # 이동시킨 구름을 q에 넣고
            cloud_q.append(move_cloud(row, col, direction_info))
            # 구름 위치 기억하기 위에 set에 추가
            cloud_set.add(tuple(cloud_q[-1]))

        # 비 내리기
        raining(cloud_q, cells)

        # 물 복사
        copy_water(cloud_q, cells)

        # 구름 재생성
        make_clouds(cloud_q, cells, cloud_set)

        # 구름 정보 지우기
        cloud_set.clear()

    total = 0

    for row in cells:
        total += sum(row)

    return total


if __name__ == "__main__":
    print(solution(get_input()))

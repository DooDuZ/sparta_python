import sys

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(m)

    houses = []

    for i in range(n):
        houses.append(int(input()))

    params.append(houses)

    return params


def solution(params):
    m, houses = params
    houses.sort()

    max_distance = 0

    # 공유기간 이격 거리가 주어졌을 때 True False 반환 함수
    def set_device(distance, device):
        # 가장 앞에는 항상 설치한다
        prev = houses[0]
        device -= 1
        for i in range(1, len(houses)):
            # 직전 설치한 집과의 거리가 주어진 거리 이상이면
            if houses[i] - prev >= distance:
                device -= 1
                prev = houses[i]

        return device <= 0

    left = 0
    # 이격 가능한 최대 거리
    # +1안하면 left가 최대 가능 거리 -1까지만 돈다
    right = houses[-1] - houses[0] + 1

    while left < right:
        mid = (left + right) // 2

        if set_device(mid, m):
            max_distance = max(mid, max_distance)
            left = mid + 1
        else:
            right = mid

    return max_distance


print(solution(get_input()))

"""
3 2
1
100
1000

"""

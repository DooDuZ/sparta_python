# BOJ 13305 주유소

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    cities = [0] + list(map(int, input().split()))
    costs = list(map(int, input().split()))

    return [n, cities, costs]


def solution(params):
    n, dist, costs = params

    # 도시 위치 = 출발점으로부터의 거리, 누적합
    for i in range(1, n):
        dist[i] += dist[i - 1]

    # 비용이 도시 인덱스와 함께 저장되도록 정보 저장
    info = []

    for i in range(n):
        info.append([dist[i], costs[i]])

    # 비용 순 정렬
    info.sort(key=lambda x: x[1])

    # 마지막 도시 -> 첫번째 도시로 역방향 진행
    # 출발점
    distance = dist[n - 1]

    total_cost = 0

    for city in info:
        location, cost = city
        # 출발점보다 값이 작은 곳에서만 기름을 넣는다
        if location >= distance:
            continue
        # 거리만큼 기름 넣어주고
        total_cost += (distance - location) * cost
        # 출발점 변경
        distance = location

    return total_cost


if __name__ == "__main__":
    print(solution(get_input()))

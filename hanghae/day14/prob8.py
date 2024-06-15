# BOJ RGB거리
"""

    R       G       B
1  cost    cost    cost
2  아... 못그리겠어요 암튼 2차원 씀
3

n번째 집을 칠할 때 비용 = 이전 집에서 현재 칠할 색을 제외한 두 색의 비용 중 작은것 + 현재 비용
"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 1_000_000


def get_input():
    n = int(input())

    houses = []

    for _ in range(n):
        houses.append(list(map(int, input().split())))

    return [n, houses]


def solution(params):
    n, houses = params

    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][0] = houses[0][0]
    dp[0][1] = houses[0][1]
    dp[0][2] = houses[0][2]

    def paint(house, color):
        # 비어있다면 채워줘요
        if dp[house][color] == INF:
            for prev_color in range(3):
                # 같은 색이면 continue
                if prev_color == color:
                    continue
                # 이전 집 색칠 비용에서 작은 값으로 갱신
                dp[house][color] = min(dp[house][color], paint(house - 1, prev_color))
            # 현재 비용 더하기
            dp[house][color] += houses[house][color]

        return dp[house][color]

    cost = 1_000_000

    for color in range(3):
        cost = min(paint(n - 1, color), cost)

    return cost


if __name__ == "__main__":
    print(solution(get_input()))

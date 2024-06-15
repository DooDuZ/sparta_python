# BOJ 9655 돌게임

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
gamer = ["CY", "SK"]


def get_input():
    return int(input())


def solution(n):
    if n == 1:
        return gamer[1]
    elif n == 2:
        return gamer[0]

    # -1 승패 없음
    # 게임을 끝내는데 필요한 최소 턴 수 를 저장
    dp = [-1 for _ in range(n + 1)]
    # 2%n == 1이면 상근 승
    # 1번의 턴으로 게임을 승리함
    dp[1] = 1
    dp[3] = 1

    # top down
    # 3개 뺀 경우 vs 1개 뺀 경우에서 작은값에 + 1
    def set_dp(n):
        if dp[n] == -1:
            dp[n] = set_dp(n - 1)
            if n > 3:
                dp[n] = min(dp[n], set_dp(n - 3))

            dp[n] += 1

        return dp[n]

    """
    # bottom up
    def set_dp(n):
        for i in range(1, n + 1):
            if dp[i] != -1:
                continue

            dp[i] = dp[i - 1]

            if i > 3:
                dp[i] = min(dp[i - 3], dp[i])

            dp[i] += 1
    """

    return gamer[set_dp(n) % 2]


if __name__ == "__main__":
    print(solution(get_input()))

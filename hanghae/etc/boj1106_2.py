# BOJ 1106 호텔

import sys

input = sys.stdin.readline


def get_input():
    c, m = list(map(int, input().split()))

    ad_table = []

    for _ in range(m):
        ad_table.append(list(map(int, input().split())))

    return [c, m, ad_table]


def solution(params):
    INF = 1000000000
    c, m, ad_table = params

    # index = guest 수
    # value = 최소 비용
    dp = [INF for _ in range(c + 1)]
    dp[0] = 0

    for ad in ad_table:
        cost, guest = ad

        for j in range(c + 1):
            if j - guest < 0:
                dp[j] = min(dp[j], cost)
                continue
            dp[j] = min(dp[j], dp[j - guest] + cost)

    return dp[c]


if __name__ == "__main__":
    print(solution(get_input()))

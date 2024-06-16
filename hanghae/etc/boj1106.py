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
    c, m, ad_table = params

    # index = cost
    # value = 해당 cost로 얻을 수 있는 guest의 수
    # 매우 비효율적
    dp = [0 for _ in range(100001)]

    for ad in ad_table:
        cost, guest = ad

        for j in range(1, 100001):
            if j - cost < 0:
                continue

            if dp[j - cost] + guest > dp[j]:
                dp[j] = dp[j - cost] + guest

    for i, total_guest in enumerate(dp):
        if total_guest >= c:
            return i


if __name__ == "__main__":
    print(solution(get_input()))

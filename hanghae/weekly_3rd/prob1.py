# BOJ 9465 스티커

import sys

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for i in range(T):
        n = int(input())
        sticker = []

        for _ in range(2):
            sticker.append(list(map(int, input().split())))

        params.append([n, sticker])

    return params


def solution(params):
    n, sticker = params

    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1] + sticker[0][i], dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1] + sticker[1][i], dp[1][i - 1])

    return max(max(dp[0]), max(dp[1]))


if __name__ == "__main__":
    params = get_input()
    for param in params:
        print(solution(param))


"""
1
10
1 2 3 4 5 1 2 3 4 5
1 3 5 7 9 1 3 5 7 9
"""

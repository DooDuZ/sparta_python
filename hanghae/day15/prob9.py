# BOJ 2156 포도주 시식

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    wines = [0]

    for _ in range(n):
        wines.append(int(input()))

    return [n, wines]


def solution(params):
    n, wines = params

    if n == 1:
        return wines[1]

    dp = [0 for _ in range(n + 1)]
    dp[1] = wines[1]
    dp[2] = wines[2] + wines[1]

    for i in range(3, n + 1):
        dp[i] = max(max(wines[i - 1] + dp[i - 3], dp[i - 2]) + wines[i], dp[i - 1])

    return dp[n]


if __name__ == "__main__":
    print(solution(get_input()))

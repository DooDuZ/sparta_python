# BOJ 1699 제곱수의 합
import sys
import math

input = sys.stdin.readline


def get_input():
    return int(input())


def solution(number):

    dp = [0 for _ in range(100001)]

    for i in range(1, number + 1):
        dp[i] = i
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)

    return dp[number]


if __name__ == "__main__":
    print(solution(get_input()))

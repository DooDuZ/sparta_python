import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get_input():
    n, price = list(map(int, input().split()))

    coins = []

    for _ in range(n):
        coins.append(int(input()))

    return [n, coins, price]


def solution(params):
    n, coins, price = params

    # 금액 최대 10000까지
    dp = [0 for _ in range(10001)]
    dp[0] = 1

    for coin in coins:
        for i in range(price + 1):
            if i - coin < 0:
                continue
            dp[i] += dp[i - coin]

    return dp[price]


if __name__ == "__main__":
    print(solution(get_input()))

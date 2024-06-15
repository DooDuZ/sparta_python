import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        n = int(input())
        coins = list(map(int, input().split()))
        price = int(input())

        params.append([n, coins, price])

    return params


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
    params = get_input()
    for param in params:
        print(solution(param))


"""
1
2
1 2
10

"""

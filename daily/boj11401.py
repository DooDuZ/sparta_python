# BOJ 11401 이항 계수 3
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

MOD = 1_000_000_007


def get_input():
    return list(map(int, input().split()))


def solution(params):
    def factorial(number):
        ret = 1

        while number > 1:
            ret = (ret * number) % MOD
            number -= 1

        return ret

    def pow(number, index):
        ret = 1

        while index > 0:
            if index % 2 == 1:
                ret *= number
                ret %= MOD
            number *= number
            number %= MOD
            index //= 2

        return ret

    n, k = params

    dp = [0 for _ in range(n + 1)]

    dp[0] = 1
    dp[1] = 1

    top = factorial(n) % MOD
    bottom = factorial(k) * factorial(n - k) % MOD

    # 페르마 소정리라고 합니다... 수학 싫다!
    return top * pow(bottom, MOD - 2) % MOD


if __name__ == "__main__":
    print(solution(get_input()))

# BOJ 11726 2xn 타일링
# 넓이가 1인 도형과 2인 도형으로 n의 넓이를 채우는 문제와 같다
# 넓이가 3인 도형을 만드는 경우의 수 1 1 1, 1 2 , 2 1
# 문제를 작게 나눠보면
# -> 넓이가 2인 도형에서 1을 더하는 경우
# -> 넓이가 1인 도형에서 2를 더하는 경우
# 따라서 3을 만드는 경우의 수는 1에서 2 더하기, 2에서 1더하기의 경우를 합친 것과 같다. 도형의 넓이가 2개뿐이기 때문에 다른 경우의 수는 없음
# 1에서 2를 더하는 경우 = 1 + (1+1), 1 + 2
# 2에서 1을 더하는 경우 = 2 + 1
#   -> 여기서 1+2를 하지 않는 이유는, n-2항에서 이미 구해지기 때문이다.
#   -> 즉, 값이 왼쪽에 추가되는 경우는 고려할 필요가 없다.
# a(n) = a(n-2) + a(n-1) -> 피보나치

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline
MOD = 10007


def get_input():
    return int(input())


def solution(n):

    dp = [0 for _ in range(n + 2)]
    # 1,2의 값은 결정되어있음
    dp[1] = 1
    dp[2] = 2

    def fibonacci(n):
        if dp[n] == 0:
            dp[n] = (fibonacci(n - 1) + fibonacci(n - 2)) % MOD
        return dp[n]

    return fibonacci(n)


if __name__ == "__main__":
    print(solution(get_input()))

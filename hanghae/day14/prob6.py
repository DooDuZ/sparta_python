# BOJ 2938 설탕 배달

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def get_input():
    return int(input())


def solution(weight):

    # 충분히 큰 수 2000
    dp = [2000 for _ in range(5001)]
    dp[3] = dp[5] = 1
    # 만들 수 없는 무게에 index에러 방지
    # 2001로 올려서 진입 못하게 막아주기
    dp[1] = dp[2] = dp[4] = 2001

    # 만들고 싶은 무게에서 1 혹은 3을 뺀 값 중 작은 값을 가져와서 1을 더해준다
    def set_dp(w):
        if dp[w] == 2000:
            dp[w] = min(set_dp(w - 3), set_dp(w - 5)) + 1

        return dp[w]

    return dp[weight] if set_dp(weight) < 2000 else -1


if __name__ == "__main__":
    print(solution(get_input()))

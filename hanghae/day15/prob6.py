# BOJ 2512 예산

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    requests = list(map(int, input().split()))

    total = int(input())

    return [n, requests, total]


def solution(params):
    n, requests, total = params

    # 예산 분배 가능 여부 체크
    def divide_budget(maximum, total_cost):

        for request in requests:
            if request >= maximum:
                total_cost -= maximum
            else:
                total_cost -= request

        if total_cost >= 0:
            return True

        return False

    # 이분 탐색으로 상한선 찾기
    def binary_search():
        left = 0
        right = 1_000_000_000

        while left <= right:
            mid = (left + right) // 2

            if divide_budget(mid, total):
                left = mid + 1
            else:
                right = mid - 1

        return left

    upper_limit = binary_search() - 1

    # 요청 최대값과 상한선 중 작은값 return
    return min(upper_limit, max(requests))


if __name__ == "__main__":
    print(solution(get_input()))

# BOJ 2565 전깃줄
# LIS문제

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    cables = []

    for i in range(n):
        cables.append(list(map(int, input().split())))

    return [n, cables]


def solution(params):
    def binary_search(target):
        left = 1
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if dp[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    n, numbers = params

    # 출발 전봇대 기준 정렬
    numbers.sort()

    # 가능한 부분수열의 최대 길이는 n이다
    # dp[i]에 들어가는 값은 부분 수열의 i위치에 올 수 있는 최소값
    dp = [501 for _ in range(n + 1)]

    # dp에 업데이트되는 가장 큰 인덱스를 저장한다
    maximum = 0

    # 숫자가 가장 많이 증가하는 부분 수열의 길이를 찾으면 그게 최대 전깃줄의 개수다
    for number in numbers:
        index = binary_search(number[1])
        dp[index] = number[1]
        maximum = max(maximum, index)

    return n - maximum


if __name__ == "__main__":
    print(solution(get_input()))

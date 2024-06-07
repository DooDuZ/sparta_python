# BOJ 10815 숫자 카드
# 이분탐색 굳이굳이 쓰자면...

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    return [numbers, targets]


def solution(params):
    answer = []
    numbers, targets = params

    numbers.sort()

    def binary_search(target):
        left, right = 0, len(numbers) - 1

        while left <= right:
            mid = (left + right) // 2

            if numbers[mid] == target:
                return 1
            elif numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0

    for target in targets:
        answer.append(binary_search(target))

    return answer


print(*solution(get_input()))

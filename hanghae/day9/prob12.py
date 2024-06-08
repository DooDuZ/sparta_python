import sys

input = sys.stdin.readline


def get_input():
    return int(input())


def solution(n):
    # 1씩 증가한 횟수 세기
    target = 2 * n

    def get_cnt(mid):
        return mid * mid + mid

    def binary_search():
        left = 0
        right = (10**100) * 2

        while left < right:
            mid = (left + right) // 2

            if get_cnt(mid) < target:
                left = mid + 1
            else:
                right = mid

        return left

    return target - binary_search()


print(solution(get_input()))

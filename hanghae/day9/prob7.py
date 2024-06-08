import sys

input = sys.stdin.readline


def get_input():
    return list(map(int, input().split()))


def solution(params):
    x, y = params

    z = int(y * 100 / x)

    if x == y or z == 99:
        return -1

    def binary_search():
        left = 0
        right = 1000000000

        while left < right:
            mid = (left + right) // 2

            if get_rate(mid) < z + 1:
                left = mid + 1
            else:
                right = mid

        return left

    def get_rate(n):
        return int((y + n) * 100 / (x + n))

    return binary_search()


print(solution(get_input()))

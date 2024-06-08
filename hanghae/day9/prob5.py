import sys

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        params.append(int(input()))

    return params


def solution(params):
    answer = []

    def binary_search(lng):
        left = 1
        right = lng

        if lng == 1:
            return 1

        while left < right:
            mid = (left + right) // 2

            if get_jumps(mid) <= lng:
                left = mid + 1
            else:
                right = mid

        return left - 1

    def get_jumps(n):
        total = (n + 1) * (n // 2)
        if n % 2 == 1:
            total += n // 2 + 1

        return total

    for param in params:
        answer.append(str(binary_search(param)))

    return answer


print("\n".join(solution(get_input())))

# 20240620
# BOJ 2473 세 용액

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())
    numbers = list(map(int, input().split()))

    return [n, numbers]


# test add
def solution(params):
    def binary_search(target, visited):
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            if liquids[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        value = 3000000001
        idx = left

        for i in range(-1, 2):
            cur = left + i
            if cur % n in visited:
                continue

            if abs(target - liquids[cur % n]) < value:
                idx = cur % n
                value = abs(target - liquids[cur % n])

        return idx

    n, liquids = params
    liquids.sort()

    min_abs = 3_000_000_000

    answer = [0, 0, 0]

    for i in range(n):
        for j in range(i + 1, n):
            visited = {i, j}
            idx = binary_search(-(liquids[i] + liquids[j]), visited)

            if abs(liquids[i] + liquids[j] + liquids[idx]) < min_abs:
                min_abs = abs(liquids[i] + liquids[j] + liquids[idx])
                answer = [liquids[i], liquids[j], liquids[idx]]

    answer.sort()

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

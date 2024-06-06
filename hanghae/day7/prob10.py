import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))
    params.append(n)
    params.append(m)
    params.append(list(map(int, input().split())))

    return params


# 단순 구현
def solution(params):
    n, m, numbers = params

    heapify(numbers)

    for _ in range(m):
        num = heappop(numbers) + heappop(numbers)
        for _ in range(2):
            heappush(numbers, num)

    return sum(numbers)


print(solution(get_input()))

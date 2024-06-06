import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(int(input()))

    return params


def solution(numbers):
    heapify(numbers)

    # 비교 누적
    cnt = 0

    while len(numbers) > 1:
        # 섞고
        num = heappop(numbers) + heappop(numbers)
        cnt += num
        # 섞은 더미를 다시 넣어준다
        heappush(numbers, num)

    return cnt


print(solution(get_input()))

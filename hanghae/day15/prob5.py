# BOJ 11047 동전0
# 모든 동전은 가장 작은 동전의 배수임... 조건 확인 잘하고 풀자

import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    n, target = list(map(int, input().split()))
    coins = []

    for _ in range(n):
        coins.append(int(input()))

    return [n, target, coins]


def solution(params):

    n, target, coins = params

    max_heap = []

    for coin in coins:
        heappush(max_heap, -coin)

    cnt = 0

    # 모든 동전은 최소 동전의 배수이므로, 큰 동전을 최대한 빼면서 진행
    while target != 0 and max_heap:
        if -max_heap[0] > target:
            heappop(max_heap)
            continue

        cnt += target // -max_heap[0]
        target %= -max_heap[0]

    return cnt


if __name__ == "__main__":
    print(solution(get_input()))


"""
2 4200
500
1200

"""

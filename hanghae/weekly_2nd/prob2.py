import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        n = int(input())
        params.append(list(map(int, input().split())))

    return params


def get_cost(files):
    heapify(files)

    total = 0
    while len(files) >= 2:
        file = 0
        for _ in range(2):
            file += heappop(files)

        total += file
        heappush(files, file)

    return total


def solution(params):
    answer = []

    for param in params:
        answer.append(get_cost(param))

    return answer


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

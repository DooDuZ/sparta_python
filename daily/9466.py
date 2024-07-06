# BOJ 9466 텀 프로젝트

import sys

input = sys.stdin.readline


def get_input():
    T = int(input())

    params = []

    for _ in range(T):
        n = int(input())
        wish = [0] + list(map(int, input().split()))
        params.append([n, wish])

    return params


def solution(params):
    n, wish = params

    visited = [True] + [False for _ in range(n)]

    for i in range(1, n + 1):
        if visited[i]:
            continue

        up_set = set()
        down_set = set()

        v = i

        while not visited[v]:
            up_set.add(v)
            down_set.add(wish[v])
            visited[v] = True
            v = wish[v]

        if up_set != down_set:
            for s in up_set:
                visited[s] = False

    total = 0
    for v in visited:
        if not v:
            total += 1

    return total


if __name__ == "__main__":
    for c in get_input():
        print(solution(c))

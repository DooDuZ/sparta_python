import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    return list(map(int, input().split()))


def check_range(v):
    if 0 <= v <= 100000:
        return True
    return False


def bfs(q, visited, k):

    while q:
        v, d = q.popleft()

        if v == k:
            return d

        if check_range(v - 1) and visited[v - 1]:
            visited[v - 1] = False
            q.append([v - 1, d + 1])

        if check_range(v + 1) and visited[v + 1]:
            visited[v + 1] = False
            q.append([v + 1, d + 1])

        if check_range(v * 2) and visited[v * 2]:
            visited[v * 2] = False
            q.append([v * 2, d + 1])


def solution(params):
    n, k = params

    q = deque()
    visited = [True for _ in range(100001)]

    visited[n] = False
    q.append([n, 0])

    return bfs(q, visited, k)


if __name__ == "__main__":
    print(solution(get_input()))

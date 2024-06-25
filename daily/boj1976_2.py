# BOJ 1976 여행계획

import sys
from collections import deque

input = sys.stdin.readline


def get_input():

    n = int(input())
    m = int(input())

    edges = [list(map(int, input().split())) for _ in range(n)]

    path = list(map(int, input().split()))

    return [n, m, edges, path]


def solution(params):

    n, m, edges, path = params

    # for i in range(n):
    # edges[i][i] = 1

    def bfs():
        visited = [True for _ in range(n + 1)]
        q = deque()

        q.append(path[0])
        visited[path[0]] = False
        visited[0] = False

        while q:
            cur = q.popleft()

            for i in range(n):
                if edges[cur - 1][i] == 1 and visited[i + 1]:
                    visited[i + 1] = False
                    q.append(i + 1)

        return visited

    visited = bfs()

    for c in path:
        if visited[c]:
            return "NO"

    return "YES"


if __name__ == "__main__":
    print(solution(get_input()))


"""
2
2
0 1
0 0
2 2

"""

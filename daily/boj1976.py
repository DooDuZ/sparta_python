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

    # 왜 82퍼에서 틀리지... 인접 리스트로 바꿔보자

    edgelist = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if edges[i][j] == 1:
                edgelist[i].append(j)
                edgelist[j].append(i)

    def bfs():
        visited = [True for _ in range(n)]
        q = deque()

        q.append(path[0] - 1)
        visited[path[0] - 1] = False

        while q:
            cur = q.popleft()

            for e in edgelist[cur]:
                if visited[e]:
                    visited[e] = False
                    q.append(e)

        return visited

    v = bfs()

    for c in path:
        if v[c - 1]:
            return "NO"

    return "YES"


if __name__ == "__main__":
    print(solution(get_input()))

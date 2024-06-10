import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    edge_input = []

    for _ in range(n - 1):
        edge_input.append(list(map(int, input().split())))

    pairs = []

    for _ in range(m):
        pairs.append(list(map(int, input().split())))

    params.append(n)
    params.append(edge_input)
    params.append(pairs)

    return params


# 간선 입력 받기
def get_edges(n, edge_input):
    edges = [[] for _ in range(n + 1)]

    for edge in edge_input:
        start, end, cost = edge
        edges[start].append([end, cost])
        edges[end].append([start, cost])

    return edges


def bfs(n, edges, start, end):
    q = deque()
    visited = [True for _ in range(n + 1)]
    visited[start] = False
    q.append([start, 0])

    while q:
        v, c = q.popleft()

        if v == end:
            return c

        for edge in edges[v]:
            nv, cost = edge
            if visited[nv]:
                visited[nv] = False
                q.append([nv, c + cost])


def solution(params):
    answer = []
    n, edge_input, pairs = params

    edges = get_edges(n, edge_input)

    for pair in pairs:
        answer.append(bfs(n, edges, pair[0], pair[1]))

    return answer


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

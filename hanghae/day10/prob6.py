# BOJ 2606

import sys

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())
    m = int(input())

    params.append(n)
    params.append(m)

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    params.append(edges)

    return params


def get_edges(n, edge_input):
    ret = [[] for _ in range(n + 1)]

    # 양방향 간선
    for edge in edge_input:
        start, end = edge

        ret[start].append(end)
        ret[end].append(start)

    return ret


def dfs(v, edges, visited):
    total = 0

    for nv in edges[v]:
        # 방문하지 않은 노드인 경우 체크 후 이동
        if visited[nv]:
            visited[nv] = False
            total += dfs(nv, edges, visited)

    # 방문한 노드 수 + 현재 노드 리턴
    return total + 1


def solution(params):
    n, m, edge_input = params

    edges = get_edges(n, edge_input)
    visited = [True for _ in range(n + 1)]
    visited[1] = False

    return dfs(1, edges, visited) - 1


if __name__ == "__main__":
    print(solution(get_input()))

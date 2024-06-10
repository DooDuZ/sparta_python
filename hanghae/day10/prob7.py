import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(n)

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    params.append(edges)

    params.append(int(input()))

    return params


# 인접 리스트 생성
def get_edges(n, edge_input):
    edges = [[] for _ in range(n + 1)]

    for edge in edge_input:
        prev, task = edge
        edges[task].append(prev)

    return edges


def bfs(n, edges, start):
    q = deque()
    visited = [True for _ in range(n + 1)]
    visited[start] = False
    q.append(start)

    # 방문한 노드 수 저장
    cnt = 0

    while q:
        v = q.popleft()
        cnt += 1

        for nv in edges[v]:
            # 방문하지 않은 노드만 q에 추가
            if visited[nv]:
                visited[nv] = False
                q.append(nv)

    # 출발점 카운트 차감
    return cnt - 1


def solution(params):
    n, edge_input, start = params
    edges = get_edges(n, edge_input)

    return bfs(n, edges, start)


if __name__ == "__main__":
    print(solution(get_input()))

# BOJ 18352 특정 거리의 도시 찾기

import sys
from collections import deque

input = sys.stdin.readline


# 입력 받기
def get_input():
    params = []

    params.append(list(map(int, input().split())))

    edges = []

    for _ in range(params[0][1]):
        edges.append(list(map(int, input().split())))

    params.append(edges)

    return params


def solution(params):

    n, m, k, x = params[0]

    # 인접 리스트 만들기
    def get_edges():
        ret = [[] for _ in range(n + 1)]

        for edge in params[1]:
            start, end = edge

            ret[start].append(end)

        return ret

    def bfs():
        q = deque()
        visited = [True for _ in range(n + 1)]

        q.append([x, 0])
        visited[x] = False

        edges = get_edges()

        cities = []

        while q:
            visit, distance = q.popleft()

            # 거리가 k면 도시 저장하고 continue
            if distance == k:
                cities.append(visit)
                continue

            for edge in edges[visit]:
                if visited[edge]:
                    visited[edge] = False
                    q.append([edge, distance + 1])

        # 도시 목록이 비었으면 -1
        if not cities:
            cities.append(-1)

        cities.sort()

        return cities

    return bfs()


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

# 멘토님 추천 문제
# BOJ 1939 중량 제한
# binary search 사용

import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(n)

    edges = [[] for _ in range(n)]

    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        a -= 1
        b -= 1

        edges[a].append([b, c])
        edges[b].append([a, c])

    p1, p2 = list(map(int, input().split()))

    params.append(p1 - 1)
    params.append(p2 - 1)
    params.append(edges)

    return params


def solution(params):
    # p1 출발지 p2 목적지
    n, p1, p2, edges = params

    def bfs(weight):
        q = deque()
        visited = [True for _ in range(n)]

        # 출발지 넣고 시작
        q.append(p1)
        visited[p1] = False

        while q:
            v = q.popleft()

            # 도착점이면 True return
            if v == p2:
                return True

            for edge in edges[v]:
                nv, nw = edge
                # 다리 제한 중량이 현재 무게보다 크거나 같으면 넘어가기
                if visited[nv] and nw >= weight:
                    visited[nv] = False
                    q.append(nv)
        # 도착점 못갔으면 False return
        return False

    def binary_search():
        left = 1
        right = 1_000_000_000

        while left <= right:
            mid = (left + right) // 2

            if bfs(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left

    return binary_search() - 1


print(solution(get_input()))

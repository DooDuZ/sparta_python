# BOJ 10282 해커
# 바이러스의 전파 시간 = 최단 비용과 같다


import sys
from heapq import *

input = sys.stdin.readline
INF = 1_000_000_000


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        n, d, c = list(map(int, input().split()))
        # 1인덱스 사용
        edges = [[] for _ in range(n + 1)]

        for _ in range(d):
            child, parent, cost = list(map(int, input().split()))
            # heapq 사용 할 예정이므로 코스트를 앞으로
            edges[parent].append([cost, child])
        params.append([n, d, c, edges])

    return params


def solution(param):
    n, d, c, edges = param
    dist = [INF for _ in range(n + 1)]

    def dijkstra():
        heap = [[0, c]]
        dist[c] = 0

        while heap:
            cost, visit = heappop(heap)

            # 갱신 정보와 인입 정보가 다른 경우 최단 거리가 아니다
            if dist[visit] != cost:
                continue

            for edge in edges[visit]:
                # 간서 꺼내고
                nc, nv = edge
                # 현재비용 + 다음 노드까지의 비용이 기록된 최소비용보다 작다면 힙에 추가
                if cost + nc < dist[nv]:
                    dist[nv] = cost + nc
                    heappush(heap, [cost + nc, nv])

    # 최단 경로 세팅
    dijkstra()

    # 마지막 컴퓨터가 감염된 시간이 총 비용
    total_cost = 0
    # INF는 감염되지 않은 컴퓨터, 아닌 값만 카운트
    cnt = 0
    for d in dist:
        if d == INF:
            continue
        cnt += 1
        total_cost = max(d, total_cost)

    return [cnt, total_cost]


if __name__ == "__main__":
    params = get_input()
    for param in params:
        print(*solution(param))

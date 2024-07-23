# BOJ 7579 앱
# 메모리 초과
# 당연하다... 추적 과정이 너무 비효율 적임
# 사실상 dfs 백트래킹 풀이와 다를 바 없는데 메모리만 한참 더 사용했음

import sys
from heapq import *

input = sys.stdin.readline

INF = 1_000_000_000


def get_input():

    n, m = list(map(int, input().split()))

    in_memory = list(map(int, input().split()))

    costs = list(map(int, input().split()))

    return [n, m, in_memory, costs]


def solution(params):
    def get_edges():
        ret = [[] for _ in range(n)]

        for i in range(n):
            edge_list = ret[i]
            for j in range(n):
                if i == j:
                    edge_list.append(0)
                    continue
                edge_list.append(costs[j])

        return ret

    def dijkstra():
        heap = []
        min_cost = INF

        visited = set()

        for i in range(n):
            tup = tuple([i])
            heappush(heap, [costs[i], i, memory[i], tup])
            visited.add(tup)

        while heap:
            cost, visit, total, sequence = heappop(heap)

            # print(heap)

            s = set(sequence)

            if cost >= min_cost:
                continue

            if total >= m:
                min_cost = min(min_cost, cost)

            # print(sequence, total, cost, min_cost)

            for nv, nc in enumerate(edges[visit]):
                s.add(nv)
                ns = tuple(sorted(list(s)))
                s.remove(nv)
                if ns in visited:
                    continue

                visited.add(ns)

                c = nc + cost
                if min_cost > c:
                    heappush(
                        heap,
                        [c, nv, total + memory[nv], ns],
                    )

        return min_cost

    n, m, memory, costs = params

    edges = get_edges()

    return dijkstra()


if __name__ == "__main__":
    print(solution(get_input()))

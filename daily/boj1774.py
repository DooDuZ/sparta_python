# BOJ 1774 우주신과의 교감

import sys
from heapq import *

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    positions = [[0, 0]]

    for _ in range(n):
        positions.append(list(map(int, input().split())))

    connections = [set() for _ in range(n + 1)]

    for _ in range(m):
        s, e = list(map(int, input().split()))
        connections[s].add(e)
        connections[e].add(s)

    return [n, m, positions, connections]


def solution(params):
    n, m, positions, connections = params

    def get_distance(start, end):
        s_x, s_y = start
        e_x, e_y = end

        return (abs(s_x - e_x) ** 2 + abs(s_y - e_y) ** 2) ** (1 / 2)

    def prim():
        visited = [False for _ in range(n + 1)]

        visited[0] = True
        heap = [[0, 1]]
        total = 0

        for i in range(1, n + 1):
            while heap and visited[heap[0][1]]:
                heappop(heap)

            cost, visit = heappop(heap)

            visited[visit] = True
            total += cost

            for j in range(1, n + 1):
                if visited[j]:
                    continue

                distance = get_distance(positions[visit], positions[j])

                if j in connections[visit]:
                    distance = 0

                heappush(heap, [distance, j])

        return total

    return prim()


if __name__ == "__main__":
    print(format(solution(get_input()), ".2f"))

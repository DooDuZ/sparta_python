# BOJ 28707 배열 정렬
import sys
from heapq import *

input = sys.stdin.readline

INF = 1_000_000_000


def get_input():

    n = int(input())

    arr = list(map(int, input().split()))

    m = int(input())

    edges = []

    for _ in range(m):
        s, e, c = list(map(int, input().split()))
        edges.append([s - 1, e - 1, c])

    return [n, m, arr, edges]


def solution(params):
    def is_sorted(arr):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def dijkstra():
        heap = []
        visited = set()

        heap.append([0, tuple(numbers)])

        while heap:
            cost, state = heappop(heap)

            if tuple(state) in visited:
                continue

            # print(state)

            visited.add(tuple(state))

            if is_sorted(state):
                return cost

            for e in edges:
                s, e, c = e
                next_state = list(state)
                tmp = next_state[e]
                next_state[e] = next_state[s]
                next_state[s] = tmp

                heappush(heap, [cost + c, tuple(next_state)])

        return -1

    n, m, numbers, edges = params

    return dijkstra()


if __name__ == "__main__":
    print(solution(get_input()))

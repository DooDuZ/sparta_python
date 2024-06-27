import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    n = int(input())
    m = int(input())

    edges = [[] for _ in range(n)]

    for _ in range(m):
        s, e, c = list(map(int, input().split()))
        s -= 1
        e -= 1
        edges[s].append([e, c])
        edges[e].append([s, c])

    return [n, m, edges]


def solution(params):

    n, m, edges = params

    def prim():
        # 간선 비용 총합
        total = 0

        heap = []
        visited = [True for _ in range(n)]

        # 임의의 노드에서 출발, 어디든 상관 없음
        heappush(heap, [0, 0])

        for i in range(n):
            # 이미 방문처리된 노드라면 pop해줍니다
            while heap and not visited[heap[0][1]]:
                heappop(heap)

            # 현재 방문한 노드로의 비용, 방문한 노드
            c, v = heappop(heap)

            # 방문 처리
            visited[v] = False
            # 총 비용에 현재 간선의 비용을 더해줍니다
            total += c

            # 방문한 노드의 간선을 순회
            for edge in edges[v]:
                nv, nc = edge
                # 방문하지 않은 노드로 가는 간선이라면 추가해줍니다
                if visited[nv]:
                    heappush(heap, [nc, nv])

        return total

    return prim()


if __name__ == "__main__":
    print(solution(get_input()))

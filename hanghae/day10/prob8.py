import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


# 입력 받기
def get_input():
    params = []

    n, m = list(map(int, input().split()))

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    s = int(input())

    params.append(n)
    params.append(edges)
    params.append(list(map(int, input().split())))

    return params


# 인접 리스트 생성
def get_edges(n, edge_input):
    edges = [[] for _ in range(n + 1)]

    for edge in edge_input:
        start, end = edge
        edges[start].append(end)

    return edges


# 재귀로 구현 시 RecursionError 발생
# sys.setrecursionlimit(10**6) 깊이 제한 풀어주기
def dfs(v, edges, visited, stop_set):
    # 열성팬의 잠복 지점이면 false
    if v in stop_set:
        return False

    # 리프노드인지 체크
    is_leaf = True

    for nv in edges[v]:
        if visited[nv]:
            visited[nv] = False
            is_leaf = dfs(nv, edges, visited, stop_set)
            # 리프노드에 도달했다면 탐색 중지
            # break 없이 추가 탐색 시 다른 경로에서 열성 팬을 만날 수 있음
            if is_leaf:
                break

    return is_leaf


def solution(params):
    n, edge_input, stop_point = params

    edges = get_edges(n, edge_input)
    visited = [True for _ in range(n + 1)]
    stop_set = set(stop_point)

    if dfs(1, edges, visited, stop_set):
        return "yes"
    else:
        return "Yes"


if __name__ == "__main__":
    print(solution(get_input()))

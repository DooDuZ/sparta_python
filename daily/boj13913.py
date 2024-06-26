# BOJ 13913 숨바꼭질 4
import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))

    return [n, m]


def solution(params):
    n, m = params
    visited = [0 for _ in range(100001)]

    def check_range(number):
        return 0 <= number <= 100000

    def bfs():
        q = deque()
        visited[n] = False
        q.append([n, 0])

        while q:
            idx, distance = q.popleft()

            if check_range(idx - 1) and visited[idx - 1] == 0:
                visited[idx - 1] = distance + 1
                q.append([idx - 1, distance + 1])

            if check_range(idx + 1) and visited[idx + 1] == 0:
                visited[idx + 1] = distance + 1
                q.append([idx + 1, distance + 1])

            if check_range(idx * 2) and visited[idx * 2] == 0:
                visited[idx * 2] = distance + 1
                q.append([idx * 2, distance + 1])

    bfs()
    visited[n] = 0

    ans = visited[m]
    arr = []

    cur = m

    cnt = 0

    n_visited = [True for _ in range(100001)]
    n_visited[cur] = False

    while cnt != ans:
        cnt += 1
        arr.append(cur)
        nxt_idx = -1

        # print(check_range(cur - 1), visited[cur - 1] == cnt + 1, n_visited[cur - 1])
        if (
            check_range(cur - 1)
            and visited[cur - 1] == ans - cnt
            and n_visited[cur - 1]
        ):
            n_visited[cur - 1] = False
            nxt_idx = cur - 1

        if (
            check_range(cur + 1)
            and visited[cur + 1] == ans - cnt
            and n_visited[cur + 1]
        ):
            n_visited[cur + 1] = False
            nxt_idx = cur + 1

        if cur % 2 == 0:
            if (
                check_range(cur // 2)
                and visited[cur // 2] == ans - cnt
                and n_visited[cur // 2]
            ):
                n_visited[cur // 2] = False
                nxt_idx = cur // 2

        cur = nxt_idx

    arr.append(n)

    return [ans, arr[::-1]]


if __name__ == "__main__":
    cnt, arr = solution(get_input())
    print(cnt)
    print(*arr)

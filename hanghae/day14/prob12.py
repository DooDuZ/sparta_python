# BOJ 1520 내리막길
# 모든 길을 탐색할 필요없음
# 탐색한 곳이라면 메모이제이션한 값 사용

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def get_input():
    n, m = list(map(int, input().split()))

    cells = []

    for _ in range(n):
        cells.append(list(map(int, input().split())))

    return [n, m, cells]


def solution(params):
    n, m, cells = params

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    dp = [[-1 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    def check_range(row, col):
        return 0 <= row < n and 0 <= col < m

    # 도착지에서 출발점으로 역방향
    def dfs(row, col):
        # print(row, col)
        # 방문 표시
        dp[row][col] = 0

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            # 역방향이므로 높은 곳으로 간다.
            if check_range(nr, nc) and cells[nr][nc] > cells[row][col]:
                if dp[nr][nc] == -1:
                    dp[row][col] += dfs(nr, nc)
                else:
                    dp[row][col] += dp[nr][nc]

        return dp[row][col]

    dfs(n - 1, m - 1)

    return dp[n - 1][m - 1]


if __name__ == "__main__":
    print(solution(get_input()))

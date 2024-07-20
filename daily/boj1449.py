#BOJ 1449 수리공 항승

import sys

input = sys.stdin.readline


def get_input():

    n,m = list(map(int, input().split()))

    points = list(map(int, input().split()))

    return [n, m, points]

def solution(params):
    n, m, points = params

    maximum = max(points)

    visited = [False for _ in range(maximum+1)]

    cnt = 0

    for i in range(1,maximum+1):
        if i in points and not visited[i]:

            for j in range(i, min(i+m, maximum+1)):

                visited[j] = True
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(solution(get_input()))

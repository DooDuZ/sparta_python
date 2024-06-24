# boj 1027 고층 건물 완료

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())
    buildings = list(map(int, input().split()))

    return [n, buildings]


def solution(params):
    n, buildings = params

    def check_range(idx):
        return 0 <= idx < n

    def get_visible_cnt(start_idx):
        direction = [1, -1]

        cnt = 0

        for i in range(2):
            n_idx = start_idx + direction[i]
            while check_range(n_idx):
                if can_see(start_idx, n_idx, direction[i]):
                    cnt += 1
                n_idx += direction[i]

        return cnt

    def can_see(start, end, direction):
        dx = (buildings[start] - buildings[end]) / (start - end)

        for i in range(start + direction, end, direction):
            if buildings[i] >= buildings[start] + dx * (i - start):
                return False
        return True

    max_cnt = 0

    for i in range(n):
        max_cnt = max(get_visible_cnt(i), max_cnt)

    return max_cnt


if __name__ == "__main__":
    print(solution(get_input()))

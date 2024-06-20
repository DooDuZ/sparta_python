# boj 30805 사전 순 최대 공통 부분 수열
# dfs 완탐은 시간 초과

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    numbers_a = list(map(int, input().split()))

    m = int(input())

    numbers_b = list(map(int, input().split()))

    return [n, m, numbers_a, numbers_b]


def solution(params):
    n, m, numbers_a, numbers_b = params

    def dfs(depth, idx, numbers, sub_list, sub_set, end):
        sub_set.add(tuple(sub_list))

        if depth == end:
            return

        sub_list.append(numbers[idx])

        dfs(depth + 1, idx + 1, numbers, sub_list, sub_set, end)
        sub_list.pop()
        dfs(depth + 1, idx + 1, numbers, sub_list, sub_set, end)

    set_a = set()
    dfs(0, 0, numbers_a, [], set_a, n)

    set_b = set()
    dfs(0, 0, numbers_b, [], set_b, m)

    sub = sorted(list(set_a & set_b), reverse=True)[0]

    return [len(sub), sub]


if __name__ == "__main__":
    lng, sub_list = solution(get_input())
    print(lng)
    print(*sub_list)

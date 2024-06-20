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

    target = 100
    a_idx = 0
    b_idx = 0

    common_sub_list = []

    while target > 0:

        find_a = -1
        find_b = -1

        for i in range(a_idx, n):
            if numbers_a[i] == target:
                find_a = i
                break

        for i in range(b_idx, m):
            if numbers_b[i] == target:
                find_b = i
                break

        if find_a != -1 and find_b != -1:
            a_idx = find_a + 1
            b_idx = find_b + 1
            common_sub_list.append(target)
        else:
            target -= 1

    return common_sub_list


if __name__ == "__main__":
    sub_list = solution(get_input())
    print(len(sub_list))
    print(*sub_list)

# BOJ 2805 나무 자르기

import sys

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(n)
    params.append(m)
    params.append(list(map(int, input().split())))

    return params


def solution(params):
    n, m, trees = params

    trees.sort()

    def binary_search():
        left = 0
        right = max(trees)

        while left < right:
            mid = (left + right) // 2

            cutting_tree = cut_trees(mid)

            if cutting_tree < m:
                right = mid
            else:
                left = mid + 1

        return left - 1

    def cut_trees(h):
        total = 0

        for tree in trees:
            if tree <= h:
                continue
            total += tree - h

        return total

    return binary_search()


print(solution(get_input()))

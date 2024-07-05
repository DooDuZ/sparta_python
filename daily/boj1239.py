# BOJ 1239 차트

import sys
from itertools import permutations

input = sys.stdin.readline


def get_input():

    n = int(input())
    rates = list(map(int, input().split()))

    return [n, rates]


def solution(params):
    def check(comb):
        ret = 0
        for i in range(len(comb)):
            total = 0
            for j in range(i, len(comb)):
                total += comb[j]
                if total == 50:
                    ret += 1
        return ret - 1

    n, rates = params

    cnt = 0

    comb = list(permutations(rates))

    for c in comb:
        numbers = list(c)
        cnt = max(cnt, check(numbers))

    return cnt


if __name__ == "__main__":
    print(solution(get_input()))

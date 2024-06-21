# BOJ 15654 N과 M 5
import sys
from itertools import permutations

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    numbers = list(map(int, input().split()))

    return [n, m, numbers]


def solution(params):
    n, m, numbers = params

    comb = list(map(list, permutations(numbers, m)))

    return sorted(comb)


if __name__ == "__main__":
    print("\n".join(" ".join(map(str, x)) for x in solution(get_input())))

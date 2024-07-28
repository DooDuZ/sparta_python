# BOJ 15663 N과 M 9
import sys
from itertools import permutations

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    return [n, m, numbers]


def solution(params):
    n, m, numbers = params

    return sorted(list(set(permutations(numbers, m))))


if __name__ == "__main__":
    for sub in solution(get_input()):
        print(*sub)

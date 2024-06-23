# BOJ 17298 오큰수

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())
    numbers = list(map(int, input().split()))

    return [n, numbers]


def solution(params):
    n, numbers = params

    marking = [-1 for _ in range(n)]

    stack = []

    for i, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            marking[stack.pop()] = number
        stack.append(i)

    return marking


if __name__ == "__main__":
    print(*solution(get_input()))

# BOJ 1059 좋은 구간
import sys

input = sys.stdin.readline


def get_input():
    L = int(input())

    numbers = list(map(int, input().split()))

    n = int(input())

    return [L, numbers, n]


def solution(params):
    L, numbers, n = params

    if n in set(numbers):
        return 0

    if n > max(numbers):
        return 0

    numbers.sort()

    start = -1
    end = -1

    for i in range(L):
        if numbers[i] < n:
            start = numbers[i]
        elif numbers[i] >= n and end < 0:
            end = numbers[i]
            break

    start = max(1, start + 1)

    return (n + 1 - start) * (end - n) - 1


if __name__ == "__main__":
    print(solution(get_input()))

"""
3
5 10 15
1

"""

# BOJ 1312 소수
import sys

input = sys.stdin.readline


def get_input():
    return list(map(int, input().split()))


def solution(params):
    a, b, n = params

    for i in range(n + 1):
        a = a % b * 10

    return a // b


if __name__ == "__main__":
    print(solution(get_input()))

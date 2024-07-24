# BOJ 1105 팔
import sys
from collections import Counter

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    return [n, m]


def solution(params):
    n, m = params

    digit_n, digit_m = list(map(int, str(n))), list(map(int, str(m)))

    if len(digit_n) != len(digit_m):
        return 0

    if digit_n.count(8) == 0 or digit_m.count(8) == 0:
        return 0

    lng = len(digit_n)

    cnt = 0

    for i in range(lng):
        if digit_n[i] == digit_m[i] == 8:
            cnt += 1
        elif digit_n[i] == digit_m[i]:
            continue
        else:
            break

    return cnt


if __name__ == "__main__":
    print(solution(get_input()))

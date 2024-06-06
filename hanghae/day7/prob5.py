import sys

input = sys.stdin.readline


def get_input():
    params = []

    params.append(int(input()))
    params.append(input().strip())

    return params


def solution(params):
    hash = 0

    # offset -> 알파벳 소문자를 1~26으로 바꿔주기 위한 변수
    offset, R, MOD = 96, 31, 1234567891

    n, string = params

    # R의 지수별 거듭제곱
    pow_r = 1

    for s in string:
        # 탐색한 문자 해싱 후 더해주기
        hash += (ord(s) - offset) * pow_r % MOD
        hash %= MOD
        # R 거듭제곱
        pow_r *= R
        pow_r %= MOD

    return hash


print(solution(get_input()))

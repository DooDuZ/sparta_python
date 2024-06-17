# BOJ 1713 후보자

import sys
from collections import defaultdict

input = sys.stdin.readline


def get_input():
    n = int(input())
    s = int(input())

    recommends = list(map(int, input().split()))

    return [n, s, recommends]


def solution(params):
    n, s, recommends = params

    candidates = defaultdict(int)

    # 후보풀 넘쳤는지 체크
    def check_over():
        return len(candidates) == n

    # 추천 가장 적은 후보 제거
    def remove_least():
        least = 1000
        rm_key = 0
        for key in candidates.keys():
            if candidates[key] < least:
                least = candidates[key]
                rm_key = key

        del candidates[rm_key]

    def recommend(student):
        # 등록되지 않은 학생이 추천되고, 후보 풀이 가득 차있으면
        if student not in candidates and check_over():
            remove_least()

        # 추천 수 추가
        candidates[student] = candidates[student] + 1

    for r in recommends:
        recommend(r)

    return sorted(list(candidates.keys()))


if __name__ == "__main__":
    print(*solution(get_input()))

# BOJ 1205 등수 구하기
import sys
from collections import defaultdict

input = sys.stdin.readline


def get_input():
    n, m, p = list(map(int, input().split()))

    scores = []

    if n != 0:
        scores = list(map(int, input().split()))

    return [n, m, p, scores]


def solution(params):
    n, m, p, scores = params

    scores.append(m)

    scores.sort(reverse=True)

    score_count = defaultdict(int)

    rank = 1
    total = 0

    for score in scores:
        score_count[score] = score_count[score] + 1

    sort_score = list(score_count.keys())

    sort_score.sort(reverse=True)

    for score in sort_score:
        total += score_count[score]
        if score == m:
            break
        rank += score_count[score]

    if total > p:
        rank = -1

    return rank


if __name__ == "__main__":
    print(solution(get_input()))

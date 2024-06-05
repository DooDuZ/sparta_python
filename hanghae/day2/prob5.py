# 단순 계산 문제

import sys

n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

scores.sort()

print(sum(score * 100 / scores[-1] for score in scores) / len(scores))

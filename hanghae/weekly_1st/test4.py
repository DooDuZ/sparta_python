import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

city = [list(map(int, input().strip().split())) for _ in range(n)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


houses = []
shops = []

for i, row in enumerate(city):
    for j, dot in enumerate(row):
        if dot == 1:
            houses.append([i, j])
        elif dot == 2:
            shops.append((i, j))

comb = list(combinations(shops, m))


def is_possible(r, c):
    if (0 <= r < n) and (0 <= c < n):
        return True
    return False


answer = 1000000000
for c in comb:
    total = 0
    for house in houses:
        # 최대 치킨거리 100
        distance = 101
        for s in c:
            distance = min(distance, abs(s[0] - house[0]) + abs(s[1] - house[1]))
        total += distance

    answer = min(answer, total)

print(answer)

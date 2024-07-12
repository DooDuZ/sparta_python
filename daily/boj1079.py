# BOJ 1079 마피아

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())

    scores = list(map(int, input().split()))

    ds = []

    for _ in range(n):
        ds.append(list(map(int, input().split())))

    eun = int(input())

    return [n, scores, ds, eun]


def solution(params):
    n, scores, ds, eun = params

    lives = [True for _ in range(n)]

    answer = 0

    def day():
        maximum = 0
        idx = 0
        for i in range(n):
            if not lives[i]:
                continue
            if maximum < scores[i]:
                maximum = scores[i]
                idx = i

        lives[idx] = False
        return idx

    def night(target):
        lives[target] = False
        update_scores(target, 1)

    def reverse_night(target):
        lives[target] = True
        update_scores(target, -1)

    def update_scores(dead_person, direction):
        for i in range(n):
            if not lives[i] or i == dead_person:
                continue
            scores[i] += ds[dead_person][i] * direction

    def dfs(depth, cnt):
        nonlocal answer

        if depth == n - 1 or not lives[eun]:
            answer = max(cnt, answer)
            return

        if (n - depth) % 2 == 0:
            for i in range(n):
                if not lives[i] or i == eun:
                    continue
                night(i)
                dfs(depth + 1, cnt + 1)
                reverse_night(i)
        else:
            dead = day()
            dfs(depth + 1, cnt)
            lives[dead] = True

    dfs(0, 0)

    return answer


if __name__ == "__main__":
    print(solution(get_input()))

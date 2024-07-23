# BOJ 7579 앱

import sys

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    in_memory = list(map(int, input().split()))

    costs = list(map(int, input().split()))

    return [n, m, in_memory, costs]


def solution(params):
    n, m, memories, costs = params

    dp = [0 for _ in range(sum(costs) + 1)]

    for j, memory in enumerate(memories):
        cost = costs[j]
        for i in range(sum(costs), -1, -1):
            if i - cost < 0:
                continue
            dp[i] = max(dp[i], dp[i - cost] + memory)

    answer = []

    for i, c in enumerate(dp):
        if c >= m:
            answer.append(i)

    return min(answer)


if __name__ == "__main__":
    print(solution(get_input()))

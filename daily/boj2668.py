# BOJ 2668 숫자 고르기

import sys

input = sys.stdin.readline


def get_input():

    n = int(input())

    numbers = []

    for _ in range(n):
        numbers.append(int(input()))

    return [n, [0] + numbers]


def solution(params):
    n, numbers = params

    answer_set = set()

    visited = [True for _ in range(n + 1)]
    visited[0] = False

    for i in range(1, n + 1):
        cur = i
        up_set = set()
        down_set = set()
        while visited[cur]:
            visited[cur] = False
            up_set.add(cur)
            down_set.add(numbers[cur])
            cur = numbers[cur]

        if up_set == down_set:
            answer_set.update(up_set)
        else:
            for number in up_set:
                if number not in answer_set:
                    visited[number] = True
            for number in down_set:
                if number not in answer_set:
                    visited[number] = True

    return sorted(list(answer_set))


if __name__ == "__main__":
    answer = solution(get_input())
    print(len(answer))
    print(*answer, sep="\n")

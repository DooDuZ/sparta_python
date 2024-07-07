# BOJ 1024 수열의 합
import sys

input = sys.stdin.readline


def get_input():
    return list(map(int, input().split()))


def solution(params):

    target, lng = params

    answer = []

    while lng <= 100 and not answer:
        if lng % 2 == 1:
            if target % lng == 0:
                start = target // lng - lng // 2
                if start >= 0:
                    answer = [x for x in range(start, start + lng)]
        else:
            if target % lng == lng // 2:
                start = target // lng - lng // 2 + 1
                if start >= 0:
                    answer = [x for x in range(start, start + lng)]

        lng += 1

    answer.sort()

    if not answer:
        answer.append(-1)

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

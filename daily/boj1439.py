# BOJ 1439 뒤집기
import sys

input = sys.stdin.readline


def get_input():
    return list(map(int, input().rstrip()))


def solution(params):

    numbers = params

    if len(set(numbers)) == 1:
        return 0

    answer = [0, 0]

    flag = -1

    for number in numbers:
        if number != flag:
            flag = number
            answer[flag] += 1

    return min(answer)


if __name__ == "__main__":
    print(solution(get_input()))

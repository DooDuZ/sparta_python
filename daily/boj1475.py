# BOJ 1475 방 번호

import sys

input = sys.stdin.readline


def get_input():
    return input().rstrip()


def solution(params):
    room = params

    # 9는 6으로 함꼐 사용한다
    numbers = [0 for _ in range(9)]

    cnt = 0

    for c in room:
        number = int(c)

        if number == 9:
            number = 6

        if numbers[number] == 0:
            cnt += 1
            for i in range(9):
                numbers[i] += 1
            numbers[6] += 1

        numbers[number] -= 1

    return cnt


if __name__ == "__main__":
    print(solution(get_input()))

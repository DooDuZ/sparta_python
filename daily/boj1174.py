# BOJ 1174 줄어드는 수

import sys

input = sys.stdin.readline


def get_input():
    return int(input())


def solution(target):

    def get_numbers(digit, number, num_str, lng):
        if digit == 0 or number == -1:
            if len(num_str) != lng:
                return
            decreases.add(int(num_str))
            return

        get_numbers(digit - 1, number - 1, num_str + str(number), lng)
        get_numbers(digit, number - 1, num_str, lng)

    decreases = set()

    for i in range(1, 11):
        get_numbers(i, 9, "", i)

    if target > 1023:
        return -1

    answer = sorted(list(decreases))

    return answer[target - 1]


if __name__ == "__main__":
    print(solution(get_input()))

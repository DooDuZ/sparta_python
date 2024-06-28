# BOJ 1253 좋다
import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))

    return [n, numbers]


def solution(params):
    n, numbers = params

    answer = 0

    numbers.sort()

    for i in range(n):
        target = numbers[i]

        left = 0
        right = n - 1

        while left < right:
            if i == left:
                left += 1
                continue
            elif i == right:
                right -= 1
                continue

            cur = numbers[left] + numbers[right]

            if cur == target:
                answer += 1
                break
            elif cur < target:
                left += 1
            else:
                right -= 1

    return answer


if __name__ == "__main__":
    print(solution(get_input()))

"""
5
-1 -2 -3 -4 -5

5
-1 0 1 2 3

4
0 1 2 5
"""

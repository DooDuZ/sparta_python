# BOJ 1111 IQ TEST
import sys

input = sys.stdin.readline


def get_input():

    n = int(input())

    return [n, list(map(int, input().split()))]


def solution(params):
    def get_a(an, an2, an3):
        x = an2 - an
        if x == 0:
            return 0

        return (an3 - an2) // x

    def get_b(x, number, number2):
        return number2 - x * number

    n, numbers = params

    if n <= 2:
        if n == 2:
            if len(set(numbers)) == 1:
                return numbers[0]
        return "A"

    func = set()

    for i in range(n - 2):
        a = get_a(numbers[i], numbers[i + 1], numbers[i + 2])
        if a == "B":
            return a
        b = get_b(a, numbers[i], numbers[i + 1])

        func.add((a, b))

    lng = len(func)

    if lng == 1:
        a, b = list(func)[0]
        return numbers[n - 1] * a + b
    else:
        answer = set()

        for f in func:
            a, b = f

            for i in range(n - 1):
                value = a * numbers[i] + b != numbers[i + 1]
                if value:
                    return "B"
                answer.add(value)

        if len(answer) >= 2:
            return "A"
        return list(answer)[0]


if __name__ == "__main__":
    print(solution(get_input()))


"""
3
-44 -43 100
"""

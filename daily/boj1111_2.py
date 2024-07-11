# BOJ 1111 IQ TEST
import sys

input = sys.stdin.readline


def get_input():

    n = int(input())

    return [n, list(map(int, input().split()))]


def solution(params):

    n, numbers = params

    idx = 0

    func = set()

    if n == 1:
        return "A"

    for i in range(-200, 201):
        b = numbers[1] - numbers[0] * i
        flag = True
        for j in range(n - 1):
            if numbers[j + 1] - numbers[j] * i != b:
                flag = False
                break
        if flag:
            func.add((i, b))

    while idx < n - 1 and func:
        fail = set()
        for f in func:
            a, b = f
            if a * numbers[idx] + b != numbers[idx + 1]:
                fail.add(f)

        func -= fail
        idx += 1

    if len(func) >= 2:
        l = list(func)

        prev = numbers[n - 1] * l[0][0] + l[0][1]

        for f in func:
            a, b = f
            if numbers[n - 1] * a + b != prev:
                return "A"

        return prev
    elif len(func) == 0:
        return "B"
    else:
        a = b = 0
        for f in func:
            a, b = f

        return numbers[n - 1] * a + b


if __name__ == "__main__":
    print(solution(get_input()))

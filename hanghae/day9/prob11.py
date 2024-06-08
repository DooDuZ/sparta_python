import sys

input = sys.stdin.readline


def get_input():
    return input().strip()


def solution(string):
    PPAP = "PPAP"
    NP = "NP"

    stack = []
    idx = 0

    for c in string:
        if PPAP[idx] == c:
            idx += 1
        else:
            if c == "P" and stack[-1] == "P":
                idx = 2
            else:
                idx = 0

        stack.append(c)

        if idx == 4:
            for _ in range(4):
                stack.pop()

            if stack and stack[-1] == "P":
                idx = 2
            else:
                idx = 1
            stack.append("P")

    if "".join(stack) == "P":
        return PPAP
    else:
        return NP


print(solution(get_input()))

"""

P

PPAP

PPAPPAP

PPPAPPAPAP

PPAP P PPAP PPAP

PPPPAAP

PPPAPAP

"""

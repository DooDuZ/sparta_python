# 프로그래머스 lv2 월간 코드 챌린지 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502#


def solution(s):
    n = len(s)

    if n == 1:
        return 0

    def check(string):
        stack = []

        for c in string:
            if c in pair:
                stack.append(c)
            else:
                if not stack or c != pair[stack.pop()]:
                    return False

        if stack:
            return False

        return True

    answer = 0

    pair = {"(": ")", "[": "]", "{": "}"}

    for i in range(n):
        if check(s):
            answer += 1

        s = s[1:] + s[0]

    return answer

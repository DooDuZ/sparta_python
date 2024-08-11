# 프로그래머스 lv2 구명 보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885#

from collections import deque


def solution(people, limit):
    answer = 0

    people.sort()

    q = deque(people)

    while q:
        weight = limit
        answer += 1

        if q and weight - q[-1] >= 0:
            weight -= q.pop()

        if q and weight - q[0] >= 0:
            weight -= q.popleft()

    return answer

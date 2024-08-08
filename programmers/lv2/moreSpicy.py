# 프로그래머스 lv2 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from heapq import *


def solution(scoville, K):
    answer = 0

    heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        answer += 1

        single = heappop(scoville)
        double = heappop(scoville)

        heappush(scoville, single + 2 * double)

    if scoville[0] < K:
        return -1

    return answer

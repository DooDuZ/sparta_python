import sys
from heapq import *

input = sys.stdin.readline


def get_input():
    params = []

    n, c, h = list(map(int, input().split()))

    giants = []

    for _ in range(n):
        giants.append(int(input()))

    params.append(c)
    params.append(h)
    params.append(giants)

    return params


def solution(params):
    answer = []

    centi, hammers, giants = params

    heap = []

    for giant in giants:
        heappush(heap, -giant)

    cnt = 0
    while heap and hammers > 0 and -heap[0] >= centi:
        giant = -heappop(heap)
        if giant > 2:
            giant //= 2
        heappush(heap, -giant)
        hammers -= 1
        cnt += 1

    biggest = -heappop(heap)

    if biggest < centi:
        answer.append("YES")
        answer.append(str(cnt))
    else:
        answer.append("NO")
        answer.append(str(biggest))

    return answer


print("\n".join(solution(get_input())))

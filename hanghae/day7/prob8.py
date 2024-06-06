import sys
from heapq import heapify, heappop, heappush

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        params.append(int(input()))

    return params


def solution(params):
    answer = []

    heap = []
    heapify(heap)

    # python heapq에 순서가 있는 데이터가 삽입되는 경우, 앞의 데이터부터 순차적으로 비교한다
    for param in params:
        if param == 0:
            if heap:
                answer.append(str(heappop(heap)[1]))
            else:
                answer.append(str(0))
            continue

        # 절대값과 원본 값을 같이 push
        heappush(heap, [abs(param), param])

    return answer


print("\n".join(solution(get_input())))

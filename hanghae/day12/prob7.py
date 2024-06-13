# BOJ 13335 트럭
# Queue 문제

import sys
from collections import deque


input = sys.stdin.readline


def get_input():
    params = []

    params.append(list(map(int, input().split())))
    params.append(list(map(int, input().split())))

    return params


def solution(params):
    n, w, L = params[0]
    truck_q = deque(params[1])
    bridge_q = deque()
    time = 0
    total_weight = 0

    while truck_q or bridge_q:
        # 다리 건너기
        # 다 건널 시간이 된 차는 pop해서 다리 위의 무게에서 제거
        if bridge_q and bridge_q[0][1] == time:
            total_weight -= bridge_q.popleft()[0]

        # 다리 올라가기
        # 다리를 다 건너는 시간을 같이 넣어준다
        if truck_q and total_weight + truck_q[0] <= L and len(bridge_q) + 1 <= w:
            weight = truck_q.popleft()
            total_weight += weight
            bridge_q.append([weight, w + time])

        # 단위 시간 증가
        time += 1

    return time


if __name__ == "__main__":
    print(solution(get_input()))

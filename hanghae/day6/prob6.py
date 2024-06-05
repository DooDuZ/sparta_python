import sys
from collections import deque

input = sys.stdin.readline


# 입력 받기
def get_input():
    params = []

    for _ in range(2):
        params.append(list(map(int, input().strip().split())))

    return params


def solution(params):
    # 찾으려는 값의 index를 찾습니다.
    def find_idx(arr, value):
        for i, v in enumerate(arr):
            if v == value:
                return i

    def shift_r(arr):
        arr.appendleft(arr.pop())

    def shift_l(arr):
        arr.append(arr.popleft())

    cnt = 0

    n, m = params[0]

    # 뽑는 순서
    picks = deque(params[1])

    indexes = deque([i for i in range(n)])

    # 뽑아야할 게 남아있다면
    while picks:
        # 목표값
        target = picks.popleft() - 1
        # 목표값의 인덱스
        idx = find_idx(indexes, target)

        if idx > len(indexes) // 2:
            while indexes[0] != target:
                shift_r(indexes)
                cnt += 1
        else:
            while indexes[0] != target:
                shift_l(indexes)
                cnt += 1

        indexes.popleft()
    return cnt


print(solution(get_input()))

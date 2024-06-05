import sys
from collections import deque

input = sys.stdin.readline


# 입력 받기
def get_input():
    int(input())
    params = list(map(int, input().strip().split()))

    return params


def solution(params):
    def shift_l(arr, count):
        for _ in range(count):
            arr.append(arr.popleft())

    def shift_r(arr, count):
        for _ in range(count):
            arr.appendleft(arr.pop())

    answer = []

    q = deque()

    # q에 원래 인덱스와 이동거리 함께 저장
    for i, param in enumerate(params):
        q.append([i, param])

    while True:
        i, value = q.popleft()
        answer.append(i + 1)

        # 종료 조건이 안에 있는게 매우.. 마음에 안든다. 추가 indent 없이 종료 조건을 하나로 합칠 수 있을까?
        if not q:
            break

        # 오른쪽으로 움직이는 경우, pop할때 1칸 땡겨지므로 이동거리 -1
        if value > 0:
            shift_l(q, abs(value) - 1)
        # 왼쪽은 그대로 진행 진행
        else:
            shift_r(q, abs(value))

    return answer


print(" ".join(str(x) for x in solution(get_input())))

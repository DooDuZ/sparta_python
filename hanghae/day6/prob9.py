import sys
from collections import deque

input = sys.stdin.readline


def get_input():
    params = []

    int(input())

    for _ in range(2):
        params.append(list(map(int, input().strip().split())))

    int(input())
    params.append(list(map(int, input().strip().split())))

    return params


# 문제 그대로 구현하면 시간초과
# stack은 항상 초기 값 대신 전달받은 값을 뱉어냄, 고려할필요 x
# q는 순서대로 리턴하므로 q를 여러개 묶을 필요 없이 하나의 배열로 처리 가능
def solution(params):
    answer = []

    queue_stack = deque()

    qs, elements, insert = params

    # q인 경우에만 순서대로 넣고
    for i, q in enumerate(qs):
        if q == 0:
            queue_stack.append(elements[i])

    for value in insert:
        queue_stack.appendleft(value)
        answer.append(queue_stack.pop())

    return answer


print(*solution(get_input()))

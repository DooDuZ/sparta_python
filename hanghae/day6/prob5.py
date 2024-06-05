import sys
from collections import deque

input = sys.stdin.readline


# 입력 받기
def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        param = []
        for _ in range(2):
            param.append(list(map(int, input().strip().split())))

        params.append(param)
    return params


def solution(params):
    # q에서 target을 인쇄하는데 걸리는 횟수
    def get_doc(q, target, sorted_by_priority):
        idx = 0
        while q:
            # 우선순위가 낮다면 뒤로 밀기
            if q[0][0] != sorted_by_priority[idx]:
                q.append(q.popleft())
                continue

            # 인쇄하고 다음 우선순위로 진행
            cur = q.popleft()
            idx += 1

            # 타겟에 도착하면 인쇄 횟수 리턴
            if cur[1] == target:
                return idx

    answer = []

    for param in params:
        idx = param[0][1]
        q = deque()

        # 문서를 idx와 함께 dequq에 저장
        for i, doc in enumerate(param[1]):
            q.append([doc, i])

        # 우선순위 별 내림차순 정렬
        sorted_docs = sorted(param[1], reverse=True)

        # 문서 찾기
        answer.append(get_doc(q, idx, sorted_docs))

    return answer


print("\n".join(str(x) for x in solution(get_input())))

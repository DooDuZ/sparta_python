import sys

input = sys.stdin.readline


def get_input():
    params = []

    params.append(int(input()))
    params.append(list(map(int, input().strip().split())))

    return params


# 타워는 왼쪽에 있는 자신보다 큰 타워들 중 가장 작은 타워를 바라본다
# 왼쪽에있는 작은 타워들은 저장할 필요x / 타워는 자신보다 작은 모든 왼쪽 타워를 가린다
def solution(params):
    n, towers = params

    answer = [0 for _ in range(n)]
    stack = []

    for i in range(0, n):
        # 현재 타워보다 더 큰 타워가 나올 때까지 이전 타워 pop
        while stack and towers[i] > towers[stack[-1] - 1]:
            stack.pop()

        # 스택이 비었다면 왼쪽에 현재 타워보다 높은 타워는 존재하지 않으므로 0
        answer[i] = stack[-1] if stack else 0

        # 현재 타워를 스택에 넣어준다
        stack.append(i + 1)

    if max(answer) == 0:
        return [0]

    return answer


print(" ".join(str(x) for x in solution(get_input())))

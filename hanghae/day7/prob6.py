import sys

input = sys.stdin.readline


def get_input():
    params = []

    for _ in range(2):
        params.append(int(input()))
        params.append(list(map(int, input().strip().split())))

    return params


def solution(params):
    answer = []

    n, numbers, m, targets = params

    num_set = set(numbers)

    # 타겟 있으면 1, 없으면 0
    for target in targets:
        if target in num_set:
            answer.append(str(1))
        else:
            answer.append(str(0))

    return answer


print("\n".join(solution(get_input())))

import sys
from collections import defaultdict

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        n = int(input())
        wears = []
        for _ in range(n):
            wears.append(input().strip())
        params.append(wears)

    return params


def solution(params):
    answer = []

    for param in params:
        wears = defaultdict(int)
        case = 1

        # 같은 이름을 가진 옷은 없다는 조건, 카테고리별로 숫자만 카운트
        for p in param:
            category = p.split()[1]
            wears[category] = wears[category] + 1

        # 옷을 입지 않는 경우가 있으므로 +1해서 곱함
        for value in wears.values():
            case *= value + 1

        # 모든 카테고리의 옷을 선택하지 않는 경우 -1
        answer.append(str(case - 1))

    return answer


print("\n".join(solution(get_input())))

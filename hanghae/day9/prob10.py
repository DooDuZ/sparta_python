import sys
from collections import defaultdict

input = sys.stdin.readline


def get_input():
    params = []

    while True:
        try:
            case = []

            case.append(int(input()))
            n = int(input())

            lego = []
            for i in range(n):
                lego.append(int(input()))
            case.append(lego)

            params.append(case)
        except:
            break

    return params


def solution(params):
    answer = []

    DANGER = "danger"
    YES = "yes "

    for case in params:
        area, legos = case
        area *= 10000000

        lego_dict = defaultdict(int)

        for lego in legos:
            lego_dict[lego] = lego_dict[lego] + 1

        selected = []

        for lego in legos:
            if area - lego in lego_dict:
                lego_dict[lego] -= 1
                if lego_dict[area - lego] < 1:
                    lego_dict[lego] += 1
                    continue
                if not selected or abs(selected[0] - selected[1]) < abs(
                    area - lego - lego
                ):
                    selected = [lego, area - lego]

                lego_dict[lego] += 1

        if not selected:
            answer.append(DANGER)
        else:
            selected.sort()
            answer.append(YES + " ".join(str(x) for x in selected))

    return answer


print("\n".join(solution(get_input())))

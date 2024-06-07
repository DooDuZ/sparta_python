import sys

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(list(map(int, input().split())))

    lines = []
    for i in range(m):
        lines.append(list(map(int, input().split())))

    params.append(lines)

    return params


def solution(params):
    answer = []

    dots, lines = params

    dots.sort()

    # 시작점 target, 시작점보다 크거나 같은 첫번째 위치 반환
    def lower(target):
        left = 0
        right = len(dots) - 1

        while left < right:
            mid = (left + right) // 2

            if dots[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    # 끝점 target, 끝점보다 큰 첫번째 위치 반환
    def upper(target):
        left = 0
        right = len(dots) - 1

        while left < right:
            mid = (left + right) // 2

            if dots[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return left

    for line in lines:
        if line[0] > dots[-1] or line[1] < dots[0]:
            answer.append(str(0))
            continue
        lng = upper(line[1]) - lower(line[0])

        if line[1] >= dots[-1]:
            lng += 1

        answer.append(str(lng))

    return answer


print("\n".join(solution(get_input())))

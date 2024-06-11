import sys

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(list(map(int, input().split())))

    return params


def solution(city):
    # 좌표 순 정렬
    city.sort()

    city.append([1000001, 0])

    stack = []
    cnt = 0

    for building in city:
        while stack and stack[-1][1] > building[1]:
            stack.pop()
            cnt += 1

        if stack and stack[-1][1] == building[1]:
            continue
        stack.append(building)

    return cnt


if __name__ == "__main__":
    print(solution(get_input()))

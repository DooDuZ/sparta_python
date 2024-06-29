# BOJ 1011 fly me to the Alpha Centauri
import sys

input = sys.stdin.readline


def get_input():

    params = []

    T = int(input())

    for _ in range(T):
        params.append(list(map(int, input().split())))

    return params


def solution(param):
    x, y = param

    dist = y - x

    def sum_target(number):
        return number * (number + 1) // 2

    def binary_search():
        left = 0
        right = dist

        target = dist // 2

        while left <= right:
            mid = (left + right) // 2

            if sum_target(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    answer = binary_search()

    num = sum_target(answer)

    if num * 2 > dist:
        if sum_target(answer - 1) == dist - num:
            answer *= 2
            answer -= 1
        else:
            answer *= 2
    elif num * 2 < dist:
        answer *= 2
        answer += 1
    else:
        answer *= 2

    return answer


if __name__ == "__main__":
    for param in get_input():
        print(solution(param))


"""
1
0 10


1
0 5

1
0 6

"""

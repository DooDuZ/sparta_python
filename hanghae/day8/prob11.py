import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    return list(map(int, input().split()))


def solution(liquid):
    liquid.sort()

    answer = []
    mixed = 2000000000

    left = 0
    right = len(liquid) - 1

    while left != right:
        mix = liquid[left] + liquid[right]
        if mix == 0:
            return [liquid[left], liquid[right]]

        if abs(mix) < abs(mixed):
            mixed = mix
            answer = [liquid[left], liquid[right]]

        if mix < 0:
            left += 1
        else:
            right -= 1

    answer.sort()

    return answer


print(*solution(get_input()))


"""

5
1 2 3 4 5

5
-2 4 -99 -1 98

answer -99 98

5
-2 4 -99 -1 99

answer -99 99

5
-2 4 1 -1 99

answer -1 1


10
-87 -42 -40 -22 -11 23 29 78 79 98

answer -22 23

5
-6 -8 -1 -2 -3

answer -2 -1

5
6 8 1 2 3

answer 1 2

3
-10 1 2

answer 1 2


4
999999995 999999996 999999997 1000000000

999999995 999999996

"""

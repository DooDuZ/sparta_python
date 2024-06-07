import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    return list(map(int, input().split()))


def solution(liquid):
    liquid.sort()

    answer = []
    mixed = 2000000001

    def binary_search(left, right, target):

        while left < right:
            mid = (left + right) // 2

            if liquid[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

    for i in range(len(liquid) - 1):
        reverse_idx = binary_search(i + 1, len(liquid) - 1, -liquid[i])

        if (
            reverse_idx != 0
            and reverse_idx - 1 != i
            and abs(liquid[reverse_idx - 1] + liquid[i])
            < abs(liquid[i] + liquid[reverse_idx])
        ):
            reverse_idx -= 1

        if abs(liquid[i] + liquid[reverse_idx]) < mixed:
            mixed = abs(liquid[i] + liquid[reverse_idx])
            answer = [liquid[i], liquid[reverse_idx]]

    answer.sort()

    return answer


print(*solution(get_input()))

"""
5
1 2 3 4 5

5
-5 -4 -3 -2 -1

4
-4 3 6 7

5
-100 -50 5 500 1000


입력
4
-4 95 -80 -2

출력
-80 95 (특성치 15)

정답
-4 -2 (특성치 -6)


5
-98 -97 1 2 92
"""

# BOJ 2042 구간 합 구하기
import sys

input = sys.stdin.readline


def get_input():

    n, m, k = list(map(int, input().split()))

    numbers = []

    for _ in range(n):
        numbers.append(int(input()))

    commands = []

    for _ in range(m + k):
        commands.append(list(map(int, input().split())))

    return [n, m, k, numbers, commands]


def solution(params):
    def set_tree(index, left, right):
        if left == right:
            tree[index] = numbers[left]
            return tree[index]

        mid = (left + right) // 2

        tree[index] = set_tree(index * 2, left, mid) + set_tree(
            index * 2 + 1, mid + 1, right
        )

        return tree[index]

    def get_sum(index, start, end, left, right):
        if end < left or start > right:
            return 0
        elif left <= start and right >= end:
            return tree[index]

        mid = (start + end) // 2

        return get_sum(index * 2, start, mid, left, right) + get_sum(
            index * 2 + 1, mid + 1, end, left, right
        )

    def update(index, start, end, target, value):
        if start == end == target:
            tree[index] = value
            numbers[target] = value
            return

        if not start <= target <= end:
            return

        tree[index] -= numbers[target]
        tree[index] += value

        mid = (start + end) // 2

        update(index * 2, start, mid, target, value)
        update(index * 2 + 1, mid + 1, end, target, value)

    n, m, k, numbers, commands = params

    tree = [0 for _ in range(4 * n)]

    set_tree(1, 0, n - 1)

    answer = []

    for cmd in commands:
        c, l, r = cmd

        if c == 1:
            l -= 1
            update(1, 0, n - 1, l, r)
        else:
            l -= 1
            r -= 1
            answer.append(get_sum(1, 0, n - 1, l, r))

    return answer


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 3

"""

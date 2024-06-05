# https://www.acmicpc.net/problem/31785

import sys

n = int(sys.stdin.readline())

numbers = []
answer = []

for _ in range(n):
    cmd = list(map(int, sys.stdin.readline().rstrip().split()))

    if len(cmd) == 1:
        mid = len(numbers) // 2

        sum_l = sum(numbers[:mid])
        sum_r = sum(numbers[mid:])

        if sum_l > sum_r:
            answer.append(sum_r)
            numbers = numbers[:mid]
        else:
            answer.append(sum_l)
            numbers = numbers[mid:]

        continue

    numbers.append(cmd[1])

for n in answer:
    print(n)
print(" ".join(str(x) for x in numbers))

"""
8
1 2
1 1
1 4
1 5
2
1 7
2
1 5

"""

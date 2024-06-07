# BOJ 11399 ATM

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    people = list(map(int, input().split()))

    return people


def solution(people):
    people.sort()

    for i in range(1, len(people)):
        people[i] += people[i - 1]

    return sum(people)


print(solution(get_input()))

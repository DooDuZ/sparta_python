# BOJ 2212 센서

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    k = int(input())

    sensors = list(map(int, input().split()))

    return [n, k, sensors]


def solution(params):
    n, k, sensors = params

    sensors = list(set(sensors))
    distance = []

    sensors.sort()

    for i in range(1, len(sensors)):
        distance.append(sensors[i] - sensors[i - 1])

    distance.sort()

    total = 0
    for i in range(len(distance) - k + 1):
        total += distance[i]

    return total


if __name__ == "__main__":
    print(solution(get_input()))

"""
6
7
1 6 9 3 6 7

7
3
1 2 3 4 6 7 8

4 
2
1 5 9 12

"""

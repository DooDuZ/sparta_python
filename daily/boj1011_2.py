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

    cnt = 0
    lng = 1
    total = 0

    while total < dist:
        cnt += 1
        total += lng
        if cnt % 2 == 0:
            lng += 1

    return cnt


if __name__ == "__main__":
    for param in get_input():
        print(solution(param))


"""
5
0 1
0 2
0 3
0 4
0 5

30
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
0 10
0 11
0 12
0 13
0 14
0 15
0 16
0 17
0 18
0 19
0 20
0 21
0 22
0 23
0 24
0 25
0 26
0 27
0 28
0 29
0 30

ans :
1
2
3
3
4
4
5
5
5
6
6
6
7
7
7
7
8
8
8
8
9
9
9
9
9
10
10
10
10
10

"""

import sys

input = sys.stdin.readline


def get_input():
    params = []

    n = int(input())

    for _ in range(n):
        params.append(list(map(int, input().split())))

    return params


def solution(pillars):
    area = 0

    pillars.sort()

    top = 0
    tops = []

    # 천장 찾기
    for i, pillar in enumerate(pillars):
        if pillar[1] > top:
            tops.clear()
            top = pillar[1]
            tops.append(i)
        elif pillar[1] == top:
            tops.append(i)

    prev = pillars[0]
    # 왼쪽에서 천장까지
    for i in range(1, tops[0] + 1):
        if pillars[i][1] > prev[1]:
            area += prev[1] * (pillars[i][0] - prev[0])
            prev = pillars[i]

    stack = []

    # 낮아지는 구간
    for i in range(tops[-1], len(pillars)):
        while stack and pillars[i][1] > stack[-1][1]:
            stack.pop()
        stack.append(pillars[i])

    end = stack.pop()
    while stack:
        prev = stack.pop()

        area += end[1] * (end[0] - prev[0])
        end = prev

    if len(tops) != 1:
        area += pillars[tops[0]][1] * (pillars[tops[-1]][0] - pillars[tops[0]][0])

    area += pillars[tops[0]][1]

    return area


print(solution(get_input()))

"""

4
1 6
3 6
5 6
7 7


4
1 6
3 6
5 6
7 5


5
1 6
3 9
5 8
7 7
9 8


4
1 3
2 2
3 3
4 3


3
0 3
1 2
2 3


3
0 3
1 4
2 3


5
1 1
2 1
3 1
4 1
5 1
"""

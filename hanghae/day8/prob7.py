# BOJ18870 좌표 압축
# 각 숫자가 몇번째로 작은 수인지 말하라는 문제임

import sys

input = sys.stdin.readline


def get_input():
    n = int(input())
    numbers = list(map(int, input().split()))

    return numbers


def solution(numbers):
    cnt = 0

    # 숫자 순위 저장
    counts = dict()

    sorted_list = sorted(list(numbers))

    # 오름차순 정렬해서 몇 번째로 큰 작은 수인지 딕셔너리에 추가한다
    for number in sorted_list:
        if number in counts:
            continue
        counts[number] = cnt
        cnt += 1

    # 값을 순위로 바꿔준다
    for i in range(len(numbers)):
        numbers[i] = counts[numbers[i]]

    return numbers


print(*solution(get_input()))

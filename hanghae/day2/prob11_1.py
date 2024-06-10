"""
재귀로 푸는 경우 최대 깊이 3000까지 발생할 수 있음
BOJ python 재귀 깊이 제한 1000
재귀 제한 풀고 진행하면 메모리 초과 발생

java 재귀 방식 : 메모리 = 44424kb, 응답 속도 = 544ms
python 반복문 사용 : 메모리 = 40800kb, 응답 속도 = 4380ms
pypy3 반복문 사용 : 메모리 200832kb, 응답 속도 = 940ms
"""

import sys
from collections import deque

N = int(sys.stdin.readline())
MOD = 1_000_000_007
names = [sys.stdin.readline().rstrip() for _ in range(N)]
facto = [0 for _ in range(3000)]

facto[0] = 1
facto[1] = 1

# 정렬된 상태에서 시작해야 같은 패턴을 가진 문자를 길이별로 잘라낼 수 있음
names.sort()

# q생성
queue = deque()
queue.append([0, N, 0])


def count_of_sort(q):
    ret = 1

    while q:
        # s : 시작 인덱스, e : 끝 인덱스, lng : 현재 탐색중인 문자열의 인덱스
        s, e, lng = q.popleft()
        group = 0
        # 길이가 짧아서 다음으로 넘어가지 못하는 그룹이 있는지 체크합니다
        check_short = False

        # 주어진 범위 탐색 시작
        for i in range(s, e):
            # 탐색 범위 안에 주어진 길이보다 짧은 단어가 있다면 체크 후 넘어갑니다
            # 다음 lng으로 넘어갈 때 포함되지 않도록 s를 뒤로 한칸 밀어줍니다
            if len(names[i]) <= lng:
                s += 1
                check_short = True
                continue

            # 탐색할 문자 지정
            last_alp = names[s][lng]

            # 문자가 달라지면, s부터 현재까지의 인덱스를 묶어 q에 넣어줍니다. lng위치의 문자 비교는 끝났기 때문에 1 증가시켜줍니다.
            # 시작지점을 현재 인덱스로 옮긴 후, 단어 묶음 변수를 하나 늘려줍니다
            if names[i][lng] != last_alp:
                q.append([s, i, lng + 1])
                s = i
                group += 1

            # 순회가 끝나고 남아있는 그룹이 있다면 q에 넣어 줍니다
            if (i + 1) == e:
                q.append([s, e, lng + 1])
                group += 1

        # 만약 길이가 짧아 문자열 비교를 하지 못한 그룹이 있다면 처리합니다
        if check_short:
            group += 1

        ret = multiple(ret, factorial(group))

    return ret


def factorial(number):
    if facto[number] == 0:
        facto[number] = number * factorial(number - 1) % MOD

    return facto[number]


def multiple(a, b):
    return a * b % MOD


print(count_of_sort(queue))

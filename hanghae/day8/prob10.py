import sys

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().split()))

    params.append(m)

    immigration = []
    for _ in range(n):
        immigration.append(int(input()))

    params.append(immigration)

    return params


# 최소 공배수로도 접근이 되지 않을까? -> 심사대가 많으면 효율적이지 못함 / 큰 숫자가 섞여도 마찬가지
# 힙큐 쓰자 -> m이 10억까지가네 ㅋㅋㅋㅋㅋㅋㅋ
# 돌고돌아 이분탐색. 싫다,,
def solution(params):
    m, immigrations = params

    immigrations.sort()

    # 시간별로 통과시킬 수 있는 인원의 수
    # 최대 걸릴 수 있는 시간은 정렬된 이미그레이션의 마지막값 * 인원수.. 하지말고 최소시간에 다때려박는 걸로 가자
    # log2 10억 * 10억...해도 60 이하
    # 주어진 시간에 통과시킬 수 있는 인원 수 계산 함수 만들기
    def pass_in_time(time):
        total = 0

        for im in immigrations:
            total += time // im

        return total

    left = 0
    right = immigrations[0] * m

    while left < right:
        mid = (left + right) // 2

        pass_cnt = pass_in_time(mid)

        if pass_cnt < m:
            left = mid + 1
        else:
            right = mid

    return left


print(solution(get_input()))

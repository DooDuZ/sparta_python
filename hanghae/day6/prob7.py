import sys

input = sys.stdin.readline

Y = "YES"
N = "NO"

T = int(input())


# 입력 받기
def get_input(T):
    params = []
    for _ in range(T):
        params.append(input().strip())

    return params


def solution(params):
    answer = []

    # 등장한 (의 개수만큼 )가 등장해야함
    def is_vps(pattern):
        cnt = 0
        for p in pattern:
            if p == "(":
                cnt += 1
            else:
                cnt -= 1

            # 모든 시점에서 )가 더 많이 등장했다면 vps조건을 만족할 수 없음
            if cnt < 0:
                break
        return cnt

    # (와 )의 개수가 같았다면 Y, 달랐다면 N
    for param in params:
        if is_vps(param) == 0:
            answer.append(Y)
        else:
            answer.append(N)

    return answer


print("\n".join(solution(get_input(T))))

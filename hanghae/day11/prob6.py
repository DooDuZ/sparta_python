# BOJ 4673 셀프 넘버
# 절대 주의
# n과 n의 각 자리수를 더하는 함수 -> 부분 수열은 더하는거 아님...!!

import sys

input = sys.stdin.readline


def solution():
    checked = [True for _ in range(10000)]

    def d(n):
        total = n
        number = str(n)

        # 각 자리수 더해주고
        for i in range(len(number)):
            total += int(number[i])

        # 더한 값이 10000 안쪽이면 생성자가 존재하므로 체크
        if total < 10000 and checked[total]:
            checked[total] = False

    # 10000 미만까지 실행
    for i in range(1, 10000):
        d(i)

    answer = []

    # 체크 안된 숫자 append
    for i in range(1, 10000):
        if checked[i]:
            answer.append(i)

    return answer


if __name__ == "__main__":
    print(*solution(), sep="\n")

# 프로그래머스 lv2 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    def to_binary_string(total):
        next = []

        while total > 1:
            next.append(total % 2)
            total //= 2

        next.append(1)

        return "".join(map(str, next[::-1]))

    def get_cnt(string):
        return sum(list(map(int, string)))

    answer = [0, 0]

    while s != "1":
        lng = get_cnt(s)

        answer[0] += 1
        answer[1] += len(s) - lng

        s = to_binary_string(lng)

    return answer

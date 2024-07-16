# BOJ 1235 학생 번호
import sys

input = sys.stdin.readline


def get_input():
    n = int(input())

    student_ids = []

    for _ in range(n):
        student_ids.append(int(input()))

    return [n, student_ids]


def solution(params):
    n, student_ids = params

    lng = len(str(student_ids[0]))

    for i in range(1, lng + 1):
        cnt_set = set()

        for student_id in student_ids:
            cnt_set.add(student_id % pow(10, i))

        if len(cnt_set) == n:
            return i

    return 1


if __name__ == "__main__":
    print(solution(get_input()))

"""
3
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
2111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
3111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
"""

# BOJ 1366 기타 코드

import sys

input = sys.stdin.readline


def get_input():

    n, m = list(map(int, input().split()))

    strings = list(map(str, input().split()))
    notes = list(map(str, input().split()))

    return [n, m, strings, notes]


def solution(params):
    answer = 100

    def dfs(idx, note_list, cost_list):
        nonlocal answer

        if idx == n:
            if set(note_list) == set(notes):
                a_set = set(cost_list)

                if 0 in a_set:
                    a_set.remove(0)

                answer_list = list(a_set)

                answer = min(answer, max(answer_list) - min(answer_list) + 1)

            return

        for c in chord:
            note_list.append(c)
            for i in range(2):
                cost_list.append(costs[idx][c][i])
                dfs(idx + 1, note_list, cost_list)
                cost_list.pop()
            note_list.pop()

    n, m, strings, notes = params

    if set(notes) == set(strings):
        return 0

    chord = set(notes)

    scale = {
        "A": 0,
        "A#": 1,
        "B": 2,
        "C": 3,
        "C#": 4,
        "D": 5,
        "D#": 6,
        "E": 7,
        "F": 8,
        "F#": 9,
        "G": 10,
        "G#": 11,
    }

    scale_list = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    costs = []

    for j, string in enumerate(strings):
        start = scale[string]
        c_dict = dict()

        for i in range(12):
            c_dict[scale_list[(start + i) % 12]] = []
            if scale_list[(start + i) % 12] in chord:
                c_dict[scale_list[(start + i) % 12]].append(i)
                c_dict[scale_list[(start + i) % 12]].append(i + 12)

        costs.append(c_dict)

    dfs(0, list(), list())

    return answer


if __name__ == "__main__":
    print(solution(get_input()))

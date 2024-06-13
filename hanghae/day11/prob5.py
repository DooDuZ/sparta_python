# BOJ 1251 단어 나누기

import sys

input = sys.stdin.readline


def get_input():
    return input().strip()


def solution(word):
    # 과정 중 중복 단어가 나올 수 있으므로 set
    word_set = set()

    # slice 위치 정보를 바탕으로 단어 가공
    def get_reverse_word(idx_list):
        first, second = idx_list

        ret = (
            word[: first + 1][::-1]
            + word[first + 1 : second + 1][::-1]
            + word[second + 1 :][::-1]
        )

        return ret

    def dfs(depth, start, idx_list):
        # 자르는 지점 2개를 골랐다면 멈춰준다
        if depth == 2:
            word_set.add(get_reverse_word(idx_list))
            return

        # 시작 인덱스부터 최소한의 길이를 남길 때 까지 순회
        for i in range(start, len(word) - (2 - depth)):
            # 자르는 지점을 배열에 저장하고 넘겨준다
            idx_list[depth] = i
            dfs(depth + 1, i + 1, idx_list)

    dfs(0, 0, [-1, -1])

    return sorted(list(word_set))[0]


if __name__ == "__main__":
    print(solution(get_input()))

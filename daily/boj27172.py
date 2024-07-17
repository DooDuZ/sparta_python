# BOJ 27172 수 나누기 게임
import sys

input = sys.stdin.readline


def get_input():

    n = int(input())

    cards = list(map(int, input().split()))

    return [n, cards]


def solution(params):
    n, cards = params

    size = max(cards)

    visited = [True for _ in range(size + 1)]

    wins = [0 for _ in range(size + 1)]

    for card in cards:
        visited[card] = False

    for card in cards:
        for i in range(card * 2, size + 1, card):
            if visited[i]:
                continue
            wins[card] += 1
            wins[i] -= 1

    answer = []

    for card in cards:
        answer.append(wins[card])

    return answer


if __name__ == "__main__":
    print(*solution(get_input()))

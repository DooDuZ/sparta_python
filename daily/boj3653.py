# BOJ 3653 영화 수집
import sys

input = sys.stdin.readline


def get_input():
    n, m = list(map(int, input().split()))
    movies = list(map(int, input().split()))

    return [n, m, movies]


def solution(params):
    def set_tree(index, left, right):
        if left == right:
            tree[index] = 0 if left <= m else 1
            return tree[index]

        mid = (left + right) // 2

        tree[index] = set_tree(index * 2, left, mid) + set_tree(
            index * 2 + 1, mid + 1, right
        )

        return tree[index]

    # 노드의 인덱스, 노트 시작 범위, 노드 끝 범위, 탐색 시작 범위, 탐색 끝 범위
    def get_sum(index, start, end, left, right):
        # 현재 노드가 탐색 구간을 포함하지 않으면
        if end < left or start > right:
            return 0
        # 현재 노드가 탐색 구간을 완전히 포함하면
        elif left <= start and right >= end:
            return tree[index]

        mid = (start + end) // 2

        return get_sum(index * 2, start, mid, left, right) + get_sum(
            index * 2 + 1, mid + 1, end, left, right
        )

    def update(index, start, end, target, value):
        if start > target or end < target:
            return

        tree[index] += value

        if start == end:
            return

        mid = (start + end) // 2

        update(index * 2, start, mid, target, value)
        update(index * 2 + 1, mid + 1, end, target, value)

    n, m, selected = params

    answer = []

    # 테스트 케이스마다 선택된 영화를 저장해준다
    record = [-1 for _ in range(n + 1)]

    tree = [0 for _ in range(4 * (n + m))]

    # 트리를 초기화 해준다
    # m칸을 비우고!
    set_tree(1, 1, m + n)

    # 로직 실행
    for i, cur in enumerate(selected):
        # 0부터 시작하니 -1
        # 위에있는 영화 count 후, 트리 밖으로 올라간 영화의 개수 +
        target = cur + m if record[cur] == -1 else record[cur]

        value = get_sum(1, 1, n + m, 1, target)

        answer.append(value - 1)

        # 올라간 영화 -1
        update(1, 1, n + m, target, -1)

        update(1, 1, n + m, m - i, 1)
        record[cur] = m - i

    return answer


if __name__ == "__main__":
    T = int(input())

    answer = []

    for _ in range(T):
        answer.append(solution(get_input()))

    for a in answer:
        print(*a)

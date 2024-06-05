import sys
from collections import deque

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))
cells = [input().strip() for _ in range(n)]
words = []
# 왼쪽 위부터 모든 정점에서 출발한다면 4방향 체크를 할 필요가 없음
down, right = (1, 0), (0, 1)


def init_visited():
    return [[True for _ in range(m)] for _ in range(n)]


def get_words(r, c, v, d):
    q = deque()
    q.append([r, c])

    w = []

    while q:
        cur_r, cur_c = q.pop()

        w.append(cells[cur_r][cur_c])

        n_r, n_c = cur_r + d[0], cur_c + d[1]
        if is_possible(n_r, n_c, v):
            v[n_r][n_c] = False
            q.append([n_r, n_c])

    return "".join(w)


def is_possible(r, c, v):
    if (0 <= r < n) and (0 <= c < m) and v[r][c] and cells[r][c] != "#":
        return True
    return False


def search(direction):
    v = init_visited()
    # down 먼저 탐색, 동시에 하면 visited 배열 충돌
    for i in range(n):
        for j in range(m):
            if v[i][j] and cells[i][j] != "#":
                v[i][j] = False

                word = get_words(i, j, v, direction)

                if len(word) >= 2:
                    words.append(word)


# 아래 방향 탐색
search(down)
# 오른쪽 방향 탐색
search(right)

# 단어 정렬
words.sort()
print(words[0])

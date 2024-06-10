import sys

N = int(sys.stdin.readline())

constellation = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# 0 -> n
constellation.sort(key=lambda x: (x[0], x[1]))

vector = []

min_r, min_c, max_r, max_c = 100000, 100000, 0, 0

for i in range(N - 1):
    r, c = constellation[i]
    nr, nc = constellation[i + 1]

    vector.append([nr - r, nc - c])


def is_possible(r, c):
    if r < 0 or c < 0 or r > 1000000 or c > 1000000:
        return False
    return True


M = int(sys.stdin.readline())

stars = {tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)}
answer = []

for star in stars:
    r, c = star

    stop = False

    answer.append([r, c])

    for i in range(N - 1):
        nr = r + vector[i][0]
        nc = c + vector[i][1]
        t = (nr, nc)
        if not is_possible(nr, nc) or not t in stars:
            answer.clear()
            break

        r = nr
        c = nc

        answer.append([nr, nc])

        if i == N - 2:
            stop = True

    if stop:
        answer.sort(key=lambda x: (x[0], x[1]))
        print(answer[0][0] - constellation[0][0], answer[0][1] - constellation[0][1])
        break

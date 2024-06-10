import sys
from collections import defaultdict

N = int(sys.stdin.readline())
answer = []
SYJKGW = "SYJKGW"

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))

    army = defaultdict(int)
    is_win = False

    for j in range(1, line[0] + 1):
        team = line[j]

        army[team] = army[team] + 1

        if army[team] > line[0] // 2:
            answer.append(str(team))
            is_win = True
            break

    if not is_win:
        answer.append(SYJKGW)

print("\n".join(answer))

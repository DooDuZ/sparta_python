import sys

N, M = list(map(int, sys.stdin.readline().rstrip().split()))

# set로 입력 받고
never_heard = {sys.stdin.readline().rstrip() for _ in range(N)}
never_seen = {sys.stdin.readline().rstrip() for _ in range(M)}

# 교집합
answer = sorted(never_seen & never_heard)

print(len(answer))
print("\n".join(answer))

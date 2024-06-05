import sys

n = int(sys.stdin.readline())

# 인사한 유저를 저장합니다
kind_user = set()
cnt = 0

for i in range(n):
    log = sys.stdin.readline().rstrip()

    if log == "ENTER":
        kind_user.clear()
        continue

    # 인사 했다면 다음으로
    if log in kind_user:
        continue

    # 인사한 유저 추가
    kind_user.add(log)
    cnt += 1

print(cnt)

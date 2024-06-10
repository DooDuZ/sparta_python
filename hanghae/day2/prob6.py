import sys

N = int(sys.stdin.readline())

# 추가 제거 빠르도록
records = set()

for i in range(N):
    name, status = sys.stdin.readline().rstrip().split()

    if status == "enter":
        records.add(name)
    else:
        records.remove(name)

print("\n".join(N for N in sorted(list(records), reverse=True)))

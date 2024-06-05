import sys

n = int(sys.stdin.readline())

# 추가 제거 빠르도록
records = set()

for i in range(n):
    name, status = sys.stdin.readline().rstrip().split()

    if status == 'enter':
        records.add(name)
    else:
        records.remove(name)

print('\n'.join(n for n in sorted(list(records), reverse=True)))
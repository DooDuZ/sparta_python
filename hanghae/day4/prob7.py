import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

enter_q = deque()
out_q = deque()

for i in range(n):
    enter_q.append(input().strip())

for i in range(n):
    out_q.append(input().strip())


cnt = 0
check_out = set()

# 입장/퇴장 순서 일치하면 양쪽 모두 pop
# 입장q 데이터가 이미 퇴장한 차랴이라면 입장q pop
# 그렇지 않으면 추월한 차량임. cnt += 1해주고 퇴장 처리
while out_q:
    if out_q[0] == enter_q[0]:
        enter_q.popleft()
        out_q.popleft()
        continue

    if enter_q[0] in check_out:
        enter_q.popleft()
        continue

    car = out_q.popleft()
    check_out.add(car)
    cnt += 1

print(cnt)

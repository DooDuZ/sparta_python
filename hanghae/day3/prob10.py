import sys
from collections import defaultdict, deque

answer = []


def bfs(q, s):

    while q:
        c = q.pop()

        if not members[c][1]:
            members[c][1] = True
            if members[c][0] == s:
                return 1
            q.append(members[c][0])

    return 0


test_no = 0
while True:
    n = int(sys.stdin.readline())
    test_no += 1

    members = defaultdict(list)
    member_list = []

    if n == 0:
        break

    for i in range(n):
        f, t = sys.stdin.readline().strip().split()
        # 도착점과 방문 여부 함께 저장
        members[f] = [t, False]
        member_list.append(f)

    q = deque()
    cnt = 0
    for m in member_list:
        # 방문하지 않은 곳으로 간다면 q에 넣고 진행
        if not members[m][1]:
            q.append(m)
            cnt += bfs(q, m)

    # test_case 저장
    answer.append([test_no, cnt])


for result in answer:
    print(" ".join(str(x) for x in result))

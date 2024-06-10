import sys
from collections import deque

N = int(sys.stdin.readline())

msg = dict()
m_list = list()
answer = []


# https://www.acmicpc.net/board/view/104921
# 연속된 자음의 최대 개수 리턴
def check_consonant(message):
    vowel = "AEIOUYaeiouy"
    consonant = "bcdfghjklmnpqrstvwxzABCDFGHJKLMNPQRSTVWXZ"

    max_cnt = 0
    cnt = 0

    for c in message:
        if c in consonant:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 0

    max_cnt = max(max_cnt, cnt)
    return max_cnt


for i in range(N):
    M = sys.stdin.readline()
    m_list.append([M, check_consonant(M)])

ten_lines = deque()

for M in m_list:
    message, cnt = M

    flag = False

    # 메세지 중복 체크
    if message in msg:
        msg[message] += 1
    else:
        msg[message] = 1

    if cnt >= 5:
        c = 0
        for line in ten_lines:
            if line[1] >= 5:
                c += 1

        if c >= 3:
            flag = True

    # 기록 덱에 현재 메시지 append
    ten_lines.append(M)

    if cnt >= 6 or msg[message] >= 3:
        flag = True

    # 메세지 10개 넘어간 건 또 삭제를 해줘야댐 ㅋㅋ
    if len(ten_lines) > 10:
        d_m, d_c = ten_lines.popleft()
        msg[d_m] -= 1

    answer.append("y" if not flag else "n")

print("\n".join(str(x) for x in answer))

"""
12
hello
how r u?
where r u from?
kjhh kh kgkjhg jhg
where r u from?
i am from London, Ontario, Canada
how r you nxw?
now
where r u from?
kjhh kh kgkjhg jhg
very good
it is very cold here.
"""

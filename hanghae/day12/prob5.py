# 왜 또 내지...?

import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip()
SORRY = "I'm Sorry Hansoo"

alpha = dict(Counter(s))

# 출력 조건 사전순
sorted_key = list(alpha.keys())
sorted_key.sort()

evens = []
odd, odd_cnt = "", 0
for key in sorted_key:
    if alpha[key] % 2 == 1:
        odd_cnt += 1
        odd = key
        if odd_cnt == 2:
            break

    for i in range(alpha[key] // 2):
        evens.append(key)

# 문자열 결합용 리스트
answer = ["".join(evens)]

if odd_cnt > 1:
    print(SORRY)
else:
    if odd_cnt == 1:
        answer.append(odd)
    answer.append("".join(evens[::-1]))
    print("".join(answer))

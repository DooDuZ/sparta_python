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
    # 전체 개수가 홀수인 문자는 1개만 존재할 수 있다
    if alpha[key] % 2 == 1:
        odd_cnt += 1
        odd = key
        if odd_cnt == 2:
            break

    # 정방향 - 역방향 1번씩 출력하므로 1/2만 넣어준다
    for i in range(alpha[key] // 2):
        evens.append(key)

# 문자열 결합용 리스트
answer = ["".join(evens)]


if odd_cnt > 1:
    print(SORRY)
else:
    # 홀수 문자가 있다면 넣어주고
    if odd_cnt == 1:
        answer.append(odd)
    # 역방향 입력
    answer.append("".join(evens[::-1]))
    print("".join(answer))

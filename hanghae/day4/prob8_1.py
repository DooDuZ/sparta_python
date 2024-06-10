import sys

input = sys.stdin.readline

O, I, IO = "O", "I", "IO"
dc = [I, O]

N = int(input())


# P(n) 얻기
def get_pattern(n):
    return "".join(["".join([IO for _ in range(n)]), I])


pattern = get_pattern(N)
lng = int(input())
s = input().strip()


cnt = 0

# 탐색중인 패턴의 pn
pn = 0
# 현재 찾아야할 문자
cur = I
for i, char in enumerate(s):
    # 찾은 문자가 찾아야할 문자와 일치하지 않거나 마지막 인덱스 탐색 중이라면
    if char != cur or i == lng - 1:
        # 마지막으로 일치한 문자가 O 였다면 I였던 인덱스로 맞춰준다
        if char == O:
            pn -= 1

        pn //= 2
        # pn이 탐색 패턴보다 긴 경우에만 추가
        if pn >= N:
            cnt += pn - N + 1
        # 탐색 정보 초기화
        pn = 0
        cur = I

    if char == cur:
        pn += 1
        cur = dc[pn % 2]

print(cnt)

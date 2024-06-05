import sys

input = sys.stdin.readline
s = input().strip()

"""
1. 크로아티아 알파벳을 기준으로 split
    -> 제거된 알파벳 수 = split된 배열 길이 -1
2. split배열을 다시 string으로 합쳐서 길이-1과 함께 리턴
    -> 그냥 합치면 별개의 알파벳이 크로아티아 알파벳으로 변경될 수 있음
    -> ex) lnjj의 경우
        -> l / nj / j로  expect : 3
        -> nj 제거 후 lj가 return되므로 nj / lj output : 2
    -> 문자를 합칠 때 크로아티아 알파벳에 사용되지 않는 구분자를 넣어서 재결합
3. 크로아티아 알파벳을 모두 세어 준 뒤, 구분자를 제거한 남은 문자열의 길이만큼 더하면 정답 
"""

cnt = 0
patterns = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]


def remove_pattern(string, pattern):
    s = string.split(pattern)

    return [len(s) - 1, ".".join(s)]


for pattern in patterns:
    count, word = remove_pattern(s, pattern)

    cnt += count
    s = word

for char in s:
    if char == ".":
        cnt -= 1

print(cnt + len(s))

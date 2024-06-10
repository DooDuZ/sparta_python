import sys
from collections import defaultdict


input = sys.stdin.readline

N = int(input())
word = input().strip()

alpha = defaultdict(int)

for w in word:
    alpha[w] = alpha[w] + 1

answer = 0
for i in range(N - 1):
    a = defaultdict(int)
    w = input().strip()

    if abs(len(word) - len(w)) >= 2:
        continue

    # 딥카피 어케하는데...
    for c in word:
        a[c] = a[c] + 1

    cnt = 0

    # 일치 단어 카운팅
    for c in w:
        if c in a and a[c] > 0:
            a[c] -= 1
            cnt += 1

    # 기준 단어가 더 길면 비교단어의 모든 단어가 일치해야함
    if len(word) > len(w) and cnt == len(w):
        answer += 1
    # 비교 단어가 더 길면 같은 단어의 수가 기준 단어 길이와 일치해야함
    elif len(w) > len(word) == cnt:
        answer += 1
    # 길이가 똑같으면 모든 단어가 같거나 한 글자만 달라야함
    elif len(word) == len(w) and (cnt == len(w) or cnt == len(w) - 1):
        answer += 1

print(answer)

"""
2
AABCCD
ABBCDD

2
ABCCD
ABCDD

2
D
DDD

6
DOG
DO
GOD
DOH
DDOG
D


10
DOG
DOL
A
D
O
OL
OG
DOOR
OUG
GUE

10
ABABA
BBAAC
BBAAD
BBAAE
BBAAB
ACQAC
LKJDS
OKWLN
OKNLS
PONLM

answer 4

10
ABAAC
ABAA
ABAC
ABAB
ABAAA
ABCAA
ABSAC
AABBB
AA
ABC

answer 5


ABAA
ABAC
ABAAA
ABCAA
ABSAC
"""

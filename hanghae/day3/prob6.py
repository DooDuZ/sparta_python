import sys
from itertools import combinations

n, m = list(map(int, sys.stdin.readline().rstrip().split()))
numbers = [i + 1 for i in range(n)]
answer = []

# 조합 얻기
# numbers가 오름차순이기 때문에 어짜피 순서대로 나옴
comb = list(combinations(numbers, m))

# 조합 문자열 가공해서 answer에 넣기
for c in comb:
    answer.append(" ".join(str(x) for x in c))

# 다시 합쳐서 출력
print("\n".join(a for a in answer))

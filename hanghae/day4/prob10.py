import sys

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

rotate = [[] for _ in range(m)]

for _ in range(n):
    s = input().strip()
    for i in range(m):
        rotate[i].append(s[i])

# 입력된 문자를 돌려서 세로로 저장한다
vertical = ["".join(l) for l in rotate]


# 행 범위를 인덱스로 탐색
def binary_search(start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    # 중간부터 끝까지 중복이 없다면 시작점을 중간 뒤로 밀어준다
    if check_duplicate(mid, n):
        start = mid + 1
    # 중복이 있었다면 끝점 당겨오기
    else:
        end = mid

    return binary_search(start, end)


# 문자 중복 체크
def check_duplicate(s, e):
    words = set()

    for i in range(m):
        w = vertical[i][s:e]
        if w in words:
            return False
        words.add(w)

    return True


print(binary_search(0, n) - 1)

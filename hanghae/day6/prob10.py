import sys

input = sys.stdin.readline


def get_input():
    params = []

    n, m = list(map(int, input().strip().split()))

    for _ in range(2):
        matrix = []
        for i in range(n):
            matrix.append([x for x in input().strip()])
        params.append(matrix)

    return params


# 어짜피 모든 값을 맞춰야한다
# 한쪽 방향으로 셀을 탐색하며 다른 값이 나오면 뒤집으면서 진행 / 한 행씩 맞추면서 내려가기
# 값이 맞춰진 행은 다시 flip할 필요가 없으므로, 이 방법은 항상 최소값만 반환한다
def solution(params):
    # 비교
    def equals(matrix_a, matrix_b):
        for i in range(n):
            for j in range(m):
                if matrix_a[i][j] != matrix_b[i][j]:
                    return False
        return True

    # 3x3 구간 뒤집기
    def flip(matrix, row, col):
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                # matrix[i][j] ^= 1 문자열이라 안될듯
                matrix[i][j] = "1" if matrix[i][j] == "0" else "0"

    answer = 0

    A, B = params
    n, m = len(A), len(A[0])

    # index, index + 1, index + 2 값까지 검사해야하므로 -2
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                answer += 1

    if not equals(A, B):
        answer = -1

    return answer


print(solution(get_input()))

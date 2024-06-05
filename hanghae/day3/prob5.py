import sys

a1, a0 = list(map(int, sys.stdin.readline().rstrip().split()))
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())


def f(n):
    return a1 * n + a0


# g(n) = n 이지만 문제에선 c를 항상 곱해서 사용함
def g(n):
    return c * n


# a1이 c보다 크면 g(n)이 더 큰 경우는 없음
if a1 > c:
    print(0)
# a1 == c거나 a1 < c라면 초항을 넣은 값만 비교하면 된다
else:
    print(0 if f(n0) > g(n0) else 1)

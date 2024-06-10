import sys

s = sys.stdin.readline().rstrip()
N = int(s)

digit = [0 for _ in range(10)]
digit_num = [int(i) for i in s]
# 1의자리부터 셀 것이므로 reverse
digit_num.reverse()

# 자릿수별 배수, 1의자리부터 시작하므로 1
cnt = 1

while N > 0:
    for i in range(10):
        digit[i] += N // 10 * cnt

    M = N % 10

    digit[N // 10] += M

    for i in range(M + 1):
        digit[i] += cnt

    digit[0] -= cnt

    N //= 10
    cnt *= 10

print(digit)

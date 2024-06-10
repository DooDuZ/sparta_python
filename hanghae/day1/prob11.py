import sys
import math

N = int(sys.stdin.readline().rstrip())
cnt = [0]


def get_digit_zero_cnt(idx):
    ret = cnt[idx]

    print("내부임")

    print(idx)
    print(ret)

    for i in range(idx):
        print(math.pow(10, i))
        ret -= int(math.pow(10, i))

    print(ret)
    return ret


def pow(num, i):
    total = 1

    for _ in range(i):
        total *= num

    return total


idx = 1
while idx < len(str(N)) + 1:
    cnt.append(cnt[idx - 1] * 10 + int(pow(10, idx - 1)))
    idx += 1

digit_cnt = [0 for _ in range(10)]

# 자릿수 최댓값 ex) 3자리수 최대값인 999
# 현재 cnt는 각 자리수별로 가지게되는 최대값으로 맞춰짐 / 0 제외
c_digit = 1

while N > 0:
    s = 0
    c = N % 10

    while s <= c:
        if s != 0:
            digit_cnt[s] += int(pow(10, c_digit - 1))
            for i in range(10):
                digit_cnt[i] += cnt[c_digit - 1]
        else:
            digit_cnt[s] += get_digit_zero_cnt(c_digit - 1)

        s += 1

    c_digit += 1
    N //= 10

print(digit_cnt)

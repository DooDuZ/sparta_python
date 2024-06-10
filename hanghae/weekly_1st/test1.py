import sys

input = sys.stdin.readline

N = int(input())
switches = [0]

switches.extend(list(map(int, input().strip().split())))

M = int(input())


def check_multiple(num, s):
    idx = num
    while idx <= N:
        s[idx] += 1
        s[idx] %= 2
        idx += num


def check_sym(num, s):
    s[num] += 1
    s[num] %= 2
    lng = 1
    while num - lng > 0 and num + lng <= N:
        if s[num - lng] == s[num + lng]:
            s[num - lng] += 1
            s[num - lng] %= 2
            s[num + lng] += 1
            s[num + lng] %= 2
            lng += 1
        else:
            break


for _ in range(M):
    gender, num = list(map(int, input().strip().split()))
    if gender == 1:
        check_multiple(num, switches)
    else:
        check_sym(num, switches)

for i in range(1, N, 20):
    print(" ".join(str(x) for x in switches[i : i + 20]))

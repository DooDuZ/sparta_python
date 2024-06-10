import sys

N = int(sys.stdin.readline())
MOD = 1_000_000_007

names = [sys.stdin.readline().rstrip() for _ in range(N)]
facto = [0 for _ in range(3000)]

# 정렬된 상태에서 시작해야 같은 패턴을 가진 문자를 길이별로 잘라낼 수 있음
names.sort()


def count_of_sort(s, e, lng):
    ret = 1
    group = 0

    check_short = False

    for i in range(s, e):
        if len(names[i]) <= lng:
            s += 1
            check_short = True
            continue

        last_alp = names[s][lng]

        if names[i][lng] != last_alp:
            ret = multiple(ret, count_of_sort(s, i, lng + 1))
            s = i
            group += 1

        # 끝날 때 남은 그룹 로직 실행
        if (i + 1) == e:
            ret = multiple(ret, count_of_sort(s, e, lng + 1))
            group += 1

    # 짧아서 패스된 문자가 있다면, 다음 로직으로 넘어가지 않은 별도의 그룹이 있다
    if check_short:
        group += 1

    ret = multiple(ret, factorial(group))

    return ret


def factorial(n):
    if n == 1 or n == 0:
        return 1

    if facto[n] == 0:
        facto[n] = n * factorial(n - 1) % MOD

    return facto[n]


def multiple(a, b):
    return a * b % MOD


print(count_of_sort(0, N, 0))

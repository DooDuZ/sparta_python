import sys

input = sys.stdin.readline

m = int(input())
numbers = [[0]]
numbers[0].extend(list(map(int, input().strip().split())))

q = int(input())


def set_numbers():
    for i in range(1, 20):
        for j in range(m + 1):
            numbers[i][j] = numbers[i - 1][numbers[i - 1][j]]


def get_f(n, x):
    idx, minus = get_minus(n)

    x = numbers[idx][x]

    if n - minus == 0:
        return x
    elif n - minus == 1:
        return numbers[0][x]

    return get_f(n - minus, x)


def get_minus(n):
    double = 1
    cnt = 0

    while n >= double * 2:
        double *= 2
        cnt += 1

    return [cnt, double]


# 50만의 log2 == 19.xxxxx
for i in range(20):
    numbers.append([0 for _ in range(m + 1)])


set_numbers()

answer = []

for i in range(q):
    n, x = list(map(int, input().strip().split()))
    answer.append(get_f(n, x))


print("\n".join(str(x) for x in answer))

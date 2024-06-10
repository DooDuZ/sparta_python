import sys

alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
N, M = list(map(int, sys.stdin.readline().split()))

index = dict()

for i in range(N, M + 1):
    s = str(i)
    alp_num = ""

    for c in s:
        alp_num += alp[int(c)]

    index[alp_num] = i

sorted_alp = sorted(list(index.items()), key=lambda x: x[0])

answer = ""

for i, N in enumerate(sorted_alp):
    answer += str(N[1])
    answer += " "
    if i % 10 == 9:
        answer += "\n"

print(answer)

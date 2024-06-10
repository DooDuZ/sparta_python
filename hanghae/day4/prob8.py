import sys

input = sys.stdin.readline

O, I, IO = "O", "I", "IO"

N = int(input())


# 초기 패턴
def get_pattern(n):
    return "".join(["".join([IO for _ in range(n)]), I])


pattern = get_pattern(N)
lng = int(input())
s = input().strip()

convert_string = s.replace(IO, "-")

cnt = 0
pn = 0
for c in convert_string:
    if c == "-":
        pn += 1
    else:
        if c == O:
            pn -= 1

        if pn >= N:
            cnt += pn - N + 1

        pn = 0

print(cnt)

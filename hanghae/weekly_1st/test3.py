import sys

input = sys.stdin.readline

ip = input().strip().split(":")

cnt = 8
for num in ip:
    if num != "":
        cnt -= 1


ret = []

for i, num in enumerate(ip):

    zero = ""
    if num == "":
        while cnt > 0:
            ret.append("0000")
            cnt -= 1
            if cnt > 0:
                i += 1
        continue

    if len(num) < 4:
        for _ in range(4 - len(num)):
            zero += "0"

    ret.append(zero + num)


print(":".join(ret))

"""
25:09:1985::091:4846:374:bb
"""

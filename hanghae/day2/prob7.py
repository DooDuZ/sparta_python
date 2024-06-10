import sys

N = int(sys.stdin.readline())

extensions = dict()

for _ in range(N):
    extension = sys.stdin.readline().rstrip().split(".")[1]

    if extension in extensions:
        extensions[extension] += 1
    else:
        extensions[extension] = 1

sorted_list = sorted(list(extensions.items()))

print("\n".join(" ".join(str(e) for e in extn) for extn in sorted_list))

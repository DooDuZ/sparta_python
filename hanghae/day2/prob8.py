import sys

s = sys.stdin.readline().rstrip()

store = set()

for i in range(len(s)):
    for j in range(len(s)):
        store.add(s[j:j+i+1])

print(len(store))
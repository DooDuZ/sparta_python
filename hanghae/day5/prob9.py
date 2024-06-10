import sys

input = sys.stdin.readline


class SegmentTree:
    def __init__(self, numbers):
        self.numbers = numbers
        self.root = self.Node(0, len(numbers) - 1, self.numbers)

    class Node:
        def __init__(self, start, end, numbers):
            self.start = start
            self.end = end
            self.min = float("inf")
            self.left = None
            self.right = None
            self.numbers = numbers
            self.init()

        def init(self):
            if self.start != self.end:
                mid = (self.start + self.end) // 2
                self.left = SegmentTree.Node(self.start, mid, self.numbers)
                self.right = SegmentTree.Node(mid + 1, self.end, self.numbers)
                self.min = min(self.left.min, self.right.min)
            else:
                self.min = self.numbers[self.start]

        def search(self, s, e):
            if s == self.start and e == self.end:
                return self.min

            ret = 1_000_000_000

            if s <= self.left.end:
                ret = min(ret, self.left.search(s, min(e, self.left.end)))

            if e >= self.right.start:
                ret = min(ret, self.right.search(max(s, self.right.start), e))

            return ret


N, M = list(map(int, input().strip().split()))
numbers = [int(input()) for _ in range(N)]

answer = []

segmentTree = SegmentTree(numbers)

for i in range(M):
    a, b = list(map(int, input().strip().split()))
    answer.append(segmentTree.root.search(a - 1, b - 1))

print("\n".join(str(x) for x in answer))

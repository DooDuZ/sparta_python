import sys
from heapq import heappop, heapify, heappush

input = sys.stdin.readline


# 데이터 크기 최대 1500*1500 225만
# 메모리 제한 12mb, 2250000*4byte = 900만 -> 9mb쯤?
# 좌표값 같이 넘겨서 열 별로 pop하려니 메모리 초과 난다
# 그냥 n개마다 뽑자...
# n개마다 뽑아도 메모리 초과난다. 입력 한줄마다 돌리자
# 입력별로 최소값 뽑아서 n^n - n 일때 멈추자
def solution():
    n = int(input())

    heap = []
    heapify(heap)

    cnt = n * n
    for i in range(n):
        row = list(map(int, input().strip().split()))

        for number in row:
            heappush(heap, number)
            if len(heap) > n:
                heappop(heap)
                cnt -= 1
            if cnt == n:
                return heappop(heap)


print(solution())

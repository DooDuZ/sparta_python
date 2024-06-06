import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline


class ProblemHeap:
    # 저장되어있는지 체크할 boolean 리스트
    is_saved = [False for _ in range(100001)]
    # 레벨 최신화 리스트
    levels = [0 for _ in range(100001)]

    # 문제 필요조건엔 없음. len(heap) 체크용
    elements_count = 0

    max_heap = []
    min_heap = []

    def add(self, num, level):
        if not self.is_saved[num]:
            self.elements_count += 1

        self.is_saved[num] = True
        self.levels[num] = level

        # maxheap은 난이도 / 문제번호 모두 내림차순
        heappush(self.max_heap, [-level, -num])
        heappush(self.min_heap, [level, num])

    def solved(self, problem_num):
        self.is_saved[problem_num] = False
        self.elements_count -= 1

    def recommend(self, direction):
        target_heap = self.max_heap

        if direction == -1:
            target_heap = self.min_heap

        # max heap의 데이터는 음수이므로 모두 abs
        while not self.is_saved[abs(target_heap[0][1])] or self.levels[
            abs(target_heap[0][1])
        ] != abs(target_heap[0][0]):
            heappop(target_heap)

        return abs(target_heap[0][1])


def get_input():
    params = []

    n = int(input())

    problems = []
    for _ in range(n):
        problems.append(list(map(int, input().split())))

    params.append(problems)
    m = int(input())

    commands = []
    for _ in range(m):
        cmd = input().strip().split()
        if cmd[0] != "add":
            commands.append([cmd[0], int(cmd[1])])
        else:
            commands.append([cmd[0], int(cmd[1]), int(cmd[2])])

    params.append(commands)
    return params


def solution(params):
    answer = []

    problems, commands = params

    problem_heap = ProblemHeap()

    for problem in problems:
        problem_heap.add(problem[0], problem[1])

    for command in commands:
        cmd = command[0]

        if cmd == "add":
            problem_heap.add(command[1], command[2])
        elif cmd == "solved":
            problem_heap.solved(command[1])
        else:
            answer.append(str(problem_heap.recommend(command[1])))

    return answer


print("\n".join(solution(get_input())))


"""
1
1 2
4
add 2 1
solved 1
add 1 3
recommend 1

2
1000 1
2000 1
4
recommend -1
solved 1000
add 1000 1000
recommend -1


2
101 1
103 3
3
solved 103
add 103 3
recommend 1

2
1000 1
2000 1
2
recommend -1
recommend 1
"""

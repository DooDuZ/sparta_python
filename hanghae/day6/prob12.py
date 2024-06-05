import sys

input = sys.stdin.readline


def get_input():
    params = []
    for _ in range(2):
        params.append(input().strip())

    return params


def solution(params):
    # 탐색한 문자까지 bomb와 일치한 길이를 저장
    counter = []
    # 문자열 가공을 위한 stack
    characters = []

    string, bomb = params

    # 탐색한 곳까지 연속하여 폭탄 문자와 일치한 개수
    count = 0
    for c in string:
        if c == bomb[count]:
            count += 1
        else:
            if c == bomb[0]:
                count = 1
            else:
                count = 0
        counter.append(count)
        characters.append(c)

        # 연속해서 일치한 값이 bomb의 길이와 같아지면
        if count == len(bomb):
            for i in range(count):
                # 길이만큼 pop
                counter.pop()
                characters.pop()
                # counter stack에 값이 남아있다면 해당 값부터 다시 시작, 없다면 처음부터 다시 시작
            if counter:
                count = counter[-1]
            else:
                count = 0

    if not characters:
        return "FRULA"

    return characters


print("".join(solution(get_input())))

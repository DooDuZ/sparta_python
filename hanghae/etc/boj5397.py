import sys

input = sys.stdin.readline


def get_input():
    params = []

    T = int(input())

    for _ in range(T):
        params.append(input().strip())

    return params


def solution(param):
    def shift_left():
        if password:
            buffer.append(password.pop())

    def shift_right():
        if buffer:
            password.append(buffer.pop())

    def delete():
        if password:
            password.pop()

    operators = {"<": shift_left, ">": shift_right, "-": delete}

    password = []

    buffer = []

    for c in param:
        if c in operators:
            operators[c]()
        else:
            password.append(c)

    while buffer:
        password.append(buffer.pop())

    return "".join(password)


if __name__ == "__main__":
    params = get_input()
    for param in params:
        print(solution(param))

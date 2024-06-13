import sys

input = sys.stdin.readline


def get_input():
    params = []

    king, stone, cmd = list(input().strip().split())

    commands = []

    for i in range(int(cmd)):
        commands.append(input().strip())

    params.append(king)
    params.append(stone)
    params.append(commands)

    return params


def check_range(row, col):
    if 1 <= row <= 8 and 1 <= col <= 8:
        return True
    return False


def to_number_coord(coord):
    return tuple([ord(coord[0]) - ord("A") + 1, int(coord[1])])


def to_alp_coord(coord):
    return chr(coord[0] - 1 + ord("A")) + str(coord[1])


def solution(params):
    king, stone, commands = params

    # 계산 간편화 위해 숫자 좌표로 변환
    # 튜플을 k,s라는 변수에 저장해서 대입하니 함수 밖으로 값이 반영되지 않는다
    # 튜플은 참조 변수가 아닌가...?
    coords = [to_number_coord(king), to_number_coord(stone)]

    # idx 0 = king, idx = 1 = stone
    def move(cmd, idx):
        # 각 명령 별 변화량 dictionary 매핑
        cmd_map = {
            "B": [0, -1],
            "T": [0, 1],
            "R": [1, 0],
            "L": [-1, 0],
            "RB": [1, -1],
            "LB": [-1, -1],
            "RT": [1, 1],
            "LT": [-1, 1],
        }

        x, y = coords[idx]

        nx = x + cmd_map[cmd][0]
        ny = y + cmd_map[cmd][1]

        # 다음 좌표가 유효하지 않으면 return
        if not check_range(nx, ny):
            return False

        # 이동한 위치에 다른 물체가 있는 경우 -> 항상 0으로 시작되므로 킹이 이동한 자리에 stone이 있는 경우
        if (nx, ny) in coords:
            if not move(cmd, idx + 1):
                return False

        # 이동한 물체의 위치 저장
        coords[idx] = (nx, ny)
        return True

    for command in commands:
        move(command, 0)

    return [to_alp_coord(coords[0]), to_alp_coord(coords[1])]


if __name__ == "__main__":
    print(*solution(get_input()), sep="\n")

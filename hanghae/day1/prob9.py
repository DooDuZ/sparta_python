import sys

'''
https://www.acmicpc.net/problem/2641

1. 커맨드의 실행 순서가 같다면 시작 지점이 다르더라도 같은 도형을 그릴 수 있음
2. 기존 커맨드를 거꾸로, 반대 방향으로 그리면 같은 도형을 그릴 수 있음
3. 문자열로 변환 후 in 을 통해 포함 여부를 알 수 있음
    * 모양 수열의 최대 길이가 50이므로 사용할 수 있으나 기본적으로 n*n 시간이 소모될 것으로 보임
    * 데이터 값의 범위가 커지면 탐색 알고리즘을 in에서 다른 걸로 바꿔야할 수 있음
'''

n = int(sys.stdin.readline())

# 정방향
figure = list(map(int, sys.stdin.readline().split()))
# 역방향
figure_r = []

# 커맨드 반대 방향으로 돌려주는 배열
reverse = [0, 3, 4, 1, 2]

# 기존 커맨드를 뒤에서부터 반대로 뒤집어서 reverse 도형 배열에 추가
for i in range(len(figure)-1, -1, -1):
    figure_r.append(reverse[ figure[i] ])

# 기존 문자열을 두배로 늘려서 범위 탐색 할 수 있도록 하는 string 생성
data = ''.join(map(str, figure)) * 2
data_r = ''.join(map(str, figure_r)) * 2

# 비교 모양의 수 입력 받기
m = int(sys.stdin.readline())

# 정답 저장 리스트
answer = []

for i in range(m):
    # rstrip을 통해 \n 제거
    r = sys.stdin.readline().rstrip()
    # 입력 받은 문자열을 공백 제거 후 문자열로 합쳐준다
    sequence = (''.join(r.split()))

    # 정방향 / 혹은 역방향으로 그린 것과 같은 모양이라면
    if sequence in data or sequence in data_r:
        # 정답 리스트에 추가
        answer.append(r)

# 출력
print(len(answer))
for f in answer:
    print(f)
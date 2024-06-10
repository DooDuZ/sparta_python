import sys

s = sys.stdin.readline().strip()
N = int(s)

# 자릿수별 등장 횟수 저장 리스트
digit = [0 for _ in range(10)]

# 자릿수별 각 숫자의 최대 등장 횟수
# ex) 3자리 숫자에서 1~9가 등장할 수 있는 최대 횟수 = cnt[3] = 300
cnt = [0, 1]


# math.pow int감싸는거 귀찮아서 직접 구현
def pow(num, idx):
    ret = 1

    for i in range(idx):
        ret *= num

    return ret


# cnt 배열 초기화
# 이전 자릿수 등장횟수 * 9 + 10^해당 자릿수 + 누적합용 이전 cnt[i]
for i in range(1, len(s)):
    cnt.append(pow(10, i) + cnt[i] * 9 + cnt[i])

# 전체 다 계산한 값으로 채워주고
for i in range(10):
    digit[i] = cnt[len(s)]

# 0은 각 자릿수별로 1번씩 덜 등장하므로 차감해준다
for i in range(len(s)):
    digit[0] -= pow(10, i)


# 문자로 받은 데이터에 접근 편하게 하기위해 선언한 인덱스
idx = 0
# cnt 배열에 접근할 때 쓸 인?덱스
cur_digit = len(s) - 1
while cur_digit >= 0:
    # 각 자릿수를 모두 9로 채운 숫자에서 차감 시작
    start = 9

    # 현재 자릿수가 주어진 숫자와 일치할 때까지 차감
    while start > int(s[idx]):
        # 날리는 자릿수 카운트 차감ex) 999면 100
        digit[start] -= pow(10, cur_digit)

        # 현재 진행하는 앞자리 숫자들 차감
        for i in range(idx):
            digit[int(s[i])] -= pow(10, cur_digit)

        # 현재 자릿수에 대한 누적합 차감
        for i in range(10):
            digit[i] -= cnt[cur_digit]

        # 현재 자릿수 숫자 내려주기
        start -= 1

    # 자릿수 처리가 다 끝났다면 문자 접근 인덱스/cnt배열 접근 인덱스 증감
    idx += 1
    cur_digit -= 1

print(*digit)

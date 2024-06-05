import sys


input = sys.stdin.readline


N = int(input())


# 숫자는 최대 100만까지지만 부분 수열은 10만까지만 고를 수있다
dp = [0 for _ in range(1000001)]
for i in range(10):
    dp[i] = -1

"""
recursion error...
파이썬으론 재귀 쓰면 안될 거 같다


def set_dp(n):
    # 10 이하에선 패배 처리
    if n < 10:
        return -1
    
    # 찾는 값이 비어있으면
    if dp[n] == 0:
        # 연속적인 부분 수열을 가져온다
        subset = list(get_subset(n))

        nums = []
        # 부분 수열 순회
        for sub in subset:
            # 현재 값에서 부분 수열을 뺀 값을 dp에서 찾아주고
            res = set_dp(n - sub)
            # -1이 리턴된다면 상대방의 패배
            if res == -1:
                nums.append(sub)
        
        담은 값 정렬
        nums.sort()
        
        if nums:
            dp[n] = nums[0]
        #배열이 비어있다면 이길 수 없는 경우. 패배 처리
        else:
            dp[n] = -1

    return dp[n]
"""


# 재귀 반복문 변환 버전
def set_dp(n):
    for i in range(10, n + 1):
        subset = list(get_subset(i))

        nums = []

        for sub in subset:
            if dp[i - sub] == -1:
                nums.append(sub)

        nums.sort()

        if nums:
            dp[i] = nums[0]
        else:
            dp[i] = -1

    return dp[n]


def get_subset(n):
    s = str(n)
    ret = set()

    for lng in range(1, len(s)):
        for i in range(len(s) - lng + 1):
            num = int(s[i : i + lng])
            if num != 0:
                ret.add(num)

    return ret


print(set_dp(N))

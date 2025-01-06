
import sys
input = sys.stdin.readline

S = input().strip()  # 입력 문자열에서 끝의 공백 제거
L = len(S)

# dp 배열 초기화: 최소 분할 횟수를 저장하는 배열
dp = [2500 for _ in range(L + 1)]
dp[-1] = 0  # 아무것도 없는 상태에서의 최소 분할 횟수는 0

# 팰린드롬 여부를 저장하는 2차원 배열 초기화
is_p = [[0 for j in range(L)] for i in range(L)]

# 길이 1짜리 팰린드롬 처리
for i in range(L):
    is_p[i][i] = 1

# 길이 2짜리 팰린드롬 처리
for i in range(1, L):
    if S[i - 1] == S[i]:
        is_p[i - 1][i] = 1

# 길이 3 이상짜리 팰린드롬 처리
for i in range(3, L + 1):  # 길이 i
    for start in range(L - i + 1):
        end = start + i - 1
        if S[start] == S[end] and is_p[start + 1][end - 1]:
            is_p[start][end] = 1  # 팰린드롬으로 표시

# 최소 분할 횟수 계산
for end in range(L):
    for start in range(end + 1):
        if is_p[start][end]:  # start부터 end까지가 팰린드롬인 경우
            dp[end] = min(dp[end], dp[start - 1] + 1)

# 결과 출력
print(dp[L - 1])

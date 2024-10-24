
T = int(input())
dp = [0] * 101  # 최대 100

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]


for tc in range(1, T+1):
    N = int(input())

    print(dp[N])

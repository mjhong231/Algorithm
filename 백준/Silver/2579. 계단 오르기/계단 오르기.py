import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 301
for i in range(1, N+1):
    arr[i] = int(input())

dp = [0] * 301
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])

for j in range(4, N+1):
    dp[j] = max(dp[j-3] + arr[j-1] + arr[j], dp[j-2] + arr[j])

print(dp[N])

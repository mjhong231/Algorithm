
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for coin in coins:
    if K >= coin:
        cnt += K // coin
        K %= coin


print(cnt)
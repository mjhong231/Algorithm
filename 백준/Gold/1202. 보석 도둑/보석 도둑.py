
import sys
input = sys.stdin.readline

import heapq

N, K = map(int, input().split())
gem = []
bags = []
for _ in range(N):
    heapq.heappush(gem, list(map(int, input().split())))

for _ in range(K):
    bags.append(int(input()))
bags.sort()

ans = 0
temp = []
for bag in bags:
    while gem and bag >= gem[0][0]:
        heapq.heappush(temp, -heapq.heappop(gem)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not gem:
        break
print(ans)
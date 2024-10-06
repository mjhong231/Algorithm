
import heapq

import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(1, N+1):
    num = int(input())
    if num != 0:
        heapq.heappush(q, num)
    else:
        try:
            print(heapq.heappop(q))
        except:
            print(0)


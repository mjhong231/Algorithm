import heapq

import sys
input = sys.stdin.readline

N = int(input())
q = []

for _ in range(1, N+1):
    num = int(input())
    if num != 0:
        heapq.heappush(q, (abs(num), num))

    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)

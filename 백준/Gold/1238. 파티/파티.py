import heapq

import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())  # N은 노드 X는 도착점 M은 단방향 간선
lst = [[] for _ in range(N+1)]  # 학생은 1번부터


for _ in range(1, M+1):
    start, end, time = map(int, input().split())
    lst[start].append((time, end))

def dik(start):
    dp = [float('inf')] * (N + 1)  # 비교테이블
    hq = []
    dp[start] = 0
    heapq.heappush(hq, (0, start))  # (시간, 도로)

    while hq:
        now, node = heapq.heappop(hq)

        if dp[node] < now:
            continue

        for time_cost, road in lst[node]:
            next_time = now + time_cost

            if next_time < dp[road]:
                dp[road] = next_time
                heapq.heappush(hq, (next_time, road))

    return dp

result = 0
back = dik(X)

for i in range(1, N+1):
    go = dik(i)
    result = max(result, go[X] + back[i])

print(result)


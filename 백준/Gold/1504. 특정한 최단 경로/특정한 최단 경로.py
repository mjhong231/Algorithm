
import sys
input = sys.stdin.readline

import heapq

N, E = map(int, input().split())  # 정점의 개수 N, 간선의 개수 E
lst = [[] for _ in range(N+1)]  # 인접리스트
for _ in range(E):
    a, b, c = map(int, input().split())  # c가 가중치
    lst[a].append((c, b))
    lst[b].append((c, a))

v1, v2 = map(int, input().split())

def dik(start):
    dp = [float('inf')] * (N+1)  # 비교테이블
    hq = []
    dp[start] = 0
    heapq.heappush(hq, (0, start))  # (가중치합, 위치)

    while hq:
        cur_sum, cur_pos = heapq.heappop(hq)

        if cur_sum > dp[cur_pos]:
            continue

        for next_sum, next_node in lst[cur_pos]:
            new_sum = cur_sum + next_sum

            if new_sum < dp[next_node]:
                dp[next_node] = new_sum
                heapq.heappush(hq, (new_sum, next_node))


    return dp


origin = dik(1)
v1_dis = dik(v1)
v2_dis = dik(v2)

v1_path = origin[v1] + v1_dis[v2] + v2_dis[N]
v2_path = origin[v2] + v2_dis[v1] + v1_dis[N]


result = min(v1_path, v2_path)
print(result if result < float('inf') else -1)

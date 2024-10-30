import sys
input = sys.stdin.readline

import heapq


n, m = map(int, input().split())  # 정점의 개수 n, 간선수 m
lst = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((c, b))  # c는 가중치
    lst[b].append((c, a))
s, t = map(int, input().split())


def dik(start):
    hq = []
    dp = [float('inf')] * (n+1)
    dp[start] = 0
    heapq.heappush(hq, (0, start))  # (가중치합, 시작지점)

    while hq:
        cur_sum, cur_pos = heapq.heappop(hq)

        if cur_sum > dp[cur_pos]:
            continue

        for next_sum, next_pos in lst[cur_pos]:
            new_sum = cur_sum + next_sum
            if new_sum < dp[next_pos]:
                dp[next_pos] = new_sum
                heapq.heappush(hq, (new_sum, next_pos))

    return dp[t]

print(dik(s))
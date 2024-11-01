import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

lst = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    lst[s].append((cost, e))

start, end = map(int, input().split())

def dik(start, end):
    hq = []
    dp = [float('inf')] * (n + 1)
    dp[start] = 0
    heapq.heappush(hq, (0, start))
    
    # 경로 추적을 위한 리스트
    path = [-1] * (n + 1)

    while hq:
        cur_cost, now = heapq.heappop(hq)

        if cur_cost > dp[now]:
            continue

        for next_cost, next_arr in lst[now]:
            new_cost = cur_cost + next_cost
            if new_cost < dp[next_arr]:
                dp[next_arr] = new_cost
                path[next_arr] = now  # 이전 도시를 기록
                heapq.heappush(hq, (new_cost, next_arr))

    # 최소 비용 경로 추적
    route = []
    temp = end
    while temp != -1:
        route.append(temp)
        temp = path[temp]
    route.reverse()  # 경로를 거꾸로 뒤집음

    return dp[end], route

# 최소 비용, 경로를 구하고 출력
min_cost, route = dik(start, end)
print(min_cost)
print(len(route))
print(" ".join(map(str, route)))

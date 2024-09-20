import heapq



N = int(input())  #도시 수
M = int(input())  #버스 수
lst = [[] for _ in range(N+1)]

for _ in range(M):
    first, mid, cost = map(int, input().split())
    lst[first].append([mid, cost])

start, end = map(int, input().split())

costs = [float('inf')] * (N+1)

def dijkstra(start):
    costs[start] = 0
    q = [(0, start)]

    while q:
        cost, now = heapq.heappop(q)
        if costs[now] < cost:
            continue
        for next_city, next_cost in lst[now]:
            sum_cost = costs[now] + next_cost
            if costs[next_city] > sum_cost:
                costs[next_city] = sum_cost
                heapq.heappush(q, (sum_cost, next_city))

dijkstra(start)
print(costs[end])

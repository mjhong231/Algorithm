import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

dp = [float('inf')] * (V + 1)

arr = [[] for _ in range(V + 1)]

start = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((v, w))

def Dijkstra(start):
    hq = []
    dp[start] = 0
    heapq.heappush(hq, (0, start))  # (distance, node)

    while hq:
        distance, node = heapq.heappop(hq)

        if dp[node] < distance:
            continue

        for next_node, next_distance in arr[node]:
            new_distance = distance + next_distance

            if new_distance < dp[next_node]:
                dp[next_node] = new_distance
                heapq.heappush(hq, (new_distance, next_node))


Dijkstra(start)


for i in range(1, V + 1):
    print("INF" if dp[i] == float('inf') else dp[i])
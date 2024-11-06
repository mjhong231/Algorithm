import sys
input  = sys.stdin.readline

import heapq

n, m, r = map(int, input().split())  # n = 노드, m = 수색범위, r = 간선수
item = list(map(int, input().split()))  # 아이템 수
lst = [[] for _ in range(n+1)]  # 인접리스트
for tc in range(r):
    a, b, cost = map(int, input().split())  # cost 거리 가중치
    lst[a].append((cost, b))
    lst[b].append((cost, a))



def dik(start):
    hq = []
    heapq.heappush(hq, (0, start))  #거리 가중치, 현재 노드 위치
    arr[start] = 0

    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if arr[cur_node] < cur_cost:
            continue

        for next_cost, next_node in lst[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < arr[next_node]:
                arr[next_node] = new_cost
                heapq.heappush(hq, (new_cost, next_node))

cnt = 0
for i in range(1, n + 1):
    arr = [float('inf')] * (n + 1)
    dik(i)
    temp = 0
    for j in range(1, n+1):
        if m >= arr[j]:
            temp += item[j-1]

    cnt = max(cnt, temp)

print(cnt)
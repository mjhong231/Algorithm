from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())  # N: 가수의 수, M: 보조 PD의 수
graph = [[] for _ in range(N + 1)]  
indegree = [0] * (N + 1)  


for _ in range(M):
    order = list(map(int, input().split()))
    k = order[0]  # 가수의 수
    for i in range(1, k):
        a, b = order[i], order[i + 1]
        graph[a].append(b)
        indegree[b] += 1


q = deque()
result = []


for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    result.append(cur) 

    for neighbor in graph[cur]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            q.append(neighbor)

if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

lst = [[] for _ in range(N+1)]  # 인접리스트

indegree = [0] * (N+1)  # 간선수 카운팅할 배열

dp = [0] * (N+1)

q = deque()

min_t = [0]  # 최소 시간

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    min_t.append(arr[0])
    if arr[1] != 0:
        for j in range(2, len(arr)):
            lst[arr[j]].append(i)
            indegree[i] += 1


for node in range(1, N+1):
    if indegree[node] == 0:
        q.append(node)
        dp[node] = min_t[node]

while q:
    now = q.popleft()
    for i in lst[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + min_t[i], dp[i])
        if indegree[i] == 0:
            q.append(i)

print(max(dp))

from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
alist = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for tc in range(1, M+1):
    u, v = map(int, input().split())
    alist[u].append(v)
    alist[v].append(u)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        for i in range(len(alist[now])):
            next = alist[now][i]
            if visited[next] == 1: continue
            visited[next] = 1
            q.append(next)

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
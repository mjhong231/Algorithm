import sys
input = sys.stdin.readline

from collections import deque


C = int(input())  # 노드 수
N = int(input())  # 연결된 노드쌍
alist = [[] for _ in range(C+1)]
result = []

for tc in range(1, N+1):
    s, e = map(int, input().split())
    alist[s].append(e)
    alist[e].append(s)

def bfs(start):

    q = deque()
    q.append(1)
    used = [0] * (C+1)
    used[start] = 1

    while q:
        now = q.popleft()
        result.append(now)
        for i in range(len(alist[now])):
            next = alist[now][i]
            if used[next] == 1: continue
            used[next] = 1
            q.append(next)

bfs(1)
print(len(result)-1)
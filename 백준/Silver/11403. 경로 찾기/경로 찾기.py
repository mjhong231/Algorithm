
from collections import deque

import sys
input = sys.stdin.readline


def bfs(start):
    q = deque()
    q. append(start)

    while q:
        now = q.popleft()

        for i in range(N):
            if not used[start][i] and MAP[now][i]:
                q.append(i)
                used[start][i] = 1

N = int(input())

MAP = [list(map(int, input().split())) for _ in range(N)]
used = [[0] * N for _ in range(N)]

for j in range(N):
    bfs(j)

for u in used:
    print(*u)
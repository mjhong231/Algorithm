
import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split()) # 사다리 N, 뱀 M

MAP = [0] * 101
visited = [False] * 101

ladder = {}
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

snake = {}
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

def bfs(start):
    q = deque()
    q.append(start) # 시작지점 넣기
    visited[start] = True

    while q:
        now = q.popleft()

        for i in range(1, 7): # 주사위
            next = now + i

            if 0 < next <= 100:
                if next in ladder:
                    next = ladder[next]

                elif next in snake:
                    next = snake[next]

                if not visited[next]:
                    visited[next] = True
                    MAP[next] = MAP[now] + 1
                    q.append(next)


bfs(1)
print(MAP[100])
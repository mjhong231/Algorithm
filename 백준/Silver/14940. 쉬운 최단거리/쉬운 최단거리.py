
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N이 행(세로), M이 열(가로)

MAP = [list(map(int, input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

q = deque()

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            q.append((i, j))
            visited[i][j] = 0
        elif MAP[i][j] == 0:
            visited[i][j] = 0


def bfs():

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if MAP[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


bfs()

for row in visited:
    print(*row)

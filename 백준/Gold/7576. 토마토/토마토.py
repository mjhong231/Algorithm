from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())  # M 가로, N 세로

MAP = [list(map(int, input().split())) for _ in range(N)]

q = deque()

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

cnt = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and MAP[ny][nx] == 0:
                MAP[ny][nx] = MAP[y][x] + 1
                q.append([ny, nx])

bfs()
for row in MAP:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(row))

print(cnt - 1)
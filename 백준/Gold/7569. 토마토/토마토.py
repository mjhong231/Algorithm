from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split()) 

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dir = [(0, -1, 0), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

day = 0 

q = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoes[k][i][j] == 1:
                q.append((k, i, j))

def bfs():
    while q:
        z, x, y = q.popleft()
        for dx, dy, dz in dir:
            nx, ny, nz = x + dx, y + dy, z + dz
            if 0 <= nz < H and  0 <= nx < N and 0 <= ny < M and tomatoes[nz][nx][ny] == 0:
                tomatoes[nz][nx][ny] = tomatoes[z][x][y] + 1
                q.append((nz, nx, ny))

bfs()
for tomato in tomatoes:
    for toma in tomato:
        for t in toma:
            if t == 0:
                print(-1)
                exit(0)
        day = max(day, max(toma))
print(day - 1)


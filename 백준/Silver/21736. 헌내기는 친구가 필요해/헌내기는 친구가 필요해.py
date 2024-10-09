from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(input().strip()) for _ in range(N)]

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

cnt = 0

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'I':
            si, sj = i, j

visited = [[0]* M for _ in range(N)]
def bfs():
    global cnt
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 1
    while q:
        y, x = q.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if MAP[ny][nx] == 'O':
                    q.append((ny, nx))
                elif MAP[ny][nx] == 'P':
                    q.append((ny, nx))
                    cnt += 1
bfs()
print('TT' if cnt == 0 else cnt)
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(a, b):
    q = deque()
    q.append((a,b))
    while q:
        y, x = q.popleft()
        for dx, dy in dir:
            ny, nx = y + dy, x+dx
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = arr[y][x] + 1
                    q.append((ny,nx))
bfs(0, 0)
print(arr[N-1][M-1])
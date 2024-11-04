
import sys
input = sys.stdin.readline
from collections import deque

dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(y, x):
    cnt = 1
    q = deque()
    q.append((y, x))
    arr[y][x] = 0 # 방문처리

    while q:
        cy, cx = q.popleft()
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:
                arr[ny][nx] = 0
                cnt += 1
                q.append((ny, nx))
    return cnt

N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            lst.append(bfs(i, j))


lst.sort()
print(len(lst))
for l in lst:
    print(l)

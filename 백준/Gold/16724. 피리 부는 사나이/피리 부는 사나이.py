import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAP = [list(input().strip()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]
safezone = 0

def dfs(y, x):
    global safezone

    visited[y][x] = True
    temp.append((y, x))

    ny, nx = y, x
    if MAP[y][x] == 'U' and y > 0:
        ny -= 1
    elif MAP[y][x] == 'D' and y < N - 1:
        ny += 1
    elif MAP[y][x] == 'L' and x > 0:
        nx -= 1
    elif MAP[y][x] == 'R' and x < M - 1:
        nx += 1

    if visited[ny][nx]:
        if (ny, nx) in temp:
            safezone += 1
    else:
        dfs(ny, nx)

for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            temp = []
            dfs(y, x)

print(safezone)

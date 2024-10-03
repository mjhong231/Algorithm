
from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y, z):  
    q = deque()
    q.append((x,y,z))

    while q:
        x, y, z = q.popleft()
        if x == N - 1 and y == M - 1:  
            return visit[x][y][z]     
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:  
                if MAP[nx][ny] == 1 and z == 0 and visit[nx][ny][1] == 0:
                    visit[nx][ny][1] = visit[x][y][z] + 1  
                    q.append((nx, ny, 1))
                elif MAP[nx][ny] == 0 and visit[nx][ny][z] == 0:  
                    visit[nx][ny][z] = visit[x][y][z] + 1 
                    q.append((nx, ny, z))
    return -1



dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

N, M = map(int, input().split())

MAP = [list(map(int, input().strip())) for _ in range(N)]

visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]  

visit[0][0][0] = 1   

print(bfs(0, 0, 0,))



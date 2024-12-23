import sys
input = sys.stdin.readline

from collections import deque

def bfs(): # 외부 공기와 접촉한 치즈 찾기
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if MAP[ny][nx] >= 1: # 치즈가 있으면
                    MAP[ny][nx] += 1 # 접촉 체크
                else:
                    q.append((ny, nx)) # 치즈가 없으면 다음 탐색
                    visited[ny][nx] = True

def f(): # 치즈 녹이기
    melted = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] >= 3: # 2번 이상 공기와 접촉했으면 녹이기
                MAP[i][j] = 0
                melted += 1
            elif MAP[i][j] >= 2: # 한번만 접촉한 치즈는 초기화
                MAP[i][j] = 1
    return melted

N, M = map(int, input().split())  # N 세로격자(열) / M 가로격자 (행)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cycle = 0
MAP = [list(map(int, input().split())) for _ in range(N)]

time = 0

while True:
    bfs()
    melted = f()
    if melted:
        time += 1
    else:
        print(time)
        break
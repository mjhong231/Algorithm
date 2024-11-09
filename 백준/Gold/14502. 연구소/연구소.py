from collections import deque
import sys, copy
input = sys.stdin.readline



n, m = map(int, input().split()) # n은 세로(행), m은 가로(열)
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0 # 최대 비교할 변수 초기화

dir =[(-1, 0), (0, 1), (1, 0), (0, -1)]

def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 0:
                arr[y][x] = 1
                wall(cnt+1)
                arr[y][x] = 0

def bfs():
    global result
    test_arr = copy.deepcopy(arr)
    q = deque()

    for y in range(n):
        for x in range(m):
            if test_arr[y][x] == 2:
                q.append((y,x))

    while q:
        cy, cx = q.popleft()

        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < m and test_arr[ny][nx] == 0:
                test_arr[ny][nx] = 2
                q.append((ny, nx))

    safezone = 0
    for a in test_arr:
        safezone += a.count(0)

    result = max(result, safezone)

wall(0)
print(result)

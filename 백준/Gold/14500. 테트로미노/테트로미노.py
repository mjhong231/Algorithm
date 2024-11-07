n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

result = 0  

def dfs(y, x, temp, cnt):
    global result

    if cnt == 4:  # 탐색 완료
        result = max(result, temp)
        return

    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
            visited[ny][nx] = True  
            dfs(ny, nx, temp + MAP[ny][nx], cnt + 1)
            visited[ny][nx] = False  

def f(y, x):
    global result
    temp = MAP[y][x]
    arr = []
    
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m:
            arr.append(MAP[ny][nx])
    
    if len(arr) == 4:
        result = max(result, sum(arr) + temp - min(arr))

    elif len(arr) == 3:  # 3방향만 범위 안에 들어갈 경우 
        result = max(result, sum(arr) + temp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True  
        dfs(i, j, MAP[i][j], 1)
        visited[i][j] = False  
        f(i, j)

print(result)  


def pipe(y, x, now):
    global result
    if y == N-1 and x == N-1:
        result += 1
        return

    # 가로 방향 (0)
    if now == 0 or now == 2:
        if x + 1 < N and arr[y][x+1] == 0:
            pipe(y, x+1, 0)

    # 세로 방향 (1)
    if now == 1 or now == 2:
        if y + 1 < N and arr[y+1][x] == 0:
            pipe(y+1, x, 1)

    # 대각선 방향 (2)
    if y + 1 < N and x + 1 < N:
        if arr[y+1][x+1] == 0 and arr[y+1][x] == 0 and arr[y][x+1] == 0:
            pipe(y+1, x+1, 2)



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

if arr[N-1][N-1] == 1:
    print(0)
else:
    pipe(0, 1, 0)  
    print(result)

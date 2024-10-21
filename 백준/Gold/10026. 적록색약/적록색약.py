from collections import deque

N = int(input())
arr = [list(input()) for _ in range(N)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def count_areas(normal=True):
    visited = [[False] * N for _ in range(N)]
    color_count = 0

    def bfs(start_y, start_x, color):
        q = deque([(start_y, start_x)])
        visited[start_y][start_x] = True

        while q:
            y, x = q.popleft()
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if normal:  # 구분 가능한 경우
                        if arr[ny][nx] == color:
                            visited[ny][nx] = True
                            q.append((ny, nx))
                    else:  # R, G를 구분하지 못하는 경우
                        if (arr[ny][nx] == 'R' or arr[ny][nx] == 'G') and (color == 'R' or color == 'G'):
                            visited[ny][nx] = True
                            q.append((ny, nx))
                        elif arr[ny][nx] == 'B' and color == 'B':
                            visited[ny][nx] = True
                            q.append((ny, nx))

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                if normal:  # 구분 가능한 경우
                    bfs(y, x, arr[y][x])
                    color_count += 1
                else:  # R, G를 구분하지 못하는 경우
                    if arr[y][x] == 'R' or arr[y][x] == 'G':
                        bfs(y, x, 'R')  # R과 G를 같은 영역으로 처리
                        color_count += 1
                    elif arr[y][x] == 'B':
                        bfs(y, x, 'B')
                        color_count += 1

    return color_count

# 출력 결과
rg_blind_count = count_areas(normal=False)  # R, G를 구분하지 못하는 경우
normal_count = count_areas(normal=True)     # R, G를 구분하는 경우

print(normal_count, rg_blind_count)

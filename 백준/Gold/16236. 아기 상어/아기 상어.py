from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]  # 맵 입력

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상하좌우

def bfs(si, sj, shark):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    q.append((si, sj, 0))  # 현재 위치와 이동 시간(거리)
    visited[si][sj] = True
    fishes = []  # 먹을 수 있는 물고기 리스트
    min_dist = float('inf')  # 최소 거리

    while q:
        ci, cj, dist = q.popleft()

        if dist > min_dist:
            break  # 현재 거리보다 더 멀리 있는 물고기는 볼 필요 없음

        for dy, dx in dirs:
            ny, nx = ci + dy, cj + dx

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True

                if arr[ny][nx] == 0 or arr[ny][nx] == shark:  # 빈칸이거나 같은 크기
                    q.append((ny, nx, dist + 1))

                elif 0 < arr[ny][nx] < shark:  # 먹을 수 있는 물고기
                    fishes.append((dist + 1, ny, nx))
                    min_dist = dist + 1

    if fishes:
        # 가장 위쪽, 그리고 가장 왼쪽에 있는 물고기 선택
        fishes.sort()
        return fishes[0]  # 거리, y, x 반환
    return None

def solution():
    # 아기 상어의 초기 위치 찾기
    shark = 2  # 아기 상어 크기
    fish_count = 0  # 먹은 물고기 개수
    total_time = 0  # 총 시간

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                si, sj = i, j
                arr[i][j] = 0  # 아기 상어 위치 초기화

    while True:
        result = bfs(si, sj, shark)
        if not result:
            break  # 더 이상 먹을 물고기가 없으면 종료

        dist, ni, nj = result
        total_time += dist
        fish_count += 1
        if fish_count == shark:  # 상어 크기 증가 조건
            shark += 1
            fish_count = 0

        si, sj = ni, nj  # 아기 상어 위치 갱신
        arr[ni][nj] = 0  # 먹은 물고기 자리 비우기

    return total_time

print(solution())

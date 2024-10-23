import sys

sys.setrecursionlimit(10000)

input = sys.stdin.readline

def dfs(x, y):

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for dy, dx in dir:

        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:

            arr[ny][nx] = -1

            dfs(nx, ny)  # 이 부분에서 x, y 좌표의 순서에 유의

T = int(input())

for tc in range(T):

    M, N, K = map(int, input().split())  # M = 가로 / N = 세로 / K = 배추 개수

    arr = [[0] * M for _ in range(N)]

    for _ in range(K):

        X, Y = map(int, input().split())

        arr[Y][X] = 1

    cnt = 0

    for i in range(M):

        for j in range(N):

            if arr[j][i] == 1:

                dfs(i, j)

                cnt += 1

    print(cnt)


import sys
import heapq

input = sys.stdin.readline
tc = 1  

while True:
    N = int(input())
    if N == 0:
        break  

    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')] * N for _ in range(N)]
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  

    def dijkstra():
        hq = []
        dp[0][0] = arr[0][0]  # 시작 비용
        heapq.heappush(hq, (arr[0][0], 0, 0))  # (비용, y, x) 

        while hq:
            now_cost, y, x = heapq.heappop(hq)

            if now_cost > dp[y][x]:
                continue

            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0 <= ny < N and 0 <= nx < N:
                    new_cost = now_cost + arr[ny][nx]

                    if new_cost < dp[ny][nx]:
                        dp[ny][nx] = new_cost
                        heapq.heappush(hq, (new_cost, ny, nx))


    dijkstra()
    print(f'Problem {tc}: {dp[N - 1][N - 1]}')

    tc += 1

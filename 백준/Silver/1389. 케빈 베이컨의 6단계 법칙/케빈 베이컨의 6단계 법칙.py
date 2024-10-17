N, M = map(int, input().split())

INF = float('inf')

graph = [[INF] * (N+1) for _ in range(N+1)]

for tc in range(1, M+1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

kevin = INF
ans = 0
for i in range(N, 0, -1):
    s = sum(graph[i][1:])
    if kevin >= s:
        kevin = s
        ans = i
print(ans)
N, M = map(int, input().split())

path = []
visited = [0] * (N+1)

def dfs(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):

        visited[i] = 1
        path.append(i)
        dfs(level+1)
        path.pop()
        visited[i] = 0

dfs(0)

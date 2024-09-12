
N, M = map(int, input().split())

path = []
visited = [0] * (N+1)

def dfs(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):

        visited[i] = 1
        path.append(i)
        dfs(i, level+1)
        path.pop()
        visited[i] = 0

dfs(1, 0)
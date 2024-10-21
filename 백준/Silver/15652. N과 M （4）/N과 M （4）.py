N, M = map(int, input().split())

path = []

def dfs(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N+1):
        path.append(i)
        dfs(i, level+1)
        path.pop()


dfs(1, 0)

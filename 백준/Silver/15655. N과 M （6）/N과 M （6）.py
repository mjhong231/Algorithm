N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

path = []
visited = [0] * (N+1)

def program(start, level):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        if visited[i] == 1: continue
        visited[i] = 1
        path.append(arr[i])
        program(i+1, level+1)  
        path.pop()
        visited[i] = 0

program(0, 0)

from collections import deque

N, K = map(int, input().split())
max_length = 100000

visited = [0] * (max_length+1)

def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(visited[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_length and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
bfs()

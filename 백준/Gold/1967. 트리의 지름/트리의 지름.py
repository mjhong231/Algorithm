N = int(input())  # 노드 개수

lst = [[] for _ in range(N+1)]  # 트리

for _ in range(N-1):
    p, c, cost = map(int, input().split())
    lst[p].append((c, cost))
    lst[c].append((p, cost))

from collections import deque

def bfs(start):
    q = deque()
    visited = [False] * (N+1)
    visited[start] = True
    q.append(start)

    while q:
        now = q.popleft()

        for next, next_cost in lst[now]:
            if visited[next] == False:
                q.append(next)
                visited[next] = visited[now] + next_cost


    result = max(visited)
    return [visited.index(result), result]


print(bfs(bfs(1)[0])[1]-1)
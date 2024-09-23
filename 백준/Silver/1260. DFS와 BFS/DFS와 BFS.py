N, M, V = map(int, input().split())

lst = [[0] * (N+1) for _ in range(N+1)]
for tc in range(M):
    a, b = map(int, input().split())
    lst[a][b] = lst[b][a] = 1

# 방문 체크
visited1 = [0] * (N+1)
visited2 = [0] * (N+2)

# dfs 함수 만들기
def dfs(V):
    visited1[V] = 1
    print(V, end= ' ')
    for i in range(1, N+1):
        if lst[V][i] == 1 and visited1[i] == 0:
            dfs(i)


# bfs 함수 만들기
def bfs(V):
    q = [V]
    visited2[V] = 1
    while q:
        V = q.pop(0)
        print(V, end = ' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and lst[V][i] == 1:
                q.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)
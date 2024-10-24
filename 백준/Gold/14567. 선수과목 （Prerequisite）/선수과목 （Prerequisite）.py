import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 과목의 수 / M: 선수 조건의 수
lst = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    lst[A].append(B)
    indegree[B] += 1

from collections import deque

q = deque()
result = [float('inf') for _ in range(N+1)]

for node in range(1, N+1):
    if indegree[node] == 0:
        q.append((1, node))


while q:
    cnt, now = q.popleft()
    if result[now] > cnt:
        result[now] = cnt
    # 이제 과목하나 수강 해서 이 과목을 선수과목으로 삼는 애가 있는지 확인
    for next_node in lst[now]:
        indegree[next_node] -= 1
        if not indegree[next_node]:
            q.append((cnt + 1, next_node))

print(*result[1:])